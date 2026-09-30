# Exercise 1
# Can you create a parking sensor? It should:
# - turn the status light green when the nearest object is more than 300 mm
#   away
# - turn it yellow between 100 mm and 300 mm
# - turn it red and beep when the object is closer than 100 mm
#

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
distance_sensor = UltrasonicSensor(Port.C)

# Main loop
while True:
    pass
