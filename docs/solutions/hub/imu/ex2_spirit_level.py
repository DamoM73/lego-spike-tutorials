from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()

# Main loop
while True:
    pitch, roll = hub.imu.tilt()
    if abs(pitch) <= 3 and abs(roll) <= 3:
        hub.display.icon(Icon.HAPPY)
    else:
        hub.display.icon(Icon.SAD)
    wait(100)
