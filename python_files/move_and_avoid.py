# move_and_avoid.py

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from urandom import randint

# --- SETUP
# start components
hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)

distance_sensor = UltrasonicSensor(Port.C)

# store variables

# --- RUNNING
while True:
    # read sensor data
    distance_reading = distance_sensor.distance()
    
    # process data

    # output data
    if distance_reading > 100:
        robot.drive(500, 0)
    else:
        robot.stop()
        angle = randint(-180, 180)
        robot.turn(angle)