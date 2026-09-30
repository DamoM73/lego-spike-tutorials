# Exercise 1
# Can you create a program that compares the three ways of stopping? It
# should:
# - run the left motor at full power for 1 second, then stop() it, with the
#   status light green
# - run it again, then brake() it, with the status light orange
# - run it again, then hold() it, with the status light red
# - wait 1 second after each stop, and repeat
#

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)

# Main loop
while True:
    pass
