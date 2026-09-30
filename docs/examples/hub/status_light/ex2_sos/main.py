# Exercise 2
# Can you make the status light blink SOS in Morse code? SOS is three short
# blinks, three long blinks, then three short blinks. Make the long blinks
# three times as long as the short ones.
#

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
hub.light.blink(Color.RED, [500, 250])

# Main loop
while True:
    pass
