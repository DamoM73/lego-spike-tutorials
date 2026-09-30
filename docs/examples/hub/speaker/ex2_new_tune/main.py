# Exercise 2
# Can you change the program so the hub plays a different tune, such as
# *Twinkle Twinkle Little Star*?
#

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
saints = [
    "C4/4", "E4/4", "F4/4", "G4/1",
    "C4/4", "E4/4", "F4/4", "G4/1",
    "C4/4", "E4/4", "F4/4", "G4/2", "E4/2",
    "C4/2", "E4/2", "D4/1",
]

# Main loop
while True:
    hub.speaker.play_notes(saints, 180)
    wait(1000)
