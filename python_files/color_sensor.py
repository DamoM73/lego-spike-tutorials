# color_sensor

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
hub = PrimeHub()
color_sensor = ColorSensor(Port.D)
modes = ["S", "L", "R", "A"]
mode = 0

# --- MAIN LOOP
while True:
    presses = hub.buttons.pressed()

    if Button.LEFT in presses and mode > 0:
        mode -= 1
        wait(250)
    elif Button.RIGHT in presses and mode < 3:
        mode += 1
        wait(250)

    hub.display.char(modes[mode])
    
    if mode == 0:
        print(color_sensor.color())
    elif mode == 1:
        print(color_sensor.color(False))
    elif mode == 2:
        print(color_sensor.reflection())
    elif mode == 3:
        print(color_sensor.ambient())