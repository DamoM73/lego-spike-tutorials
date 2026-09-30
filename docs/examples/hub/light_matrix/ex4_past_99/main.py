# Exercise 4
# Run the number() example and wait. What happens when count goes past 99? Why
# do you think this happens?
#

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
count = 0

# Main loop
while True:
    hub.display.number(count)
    count = count + 1
    wait(500)
