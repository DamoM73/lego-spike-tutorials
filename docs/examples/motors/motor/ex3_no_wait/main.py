# Exercise 3
# Run the program. Do the wheels turn at the same time or one after the other?
# Why do you think this happens?
#

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)

# Main loop
while True:
    left_motor.run_angle(500, 360)
    right_motor.run_angle(500, 360)
    wait(1000)
