from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
colour_sensor = ColorSensor(Port.D)
modes = ["S", "L", "R", "A"]
mode = 0

# Main loop
while True:
    # Input
    pressed = hub.buttons.pressed()
    if mode == 0:
        reading = colour_sensor.color()
    elif mode == 1:
        reading = colour_sensor.color(False)
    elif mode == 2:
        reading = colour_sensor.reflection()
    else:
        reading = colour_sensor.ambient()

    # Process
    if Button.LEFT in pressed and mode > 0:
        mode = mode - 1
        wait(250)
    elif Button.RIGHT in pressed and mode < 3:
        mode = mode + 1
        wait(250)

    # Output
    hub.display.char(modes[mode])
    print(modes[mode], reading)
    wait(100)
