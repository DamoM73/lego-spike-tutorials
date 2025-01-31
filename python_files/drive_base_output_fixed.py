from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
# start components
hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
my_robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)

# store variables

# --- RUNNING
while True:
    # read sensor data
    
    # process data
    
    # output data
    hub.light.on(Color.YELLOW)
    my_robot.settings(200, 200, 200, 200)
    print(my_robot.settings())
    my_robot.straight(200)
    my_robot.turn(90)
    my_robot.curve(100,180)

    hub.light.on(Color.MAGENTA)
    my_robot.settings(500, 500, 500, 500)
    print(my_robot.settings())
    my_robot.straight(200)
    my_robot.turn(90)
    my_robot.curve(100,180)