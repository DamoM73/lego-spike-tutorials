# check_config.py

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.iodevices import PUPDevice

# ---- DETECT WHAT IS CONNECTED TO EACH PORT ----
device_names = {
    48: "SPIKE Medium Angular Motor",
    49: "SPIKE Large Angular Motor",
    61: "SPIKE Color Sensor",
    62: "SPIKE Ultrasonic Sensor",
    63: "SPIKE Force Sensor"
}

ports = [Port.A, Port.B, Port.C, Port.D, Port.F]

print("Hub configuration")

for port in ports:
    device = PUPDevice(port)
    print(port, ": ", device_names[device.info()["id"]])

# CHECK THAT LEFT AND RIGHT MOTORS ARE CONNECTED TO CORRECT PORTS
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=57, axle_track=80)

drive_base.turn(360)