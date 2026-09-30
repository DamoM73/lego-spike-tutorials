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
    wait(3000)
    hub.light.on(Color.YELLOW)
    wait(1000)
    hub.light.on(Color.RED)
    wait(3000)
