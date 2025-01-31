from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
# start components
hub = PrimeHub()
distance_sensor = UltrasonicSensor(Port.C)

# store variables

# --- RUNNING
while True:
    # read sensor data
    distance = distance_sensor.distance()
    present = distance_sensor.presence()
    
    # process data
    
    # output data
    print("Distance:", distance, "\tDetected other sensor:", present)

    distance_sensor.lights.off()
    wait(100)
    distance_sensor.lights.on(100)