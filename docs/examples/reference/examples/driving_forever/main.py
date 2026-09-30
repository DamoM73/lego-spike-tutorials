from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)
my_robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)

# Main loop
while True:
    hub.light.on(Color.WHITE)
    my_robot.drive(200, 0)
    wait(1000)

    hub.light.on(Color.RED)
    my_robot.drive(200, -90)
    wait(1000)

    my_robot.stop()
    wait(1000)

    hub.light.on(Color.WHITE)
    my_robot.drive(200, 0)
    wait(1000)

    hub.light.on(Color.GREEN)
    my_robot.drive(200, 90)
    wait(1000)

    my_robot.stop()
    wait(1000)
