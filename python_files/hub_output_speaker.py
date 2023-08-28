# speaker.py

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP

hub = PrimeHub()


# --- MAIN LOOP
while True:
    
    hub.speaker.volume(100)
    current_volume = str(hub.speaker.volume())
    hub.display.text(current_volume)
    hub.speaker.beep(440,500)
    
    hub.speaker.volume(50)
    current_volume = str(hub.speaker.volume())
    hub.display.text(current_volume)
    hub.speaker.beep(440,500)
    
    oh_when_the_saints = [
        "C4/4", "E4/4", "F4/4", "G4/1",
        "C4/4", "E4/4", "F4/4", "G4/1",
        "C4/4", "E4/4", "F4/4", "G4/2",
        "E4/2", "C4/2", "E4/2", "D4/1",
        "E4/4", "E4/4", "D4/4", "C4/2",
        "C4/2", "E4/2", "G4/4", "G4/4", "G4/4", "F4/1",
        "E4/4", "F4/4", "G4/2", "E4/2", "C4/2", "D4/2", "C4/1"
    ]

    hub.speaker.play_notes(oh_when_the_saints,180)