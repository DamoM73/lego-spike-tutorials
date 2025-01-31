from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
# start components
hub = PrimeHub()

# store variables

# --- RUNNING
while True:
    # read sensor data
    up  = hub.imu.up()
    pitch, roll = hub.imu.tilt()
    
    # process data

    # output data
    print(up, "\t", pitch, "\t", roll)