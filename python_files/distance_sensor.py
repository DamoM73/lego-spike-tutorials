# distance_sensor.py

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
hub = PrimeHub()
distance_sensor = UltrasonicSensor(Port.C)

# --- MAIN LOOP
while True:
    distance = distance_sensor.distance()
    present = distance_sensor.presence()

    print("Distance:", distance, "\tDetected other sensor:", present)

    distance_sensor.lights.off()
    wait(100)
    distance_sensor.lights.on(100)