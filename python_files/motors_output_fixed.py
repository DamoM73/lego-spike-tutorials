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
    hub.light.on(Color.BROWN)    
    
    left_motor.run_time(1000, 1000, Stop.COAST)
    right_motor.run_time(1000, 1000, Stop.COAST)

    hub.light.on(Color.VIOLET)

    left_motor.run_angle(1000, 180)
    right_motor.run_angle(1000, 180)

    hub.light.on(Color.CYAN)

    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run_target(1000, 180)
    right_motor.run_target(1000, 180)

    hub.light.on(Color.GRAY)

    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.track_target(180)
    right_motor.track_target(180)

    wait(1000)