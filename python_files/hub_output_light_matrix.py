from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
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
    hub.display.orientation(Side.RIGHT)
    hub.display.icon(Icon.UP)
    wait(250)
    hub.display.orientation(Side.BOTTOM)
    hub.display.icon(Icon.UP)
    wait(250)
    hub.display.orientation(Side.LEFT)
    hub.display.icon(Icon.UP)
    wait(250)
    hub.display.orientation(Side.TOP)
    hub.display.icon(Icon.UP)
    wait(250)

    hub.display.off()
    wait(500)

    hub.display.pixel(1,1,100)
    hub.display.pixel(1,3,100)
    hub.display.pixel(3,1,100)
    hub.display.pixel(3,2,100)
    hub.display.pixel(3,3,100)
    wait(1000)

    hub.display.off()
    wait(500)

    arrows = [Icon.RIGHT, Icon.DOWN, Icon.LEFT, Icon.UP]
    hub.display.animate(arrows, 500)
    wait(1000)

    hub.display.off()
    wait(500)

    hub.display.char("R")
    wait(500)
    hub.display.number(2)
    wait(500)
    hub.display.char("D")
    wait(500)
    hub.display.number(2)
    wait(500)

    hub.display.off()
    wait(1000)

    hub.display.text("C3PO", 500, 50)

    hub.display.off()
    wait(2000)