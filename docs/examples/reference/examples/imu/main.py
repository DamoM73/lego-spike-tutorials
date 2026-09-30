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
    up = hub.imu.up()
    pitch, roll = hub.imu.tilt()
    heading = hub.imu.heading()

    # Output
    print(up, "Pitch:", pitch, "Roll:", roll, "Heading:", heading)
    wait(200)
