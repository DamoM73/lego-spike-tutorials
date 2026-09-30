# Driving

A **drive base** joins the two wheel motors together so we can control the whole robot instead of each motor. We tell the robot to drive 300 mm or turn 90°, and Pybricks works out what each motor needs to do.

Possible uses:

- driving along a set path
- turning to face a new direction
- driving in curves around obstacles
- moving at different speeds for different jobs

## Connect it

- See [Setup](../start/setup.md#create-and-run-a-program) for how to create and run each example.
- The drive base uses the left motor in **Port E** and the right motor in **Port F**.
- **Distances** are in millimetres (mm) and **speeds** are in millimetres per second (mm/s).
- **Angles** are in degrees. A drive base angle is how far the **robot** turns. 90° is a quarter turn and 360° is a full circle.
- **Positive** distances and speeds drive **forwards**. Negative drives backwards.
- **Positive** angles turn **right** (clockwise). Negative turns left.

!!! tip "Motor angles and drive base angles"
    On the [Motor](../motors/motor.md) page, an angle is how far one **wheel** turns. 180° turns the wheel half a rotation.

    On a drive base, an angle is how far the **whole robot** turns. 180° makes the robot face the opposite way.

!!! warning "Give the robot space"
    From now on the robot drives across the floor or desk. Clear a space of about 1 metre, and keep it away from desk edges. Press the centre button to stop the program.

## Set it up

To create a drive base we first create the two motors, as on the [Motor](../motors/motor.md#set-it-up) page. Then we create a `DriveBase` with four values:

- `left_motor` → the motor on the left wheel
- `right_motor` → the motor on the right wheel
- `wheel_diameter` → the width of a wheel in millimetres. Our robot's wheels are `56` mm.
- `axle_track` → the distance between where the two wheels touch the ground, in millimetres. On our robot it is `80` mm.

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

The `wheel_diameter` and `axle_track` values are measured with a ruler, so they are only close. The [Calibration](calibration.md) page shows how to make them accurate.

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `drive(speed, turn_rate)` | `speed`: mm/s; `turn_rate`: deg/s | none | Starts driving and keeps going |
| `stop()` | none | none | Stops the robot and lets the wheels spin freely |
| `straight(distance)` | `distance`: mm | none | Drives straight for a set distance, then stops |
| `turn(angle)` | `angle`: degrees | none | Turns on the spot by a set angle, then stops |
| `arc(radius, angle=None, distance=None)` | `radius`: mm; `angle`: degrees or `distance`: mm | none | Drives part of a circle, then stops |
| `settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)` | speeds in mm/s and deg/s; accelerations in mm/s² and deg/s² | tuple when no values are given | Sets the speeds used by `straight()`, `turn()` and `arc()` |

### `drive()`

Starts the robot driving at a set speed and **turn rate**, and keeps it going until we tell it to do something else. The turn rate is how fast the robot turns, in degrees per second. A turn rate of `0` drives straight.

```python linenums="1"
--8<-- "examples/drivebase/driving/drive/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program. Press the centre button to stop it.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 14** → starts the main loop, which repeats forever.
    - **line 15** → drives the robot forwards at 200 mm per second without turning.

### `stop()`

Stops the robot and lets the wheels spin freely.

```python linenums="1"
--8<-- "examples/drivebase/driving/stop/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 14** → starts the main loop, which repeats forever.
    - **line 15** → drives the robot forwards at 200 mm per second.
    - **line 16** → waits 1 second while the robot drives.
    - **line 17** → stops the robot.
    - **line 18** → waits 1 second before the loop starts again.

### `straight()`

Drives straight for a set distance in millimetres, then stops. A negative distance drives backwards. The program waits until the robot has finished before running the next line.

```python linenums="1"
--8<-- "examples/drivebase/driving/straight/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 14** → starts the main loop, which repeats forever.
    - **line 15** → drives forwards 300 mm, then stops.
    - **line 16** → waits 1 second.
    - **line 17** → drives backwards 300 mm, then stops.
    - **line 18** → waits 1 second before the loop starts again.

### `turn()`

Turns the robot on the spot by a set angle, then stops. Positive angles turn right and negative angles turn left.

```python linenums="1"
--8<-- "examples/drivebase/driving/turn/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 14** → starts the main loop, which repeats forever.
    - **line 15** → turns the robot 90° to the right, then stops.
    - **line 16** → waits 1 second before the loop starts again.

### `arc()`

Drives along part of a circle, then stops. The **radius** is the distance from the centre of the circle to the robot. A positive radius curves to the right and a negative radius curves to the left. We choose how far to go with either `angle` (how far around the circle) or `distance` (how far along it).

```python linenums="1"
--8<-- "examples/drivebase/driving/arc/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 14** → starts the main loop, which repeats forever.
    - **line 15** → drives halfway around a circle with a radius of 150 mm, curving to the right.
    - **line 16** → waits 1 second before the loop starts again.

### `settings()`

Sets how fast the robot drives and turns in `straight()`, `turn()` and `arc()`. We only need to give the values we want to change, such as `straight_speed=400`. With nothing in the brackets, `settings()` returns the current values as a tuple, which we can print.

```python linenums="1"
--8<-- "examples/drivebase/driving/settings/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program. Compare it with the `straight()` example.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 12** → sets the speed for driving straight to 400 mm per second.
    - **line 15** → starts the main loop, which repeats forever.
    - **line 16** → drives forwards 300 mm at the new speed.
    - **line 17** → drives backwards 300 mm at the new speed.

!!! tip "Using the motors after creating a drive base"
    We can still use `left_motor` and `right_motor` on their own after creating a drive base. If we do, the drive base stops whatever it was doing.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [Pybricks — Drive base](https://docs.pybricks.com/en/stable/robotics.html)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `driving` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#driving) page.

### Exercise 1

Starter: `driving/ex1_square`

Can you make the robot drive in a square with sides of 200 mm?

### Exercise 2

Starter: `driving/ex2_figure_eight`

Can you make the robot drive in a figure eight? `arc()` with a positive and a negative radius may help.

### Exercise 3

Starter: `driving/ex3_turn_rate`

Change the turn rate in the `drive()` example to `90`, then `-90`, then `360`. What happens each time? Why do you think this happens?

### Exercise 4

Starter: `driving/ex4_slow_fast`

Can you make the robot drive forwards 300 mm slowly, then drive back 300 mm quickly? Use `settings()` to change the speed.
