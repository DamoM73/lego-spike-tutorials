from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
count = 10

# Main loop
while True:
    hub.display.number(count)
    wait(1000)
    count = count - 1
    if count < 0:
        hub.display.icon(Icon.HAPPY)
        wait(3000)
        count = 10
