# drive_base_inputs.py

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
my_robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)

my_robot.reset()

# --- MAIN LOOP
while True:
    pressed = hub.buttons.pressed()
    
    if Button.LEFT in pressed:
        distance, speed, angle, rate_of_turn = my_robot.state()
        print("Start - distance:", distance, "speed:", speed, "angle:", angle, "rate of turn:", rate_of_turn)
        my_robot.curve(100, 180)
        distance, speed, angle, rate_of_turn = my_robot.state()
        print("Start - distance:", distance, "speed:", speed, "angle:", angle, "rate of turn:", rate_of_turn)

    elif Button.RIGHT in pressed:
        distance = my_robot.distance()
        print("Start distance:", distance)
        my_robot.straight(500)
        distance = my_robot.distance()
        print("End distance:", distance)

    elif Button.BLUETOOTH in pressed:
        angle = my_robot.angle()
        print("Start angle:", angle)
        my_robot.turn(-90)
        angle = my_robot.angle()
        print("End angle:", angle)

    else:
        my_robot.stop()