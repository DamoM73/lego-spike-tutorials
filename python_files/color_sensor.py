from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# --- SETUP
# start components
hub = PrimeHub()
color_sensor = ColorSensor(Port.D)

# store variables
modes = ["S", "L", "R", "A"]
mode = 0

# --- RUNNING
while True:
    # read sensor data
    presses = hub.buttons.pressed()
    
    if mode == 0:
        mode_type = "Surface reading:"
        colour_reading = color_sensor.color()
    elif mode == 1:
        mode_type = "Light source reading:"
        colour_reading = color_sensor.color(False)
    elif mode == 2:
        mode_type = "Reflective light reading:"
        colour_reading = color_sensor.reflection()
    elif mode == 3:
        mode_type = "Ambient light reading:"
        colour_reading = color_sensor.ambient()
        
     
    # process data
    if Button.LEFT in presses and mode > 0:
        mode -= 1
        wait(250)
    elif Button.RIGHT in presses and mode < 3:
        mode += 1
        wait(250)

    # output data
    hub.display.char(modes[mode])
    print(mode_type, colour_reading)
    
    
    