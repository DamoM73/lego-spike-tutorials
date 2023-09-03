# imu_orientation

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
hub = PrimeHub()

# --- MAIN LOOP
while True:
    up  = hub.imu.up()
    pitch, roll = hub.imu.tilt()

    print(up, "\t", pitch, "\t", roll)