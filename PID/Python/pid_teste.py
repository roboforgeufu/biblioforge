#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import (  # type: ignore
    ColorSensor,
    GyroSensor,
    InfraredSensor,
    Motor,
    TouchSensor,
    UltrasonicSensor,
)
from pybricks.hubs import EV3Brick  # type: ignore
from pybricks.media.ev3dev import ImageFile, SoundFile  # type: ignore
from pybricks.parameters import Button, Color, Direction, Port, Stop  # type: ignore
from pybricks.robotics import DriveBase  # type: ignore
from pybricks.tools import DataLog, StopWatch, wait  # type: ignore

right_motor = Motor(Port.C)
left_motor = Motor(Port.B)

WHEEL_DIAMETER = 5.5
WHEEL_DISTANCE = 11
PROPORTIONAL_GAIN = 2
DERIVATIVE_GAIN = 0.5
INTEGRAL_GAIN = 0.1

def reset_angle():

    right_motor.reset_angle(0)
    left_motor.reset_angle(0)

def turn(graus_reais):

    reset_angle()

    graus_motor = graus_reais * (WHEEL_DISTANCE/WHEEL_DIAMETER)

    last_error = 0
    i_sum = 0
    '''while(graus_motor > (right_motor.angle() + left_motor.angle())/2):'''
    while True:
        
        error = graus_motor - (right_motor.angle() + abs(left_motor.angle()))/2
        i_sum += error
        p = PROPORTIONAL_GAIN * error
        d = DERIVATIVE_GAIN * (error - last_error)
        i = INTEGRAL_GAIN * i_sum

        pid_error = p + i + d

        right_motor.run(pid_error)
        left_motor.run(-pid_error)

        last_error = error

        print("target:", graus_motor, "angle:", (right_motor.angle() + abs(left_motor.angle()))/2, "speed:", (right_motor.speed() + abs(left_motor.speed()))/2, "integral error:", i_sum, "pid:", pid_error)


def main():

    turn(90)

main()





