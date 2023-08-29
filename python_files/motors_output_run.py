# motors_run_forever.py

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
hub = PrimeHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)

# --- MAIN LOOP
while True:
    left_motor.run(1000)
    right_motor.run(1000)
    wait(1000)

    left_motor.dc(50)
    right_motor.dc(50)
    wait(1000)