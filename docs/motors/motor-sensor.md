# Motor as a Sensor

Each motor has a built-in **encoder** that counts how far it has turned (see [Motor](motor.md)). This means a motor can also be a sensor: it can tell us its angle and speed, how hard it is working, and whether something has stopped it.

Possible uses:

- using a wheel as a dial or knob
- measuring how far a wheel has turned
- detecting when the robot has driven into a wall
- knowing when an arm has reached the end of its movement

## Connect it

- See [Setup](../start/setup.md#create-and-run-a-program) for how to create and run each example.
- The left motor is in **Port E** and the right motor is in **Port F**.
- The examples use the left motor. Lift the robot off the desk, or turn the wheel by hand when the example asks us to.
- **Angle** is in degrees, **speed** is in degrees per second (deg/s) and **load** is in millinewton metres (mNm), a unit of turning force.

## Set it up

We create the motor in the same way as on the [Motor](motor.md#set-it-up) page:

```python linenums="1"
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `angle()` | none | int (degrees) | How far the motor has turned |
| `reset_angle(angle)` | `angle`: degrees | none | Sets the motor's angle to a new value |
| `speed()` | none | int (deg/s) | How fast the motor is turning |
| `load()` | none | int (mNm) | How hard something is pushing against the motor |
| `stalled()` | none | Boolean | `True` if the motor is trying to move but can't |

### `angle()`

Returns how many degrees the motor has turned. The angle keeps counting past 360°, so two full turns forwards gives `720`, and turning backwards makes it smaller.

```python linenums="1"
--8<-- "examples/motors/motor_sensor/angle/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program. Turn the left wheel slowly by hand in both directions.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 12** → starts the main loop, which repeats forever.
    - **line 13** → prints the motor's angle in degrees.
    - **line 14** → waits 200 milliseconds so the terminal isn't flooded with readings.

### `reset_angle()`

Sets the motor's angle to a new value, usually `0`. This lets us measure from where the motor is now.

```python linenums="1"
--8<-- "examples/motors/motor_sensor/reset_angle/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program. Turn the wheel by hand, then press the left button.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 12** → starts the main loop, which repeats forever.
    - **line 13** → checks if the left button is being pressed…
    - **line 14** → …if it is, sets the motor's angle to `0`.
    - **line 15** → prints the motor's angle in degrees.
    - **line 16** → waits 200 milliseconds before the next reading.

### `speed()`

Returns how fast the motor is turning in degrees per second. It is negative when the motor turns backwards.

```python linenums="1"
--8<-- "examples/motors/motor_sensor/speed/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program. Spin the left wheel by hand, fast and slow, in both directions.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 12** → starts the main loop, which repeats forever.
    - **line 13** → prints the motor's speed in degrees per second.
    - **line 14** → waits 200 milliseconds before the next reading.

### `load()`

Estimates how hard something is pushing against the motor while it runs. The harder we hold the wheel back, the bigger the load.

```python linenums="1"
--8<-- "examples/motors/motor_sensor/load/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program. Gently slow the wheel with your fingers, then let go.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 12** → starts the main loop, which repeats forever.
    - **line 13** → runs the left motor at 300 degrees per second.
    - **line 14** → prints the load on the motor in millinewton metres.
    - **line 15** → waits 200 milliseconds before the next reading.

### `stalled()`

Returns `True` if the motor is trying to move but can't, even at full power. This is called **stalling**.

```python linenums="1"
--8<-- "examples/motors/motor_sensor/stalled/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program. Hold the wheel so it can't turn, then let go.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 12** → starts the main loop, which repeats forever.
    - **line 13** → runs the left motor at 300 degrees per second.
    - **line 14** → checks if the motor has stalled…
    - **line 15** → …if it has, turns the status light red.
    - **line 16** → if it hasn't…
    - **line 17** → …turns the status light green.

!!! warning "Don't stall a motor for long"
    A stalled motor is still using power and heats up. Let go of the wheel after a few seconds.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [Pybricks — Motors with rotation sensors](https://docs.pybricks.com/en/stable/pupdevices/motor.html)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `motor_sensor` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#motor-as-a-sensor) page.

### Exercise 1

Starter: `motor_sensor/ex1_dial`

Can you turn the left wheel into a dial? The display should show how many full turns we have made by hand. `int()` may help.

### Exercise 2

Starter: `motor_sensor/ex2_mirror`

Can you make the right wheel copy the left wheel? When we turn the left wheel by hand, the right wheel should turn to the same angle.

### Exercise 3

Starter: `motor_sensor/ex3_bump_reverse`

Can you make the left motor run forwards until it is stalled, then change direction? Each time we stop the wheel with our hand, it should reverse.
