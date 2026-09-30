# Exercise 3
# What is the closest distance the sensor can measure? What is the furthest?
# What happens when you point it at a jumper or at a wall at an angle? Why do
# you think this happens?
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
    print(distance_sensor.distance())
    wait(200)
