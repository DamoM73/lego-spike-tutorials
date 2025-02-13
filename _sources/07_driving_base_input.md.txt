# Drive Base as Sensors

```{topic} In this lesson you will:
- learn to read how far the dirve base has traveled
- learn to read how much the drive base has turned
- learn to read the measurement of the drive base travelling on a curve
- learn to reset the drive base values
```

```{admonition} Pybrick Documentation
:class: important
To explore all Pybricks' features check the **[Pybricks documentaion](https://docs.pybricks.com/en/stable/index.html)**. This can also be seen in the right-hand panel of the Pybricks IDE.
```

Since the drive base is made up of motors, the encoders can also be used to measure what the robot has done.

## Drive Base Measurement Functions

There are three functions that can extract measurements from the drive base:

- **[`distance()→ int: mm`](https://docs.pybricks.com/en/stable/robotics.html#pybricks.robotics.DriveBase.distance)** &rarr; Gets the estimated driven distance (mm).
- **[`angle()→ int: deg`](https://docs.pybricks.com/en/stable/robotics.html#pybricks.robotics.DriveBase.angle)** &rarr; Gets the estimated rotation angle (deg) of the drive base.
- [`state()→ Tuple[int, int, int, int]`](https://docs.pybricks.com/en/stable/robotics.html#pybricks.robotics.DriveBase.state) &rarr; Gets the state of the robot. The return tuple is `(distance, speed, angle, turn_rate)`

There is also one configuration function:

- **[`reset()`](https://docs.pybricks.com/en/stable/robotics.html#pybricks.robotics.DriveBase.reset)** &rarr; Resets the estimated driven distance and angle to `0`.

## Drive Base Measurement Example

Now use the code below to explore these functions:

1. **Create** a new file called `drive_base_inputs.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. When **running** your code you will need to interact with the robot:
    - to get an arc movement reading, press the **left button**
    - to get a straight line distance reading, press the **right button**
    - to get a turn degrees reading, press the **Bluetooth button**

```{literalinclude} ./python_files/drive_base_input.py
:linenos:
```

```{admonition} Investigate
- **lines 3 - 7** &rarr; imports all the Pybricks command for use with your robot
- **line 10** &rarr; initialises the hub
- **lines 12 - 14** &rarr; initialises the drive base
- **line 16** &rarr; sets the robot's distance and angle counters to `0`
- **line 19** &rarr; create the main loop
- **line 20** &rarr; checks for pressed buttons and stores them in `pressed`
- **line 22** &rarr; checks if the left button was pressed
- **line 23** &rarr; get the robot's state tuple and stores the values in `distance`, `speed`, `angle`, and `rate_of_turn`
- **line 24** &rarr; prints the robot state values stored in `distance`, `speed`, `angle`, and `rate_of_turn`
- **line 25** &rarr; drives the robot in an arc
- **line 26** &rarr; get the robot's state tuple and stores the values in `distance`, `speed`, `angle`, and `rate_of_turn`
- **line 27** &rarr; prints the robot state values stored in `distance`, `speed`, `angle`, and `rate_of_turn`
- **line 29** &rarr; checks if the right button is pressed
- **line 30** &rarr; reads the current robot distance count and stores it in `distance`
- **line 31** &rarr; prints th current robot distance count
- **line 32** &rarr; moves the robot in a straight line
- **line 33** &rarr; reads the current robot distance count and stores it in `distance`
- **line 34** &rarr; prints th current robot distance count
- **line 36** &rarr; checks if the Bluetooth button is pressed
- **line 37** &rarr; reads the current robot angle count and stores it in `angle`
- **line 38** &rarr; prints th current robot angle count
- **line 39** &rarr; turns the robot
- **line 40** &rarr; reads the current robot angle count and stores it in `angle`
- **line 41** &rarr; prints th current robot angle count
- **line 43 - 44** &rarr; if not button is pressed stop the drive base
```

```{admonition} Modify
:class: caution
- what happens if you move line 16 to inside the main loop?
- can you use `my_robot.state()` to measure a straight move by the robot?
```
