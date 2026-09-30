from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
colour_sensor = ColorSensor(Port.D)
colour_sensor.detectable_colors([Color.RED, Color.BLUE, Color.NONE])

# Main loop
while True:
    print(colour_sensor.color())
    wait(200)
