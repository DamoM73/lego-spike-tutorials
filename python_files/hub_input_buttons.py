# buttons.py

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
hub = PrimeHub()


# --- MAIN LOOP
while True:
    pressed = hub.buttons.pressed()
    
    if Button.LEFT in pressed:
        hub.display.icon(Icon.ARROW_LEFT)
    elif Button.RIGHT in pressed:
        hub.display.icon(Icon.ARROW_RIGHT)
    elif Button.CENTER in pressed:
        hub.display.icon(Icon.CIRCLE)
    elif Button.BLUETOOTH in pressed:
        hub.display.char("B")
    else:
        hub.display.off()