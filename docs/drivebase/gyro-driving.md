# Gyro Driving

!!! learn "On this page we will learn"
    - why counting wheel turns makes the robot drift
    - how to use the gyro to turn more accurately
    - how to hold a heading so the robot drives straight
    - how to face the direction the robot started in

!!! terms "Terminology"
    - **gyroscope** – a sensor, often called a gyro, that measures how fast something is turning.
    - **drift** – small errors that add up over time so the robot ends up facing or travelling somewhere different from what we planned.

On the [Driving](driving.md) page, the robot works out how far it has turned by counting how far each wheel has turned. On this page we'll use the hub's **gyro** (part of the [IMU](../hub/imu.md)) instead, so the robot drives straighter and turns more accurately.

## Why wheel counting drifts

When the drive base turns 90°, it turns each wheel by the amount that **should** turn the robot 90°. It doesn't check what the robot actually did. Small errors creep in:

- the wheels slip a little on smooth or dusty surfaces
- one side of the robot drags more than the other
- the `axle_track` value isn't perfect

Each error is small, but they add up. After a few turns, the robot can be facing quite a different direction from the one we planned.

A **gyro** (short for **gyroscope**) is a sensor that measures how fast something is turning. The hub adds up these measurements to get its **heading**, the direction it is facing. Because the gyro measures the robot's actual turning, wheel slip doesn't fool it.

!!! warning "Keep the robot still when the program starts"
    The gyro calibrates itself while the hub sits still for a few seconds. Put the robot down, start the program, and wait a moment before pressing any buttons.

## Driving a square without the gyro

This program drives a square when we press the left button. We'll use it to test how accurate wheel counting is.

The square uses a **for loop**. `for side in range(4):` repeats the indented lines below it 4 times, once for each side of the square.

```python linenums="1"
--8<-- "examples/drivebase/gyro_driving/square_wheels/main.py"
```

!!! primm "PRIMM"
    1. **Predict** where the robot will end up. Be specific.
    2. Mark the robot's starting position and direction with masking tape, then **run** the program and press the left button. Run it three times without moving the tape. How far from the start does the robot finish each time?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 14** → starts the main loop, which repeats forever.
    - **line 15** → checks if the left button is being pressed…
    - **line 16** → …waits half a second so our hand is clear of the robot…
    - **line 17** → …then repeats the next two lines 4 times, once for each side.
    - **line 18** → drives forwards 300 mm.
    - **line 19** → turns 90° to the right.

## Driving a square with the gyro

`use_gyro(True)` tells the drive base to use the gyro for driving straight and turning. The rest of the program is the same.

```python linenums="1"
--8<-- "examples/drivebase/gyro_driving/square_gyro/main.py"
```

!!! primm "PRIMM"
    1. **Predict** whether the robot will finish closer to the start than before. Be specific.
    2. **Run** the program three times from the same tape marks. How far from the start does the robot finish each time?
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 12** → tells the drive base to use the gyro for driving straight and turning.
    - **line 15** → starts the main loop, which repeats forever.
    - **line 16** → checks if the left button is being pressed…
    - **line 17** → …waits half a second so our hand is clear of the robot…
    - **line 18** → …then repeats the next two lines 4 times, once for each side.
    - **line 19** → drives forwards 300 mm, using the gyro to keep straight.
    - **line 20** → turns 90° to the right, using the gyro to measure the turn.

## Holding a heading

With the gyro on, the drive base also corrects itself while driving. If something pushes the robot off course, it steers back to the direction it was heading.

```python linenums="1"
--8<-- "examples/drivebase/gyro_driving/hold_heading/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what will happen if we gently push the front of the robot sideways while it drives. Be specific.
    2. **Run** the program and try it. Press the centre button to stop.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 12** → tells the drive base to use the gyro for driving straight and turning.
    - **line 15** → starts the main loop, which repeats forever.
    - **line 16** → drives forwards at 150 mm per second, using the gyro to hold its heading.

## Facing the start direction

With the gyro on, the drive base's `angle()` is the gyro heading. Turning by the **negative** of that angle turns the robot back to the direction it faced when the program started.

```python linenums="1"
--8<-- "examples/drivebase/gyro_driving/face_start/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what will happen. Be specific.
    2. **Run** the program. Turn the robot by hand to face a new direction, then press the left button.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, with 56 mm wheels that are 80 mm apart.
    - **line 12** → tells the drive base to use the gyro for driving straight and turning.
    - **line 15** → starts the main loop, which repeats forever.
    - **line 16** → checks if the left button is being pressed…
    - **line 17** → …if it is, turns by the negative of the current heading, so the robot faces its starting direction again.

!!! tip "When to use the gyro"
    - Use the gyro when turns need to be accurate, such as on a competition mat or when following a planned route.
    - Wheel counting is fine for short, simple moves.
    - Gyros can drift a tiny amount over time. If full turns are consistently a little off, `turn(357)` or `turn(362)` may give a better result on your robot.

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `gyro_driving` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#gyro-driving) page.

### Exercise 1

Starter: `gyro_driving/ex1_triangle`

Can you make the robot drive an equilateral triangle with 300 mm sides, using the gyro, when the left button is pressed? Remember that the robot turns by the **outside** angle at each corner.

### Exercise 2

Starter: `gyro_driving/ex2_there_and_back`

Can you make the robot drive forwards 500 mm, turn around, drive back 500 mm and turn around again, so it finishes where it started, facing the same way?

### Exercise 3

Starter: `gyro_driving/ex3_carpet_test`

Run the square with and without the gyro on a slippery surface, such as a smooth table or a sheet of paper. Which one finishes closer to the start? Why do you think this happens?
