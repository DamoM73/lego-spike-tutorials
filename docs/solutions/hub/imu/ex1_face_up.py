from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()

# Main loop
while True:
    up = hub.imu.up()
    if up == Side.TOP:
        hub.display.icon(Icon.HAPPY)
        hub.light.off()
    elif up == Side.BOTTOM:
        hub.display.off()
        hub.light.on(Color.RED)
    else:
        hub.display.off()
        hub.light.off()
    wait(100)
