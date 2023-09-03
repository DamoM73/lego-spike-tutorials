# motor_inputs.py

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
hub = PrimeHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

left_motor.reset_angle(0)

# --- MAIN LOOP
while True:
    pressed = hub.buttons.pressed()

    if Button.LEFT in pressed and Button.RIGHT in pressed:
        print("Angel:", left_motor.angle())
        left_motor.run_target(1000, 0)
        print("Angel:", left_motor.angle())
    
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
            print("Torque load:", left_motor.load())
    
    else:
        left_motor.stop()
