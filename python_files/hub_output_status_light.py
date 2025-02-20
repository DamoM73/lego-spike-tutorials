from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
# start components
hub = PrimeHub()

# store variables

# --- RUNNING
while True:
    # read sensor data

    # process data

    # output data
    hub.light.on(Color.MAGENTA)
    wait(1000)
    hub.light.blink(Color.RED, [500,250,500,250])
    wait(1500)
    hub.light.animate([Color.GREEN, Color.WHITE, Color.ORANGE],1000)
    wait(3000)
    hub.light.off()
    wait(1000)