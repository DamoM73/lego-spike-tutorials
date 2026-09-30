from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)

# Main loop
while True:
    hub.light.on(Color.BROWN)
    left_motor.run_time(1000, 1000, Stop.COAST, wait=False)
    right_motor.run_time(1000, 1000, Stop.COAST)

    hub.light.on(Color.VIOLET)
    left_motor.run_angle(1000, 180, wait=False)
    right_motor.run_angle(1000, 180)

    hub.light.on(Color.CYAN)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run_target(1000, 180, wait=False)
    right_motor.run_target(1000, 180)

    hub.light.on(Color.GRAY)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.track_target(180)
    right_motor.track_target(180)
    wait(1000)
