from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()

# Main loop
while True:
    # Input
    pressed = hub.buttons.pressed()

    # Output
    if Button.LEFT in pressed and Button.RIGHT in pressed:
        hub.display.icon(Icon.ARROW_DOWN)
    elif Button.LEFT in pressed:
        hub.display.icon(Icon.ARROW_LEFT)
    elif Button.RIGHT in pressed:
        hub.display.icon(Icon.ARROW_RIGHT)
    elif Button.BLUETOOTH in pressed:
        hub.display.char("B")
    else:
        hub.display.off()
