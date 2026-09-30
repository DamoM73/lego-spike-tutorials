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
my_robot.reset()

# Main loop
while True:
    # Input
    pressed = hub.buttons.pressed()

    # Process and output
    if Button.LEFT in pressed:
        print("Arc - start:", my_robot.state())
        my_robot.arc(100, angle=180)
        print("Arc - end:", my_robot.state())
    elif Button.RIGHT in pressed:
        print("Straight - start distance:", my_robot.distance())
        my_robot.straight(500)
        print("Straight - end distance:", my_robot.distance())
    elif Button.BLUETOOTH in pressed:
        print("Turn - start angle:", my_robot.angle())
        my_robot.turn(-90)
        print("Turn - end angle:", my_robot.angle())
    else:
        my_robot.stop()
