from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)

# Main loop
while True:
    hub.light.on(Color.GREEN)
    left_motor.dc(100)
    wait(1000)
    left_motor.stop()
    wait(1000)

    hub.light.on(Color.ORANGE)
    left_motor.dc(100)
    wait(1000)
    left_motor.brake()
    wait(1000)

    hub.light.on(Color.RED)
    left_motor.dc(100)
    wait(1000)
    left_motor.hold()
    wait(1000)
