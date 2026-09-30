# Exercise 1
# Can you make the hub's status light show the same colour that the colour
# sensor sees? When the sensor sees no colour, the status light should be off.
#

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
colour_sensor = ColorSensor(Port.D)

# Main loop
while True:
    pass
