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
    hub.light.on(Color.GREEN)

    left_motor.dc(100)
    right_motor.dc(100)
    wait(1000)
    
    left_motor.stop()
    right_motor.stop()
    wait(500)

    hub.light.on(Color.ORANGE)

    left_motor.dc(100)
    right_motor.dc(100)
    wait(1000)
    
    left_motor.brake()
    right_motor.brake()
    wait(500)

    hub.light.on(Color.VIOLET)

    left_motor.dc(100)
    right_motor.dc(100)
    wait(1000)
    
    left_motor.hold()
    right_motor.hold()
    wait(500)