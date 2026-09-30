# Exercise 1
# Can you turn the robot into a force meter that shows the force on the
# display as a whole number of newtons? int() may help.
#

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
force_sensor = ForceSensor(Port.B)

# Main loop
while True:
    pass
