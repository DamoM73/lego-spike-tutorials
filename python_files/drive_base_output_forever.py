# drive_base_forever.py

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
hub = PrimeHub()

# create drive base
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
my_robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)

# --- MAINLOOP
while True:
    hub.light.on(Color.WHITE)
    my_robot.drive(1000, 0)
    wait(500)

    hub.light.on(Color.RED)
    my_robot.drive(1000, -300)
    wait(500)

    my_robot.stop()
    wait(1000)

    hub.light.on(Color.WHITE)
    my_robot.drive(1000, 0)
    wait(500)

    hub.light.on(Color.GREEN)
    my_robot.drive(1000, 300)
    wait(500)

    my_robot.stop()
    wait(1000)