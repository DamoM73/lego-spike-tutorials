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
    hub.speaker.volume(100)
    hub.display.number(hub.speaker.volume())
    hub.speaker.beep(440, 500)

    hub.speaker.volume(50)
    hub.display.number(hub.speaker.volume())
    hub.speaker.beep(440, 500)

    hub.speaker.play_notes(saints, 180)
