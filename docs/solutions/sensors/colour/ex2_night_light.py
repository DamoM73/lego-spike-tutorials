from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
colour_sensor = ColorSensor(Port.D)

# Main loop
while True:
    if colour_sensor.ambient() < 10:
        hub.light.on(Color.WHITE)
    else:
        hub.light.off()
    wait(100)
