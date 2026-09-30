from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
distance_sensor = UltrasonicSensor(Port.C)

# Main loop
while True:
    distance = distance_sensor.distance()
    if distance < 100:
        hub.light.on(Color.RED)
        hub.speaker.beep(1000, 100)
    elif distance < 300:
        hub.light.on(Color.YELLOW)
    else:
        hub.light.on(Color.GREEN)
    wait(100)
