# Exercise 1
# Can you change the program so it also shows a right arrow when the right
# button is pressed, and the letter B when the Bluetooth button is pressed?
#

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()

# Main loop
while True:
    pressed = hub.buttons.pressed()
    if Button.LEFT in pressed:
        hub.display.icon(Icon.ARROW_LEFT)
    else:
        hub.display.off()
