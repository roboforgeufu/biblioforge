#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import (  # type: ignore
    Motor,
)
from pybricks.parameters import Port  # type: ignore
from pybricks.tools import DataLog, StopWatch, wait  # type: ignore

right_motor = Motor(Port.C)
left_motor = Motor(Port.B)

WHEEL_DIAMETER = 5.5
WHEEL_DISTANCE = 11.15
KP = 3.2
KD = 0.7
KI = 0.3


def reset_angle():
    right_motor.reset_angle(0)
    left_motor.reset_angle(0)


def turn(instance, graus_reais):
    error = 0
    current_angle = 0
    i_gain = 0

    data = DataLog(
        "Time",
        "Instance",
        "KP",
        "KD",
        "KI",
        "PID",
        "Angle",
        name="log_turn_PID",
        timestamp=False,
        append=instance > 1,
    )

    graus_motor = graus_reais * (WHEEL_DISTANCE / WHEEL_DIAMETER)
    pid_correction = 0
    watch = StopWatch()

    reset_angle()

    while (
        0.99 > abs(current_angle / graus_motor)
        or abs(current_angle / graus_motor) > 1.01
        or abs(pid_correction) > 1
    ):
        current_angle = right_motor.angle()
        last_error = error
        error = graus_motor - current_angle

        p_gain = KP * error

        d_gain = KD * (last_error - error)

        if abs(error) < 7:
            i_gain += KI * error

        pid_correction = p_gain + d_gain + i_gain

        right_motor.run(pid_correction)
        left_motor.run(-pid_correction)

        time = watch.time()

        data.log(time, instance, p_gain, d_gain, i_gain, pid_correction, current_angle)

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
    i = 1
    side = 1
    while i <= 8:
        turn(i, side * 180)
        i += 1
        side *= -1
        wait(500)


main()
