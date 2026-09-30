from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
left_motor.reset_angle(0)

# Main loop
while True:
    # Input
    pressed = hub.buttons.pressed()

    # Process and output
    if Button.LEFT in pressed and Button.RIGHT in pressed:
        print("Angle:", left_motor.angle())
        left_motor.run_target(1000, 0)
        print("Angle:", left_motor.angle())
        wait(500)
    elif Button.LEFT in pressed:
        left_motor.run(300)
        wait(250)
        print("Speed:", left_motor.speed())
        wait(500)
        left_motor.stop()
    elif Button.RIGHT in pressed:
        left_motor.run(300)
        if left_motor.stalled():
            print("Stalled")
        else:
            print("Load:", left_motor.load())
        wait(200)
    else:
        left_motor.stop()
