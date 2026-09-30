from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
force_sensor = ForceSensor(Port.B)

# Main loop
while True:
    # Input
    force_reading = round(force_sensor.force(), 1)
    distance_reading = round(force_sensor.distance(), 1)
    is_pressed = force_sensor.pressed(3)
    is_touched = force_sensor.touched()

    # Output
    print(
        "Force:", force_reading,
        "Distance:", distance_reading,
        "Pressed:", is_pressed,
        "Touched:", is_touched,
    )
    wait(200)
