#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick  # type: ignore
from pybricks.ev3devices import (  # type: ignore
    Motor,
)
from pybricks.parameters import Port  # type: ignore
from pybricks.tools import StopWatch, wait  # type: ignore

import socket

ev3 = EV3Brick()

right_motor = Motor(Port.C)
left_motor = Motor(Port.B)

WHEEL_DIAMETER = 5.5
WHEEL_DISTANCE = 11.25
KP = 3.2
KD = 0.7
KI = 0.3


def reset_angle():
    right_motor.reset_angle(0)
    left_motor.reset_angle(0)


def server_start():
    client_connection = socket.socket()
    port = 12345
    client_connection.bind(("", port))
    client_connection.listen(5)
    print("Waiting for connection...")
    ev3.speaker.beep()
    ev3.screen.print("Waiting for connection")
    ev3.screen.print("    with computer...")
    client, addr = client_connection.accept()
    ev3.screen.clear()
    ev3.screen.print("Connection successful!")
    ev3.speaker.beep()
    wait(500)

    return client, addr


def send_message(client, message):
    message = ",".join(map(str, message))
    client.send(message.encode())
    recv_message = str(client.recv(1024).decode())

    return recv_message


def server_end(client):
    message = "end"
    client.send(message.encode())
    ev3.screen.clear()
    ev3.screen.print("Server: ")
    ev3.screen.print(str(client.recv(1024).decode()))
    client.close()
    wait(700)
    ev3.screen.clear()
    ev3.screen.print("Connection ended!")
    wait(1000)


def pid(target, current_angle, KP, KD, KI, last_error, i_gain):
    error = target - current_angle

    p_gain = KP * error

    d_gain = KD * (last_error - error)

    if abs(error) < 7:
        i_gain += KI * error

    pid = p_gain + d_gain + i_gain

    last_error = error

    return (error, p_gain, d_gain, i_gain, pid)


def turn(graus_reais, client, instance, watch):
    reset_angle()

    error = 0
    current_angle = 0
    i_gain = 0
    pid_correction = 0
    graus_motor = graus_reais * (WHEEL_DISTANCE / WHEEL_DIAMETER)

    while (
        0.99 > abs(current_angle / graus_motor)
        or abs(current_angle / graus_motor) > 1.01
        or abs(pid_correction) > 1
    ):
        current_angle = right_motor.angle()
        error = graus_motor - current_angle

        target = graus_motor

        error, p_gain, d_gain, i_gain, pid_correction = pid(
            target, current_angle, KP, KD, KI, error, i_gain
        )

        right_motor.run(pid_correction)
        left_motor.run(-pid_correction)

        time = watch.time()

        log = [
            time,
            instance,
            p_gain,
            d_gain,
            i_gain,
            pid_correction,
            current_angle,
            target,
        ]

        # Sending values to client and receiving feedback
        recv_message = send_message(client, log)

        ev3.screen.clear()
        ev3.screen.print("Server: " + recv_message)

        print(
            "Target:",
            graus_motor,
            "Angle:",
            current_angle,
            "KP:",
            p_gain,
            "KD:",
            d_gain,
            "KI:",
            i_gain,
            "PID",
            pid_correction,
        )


def main():
    # Starting server
    client, addr = server_start()
    watch = StopWatch()

    while True:
        turn(90, client, watch)
        break

    server_end(client)


main()
