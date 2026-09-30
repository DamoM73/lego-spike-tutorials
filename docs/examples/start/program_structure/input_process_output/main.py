from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()

# Main loop
while True:
    # Input
    pressed = hub.buttons.pressed()

    # Process
    if Button.LEFT in pressed:
        colour = Color.RED
    else:
        colour = Color.GREEN

    # Output
    hub.light.on(colour)
