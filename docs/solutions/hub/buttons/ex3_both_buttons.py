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
    if Button.LEFT in pressed and Button.RIGHT in pressed:
        hub.display.icon(Icon.ARROW_DOWN)
    elif Button.LEFT in pressed:
        hub.display.icon(Icon.ARROW_LEFT)
    else:
        hub.display.off()
