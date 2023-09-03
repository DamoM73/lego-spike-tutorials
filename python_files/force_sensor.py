# force_sensor.py

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
hub = PrimeHub()
force_sensor = ForceSensor(Port.F)

# --- MAIN LOOP
while True:
    force_reading = round(force_sensor.force(), 1)
    distance_reading = round(force_sensor.distance(), 1)
    is_pressed = force_sensor.pressed(3)
    is_touched = force_sensor.touched()

    print(
        "Force:", force_reading,
        "\tDistance:", distance_reading,
        "\tForce > 3:", is_pressed,
        "\tTouched:", is_touched
    )