from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
twinkle = [
    "C4/4", "C4/4", "G4/4", "G4/4", "A4/4", "A4/4", "G4/2",
    "F4/4", "F4/4", "E4/4", "E4/4", "D4/4", "D4/4", "C4/2",
]

# Main loop
while True:
    hub.speaker.play_notes(twinkle, 120)
    wait(1000)
