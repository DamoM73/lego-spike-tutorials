# Exercise 3
# What are the lowest and highest beep frequencies you can hear? What happens
# outside that range? Why do you think this happens?
#

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()

# Main loop
while True:
    hub.speaker.beep(440, 500)
    wait(500)
