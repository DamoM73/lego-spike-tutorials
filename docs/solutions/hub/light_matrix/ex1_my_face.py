from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()

# Main loop
while True:
    hub.display.pixel(1, 1, 100)
    hub.display.pixel(1, 3, 100)
    hub.display.pixel(3, 0, 100)
    hub.display.pixel(4, 1, 100)
    hub.display.pixel(4, 2, 100)
    hub.display.pixel(4, 3, 100)
    hub.display.pixel(3, 4, 100)
