# Exercise 3
# Change the threshold in pressed() from 5 to 0, then to 15. What happens each
# time? Why do you think this happens?
#

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
force_sensor = ForceSensor(Port.B)

# Main loop
while True:
    if force_sensor.pressed(5):
        hub.light.on(Color.GREEN)
    else:
        hub.light.off()
