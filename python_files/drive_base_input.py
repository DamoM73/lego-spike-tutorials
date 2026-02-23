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
my_robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)
my_robot.reset()

# store variables
mode_message = ""
start_message = ""
end_message = ""

# --- RUNNING
while True:
    # read sensor data
    pressed = hub.buttons.pressed()
    
    # process data
    if Button.LEFT in pressed:
        distance, speed, angle, rate_of_turn = my_robot.state()
        mode_message = "Curved drive"
        start_message = "Start - distance: " + str(distance) + ", speed: " + str(speed) + ", angle: " + str(angle) + ", rate of turn: " + str(rate_of_turn)
        my_robot.curve(100, 180)
        distance, speed, angle, rate_of_turn = my_robot.state()
        end_message = "End - distance: " + str(distance) + ", speed: " + str(speed) + ", angle: " + str(angle) + ", rate of turn: " + str(rate_of_turn)

    elif Button.RIGHT in pressed:
        distance = my_robot.distance()
        mode_message = "Straight drive"
        start_message = "Start distance: " + str(distance)
        my_robot.straight(500)
        distance = my_robot.distance()
        end_message = "End distance: " + str(distance)

    elif Button.BLUETOOTH in pressed:
        angle = my_robot.angle()
        mode_message = "Turn on spot"
        start_message = "Start angle:" + str(angle)
        my_robot.turn(-90)
        angle = my_robot.angle()
        end_message = "End angle:" + str(angle)

    else:
        my_robot.stop()
        
    # output data
    print(mode_message)
    print("========================")
    print(start_message)
    print(end_message)
    print()