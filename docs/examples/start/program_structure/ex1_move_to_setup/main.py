# Exercise 1
# What happens if we move hub.speaker.beep() into the main loop? Why do you
# think this happens?
#

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
hub.speaker.beep()

# Main loop
while True:
    hub.light.on(Color.GREEN)
    wait(500)
    hub.light.off()
    wait(500)
