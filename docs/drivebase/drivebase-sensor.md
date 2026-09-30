# Drive Base as a Sensor

The drive base is made of two motors, and each motor has an **encoder** that counts how far it has turned (see [Motor as a Sensor](../motors/motor-sensor.md)). Pybricks combines the two encoder readings to work out how far the whole robot has driven and turned.

Possible uses:

- measuring how far the robot has travelled
- stopping after a set distance while doing something else
- checking how far the robot has turned
- using the robot as a measuring tool

## Connect it

- See [Setup](../start/setup.md#create-and-run-a-program) for how to create and run each example.
- We create the drive base in the same way as on the [Driving](driving.md#set-it-up) page.
- For most examples, push the robot along the desk by hand and watch the terminal.
- **Distance** is in millimetres (mm), **speed** in mm/s, **angle** in degrees and **turn rate** in degrees per second.

## Set it up

```python linenums="1"
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)
my_robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `distance()` | none | int (mm) | How far the robot has driven |
| `angle()` | none | float (degrees) | How far the robot has turned |
| `state()` | none | tuple (distance, speed, angle, turn rate) | All four measurements at once |
| `reset()` | none | none | Sets the distance and angle back to `0` |

### `distance()`

Returns how far the robot has driven in millimetres since the program started. Driving backwards makes the distance smaller.

```python linenums="1"
--8<-- "examples/drivebase/drivebase_sensor/distance/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program. Push the robot forwards and backwards along the desk.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 14** → starts the main loop, which repeats forever.
    - **line 15** → prints how far the robot has driven in millimetres.
    - **line 16** → waits 200 milliseconds so the terminal isn't flooded with readings.

### `angle()`

Returns how far the robot has turned in degrees since the program started. Turning right makes the angle bigger and turning left makes it smaller.

```python linenums="1"
--8<-- "examples/drivebase/drivebase_sensor/angle/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program. Turn the robot by hand, left and right, with its wheels on the desk.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 14** → starts the main loop, which repeats forever.
    - **line 15** → prints how far the robot has turned in degrees.
    - **line 16** → waits 200 milliseconds before the next reading.

### `state()`

Returns four measurements at once as a tuple: distance, speed, angle and turn rate. We can store each value in its own variable by writing four names before the `=`.

```python linenums="1"
--8<-- "examples/drivebase/drivebase_sensor/state/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program. Push and turn the robot by hand, fast and slow.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 14** → starts the main loop, which repeats forever.
    - **line 15** → gets the state tuple and stores its four values in `distance`, `speed`, `angle` and `turn_rate`.
    - **line 16** → prints the distance and speed.
    - **line 17** → prints the angle and turn rate.
    - **line 18** → waits half a second before the next reading.

### `reset()`

Sets the robot's distance and angle back to `0`, so we can measure from where it is now.

```python linenums="1"
--8<-- "examples/drivebase/drivebase_sensor/reset/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program. Push the robot forwards, then press the left button.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 14** → starts the main loop, which repeats forever.
    - **line 15** → checks if the left button is being pressed…
    - **line 16** → …if it is, sets the distance and angle back to `0`.
    - **line 17** → prints how far the robot has driven in millimetres.
    - **line 18** → waits 200 milliseconds before the next reading.

!!! tip "Wheels slip"
    The drive base measures how far the **wheels** have turned, not how far the robot has actually moved. If the wheels slip or the robot is picked up and put down somewhere else, the measurements will be wrong. The [Gyro Driving](gyro-driving.md) page shows how the hub's IMU makes turning measurements more accurate.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [Pybricks — Drive base](https://docs.pybricks.com/en/stable/robotics.html)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `drivebase_sensor` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#drive-base-as-a-sensor) page.

### Exercise 1

Starter: `drivebase_sensor/ex1_tape_measure`

Can you turn the robot into a tape measure? It should:

- show how far the robot has been pushed, in centimetres, on the display
- reset the measurement to `0` when the left button is pressed

### Exercise 2

Starter: `drivebase_sensor/ex2_stop_at_500`

Can you make the robot drive forwards using `drive()` and stop when it has travelled 500 mm? Don't use `straight()`.

### Exercise 3

Starter: `drivebase_sensor/ex3_protractor`

Can you make the status light turn green once the robot has been turned 90° or more to the right by hand, and red before that?
