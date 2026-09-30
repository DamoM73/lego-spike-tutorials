from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
count = 0

# Main loop
while True:
    pressed = hub.buttons.pressed()
    if Button.LEFT in pressed:
        count = count + 1
        wait(250)
    elif Button.RIGHT in pressed:
        count = count - 1
        wait(250)
    hub.display.number(count)
