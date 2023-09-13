# calibration.py

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# SETUP
hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
my_robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)

# MAIN LOOP
while True:
    pressed = hub.buttons.pressed()

    if Button.LEFT in pressed:
        # wheel diameter test
        hub.speaker.beep()
        wait(500)
        my_robot.straight(1000)
    elif Button.RIGHT in pressed:
        # axel track test
        hub.speaker.beep()
        wait(500)
        my_robot.turn(720)