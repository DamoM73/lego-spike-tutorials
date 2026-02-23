from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
# start components
hub = PrimeHub()
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)

# store variables

# --- RUNNING
while True:
    # read sensor data

    # process data

    # output data
    left_motor.run(1000)
    right_motor.run(1000)
    wait(1000)

    left_motor.dc(50)
    right_motor.dc(50)
    wait(1000)