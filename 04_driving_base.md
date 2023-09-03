# Drive Base

```{topic} In this lesson you will:
- learn what a drive base is and how it can be to command your robot
- set up a drive base on your robot
- make the robot drive forever
- make the robot drive for a fixed distance
- make the robot turn a set nubmer of degrees
- make the robot drive in a set arc
- learn to calibrate the robot so the distance measurements are accurate
```

```{admonition} Pybrick Documentation
:class: important
To explore all Pybricks' features check the **[Pybricks documentaion](https://docs.pybricks.com/en/stable/index.html)**. This can also be seen in the right-hand panel of the Pybricks IDE.
```

Pybricks uses `Drivebase` to combine two motors so you can issue command to them as a single unit. You will then be able to issue commands to your robot, rather than individual motors, getting it to move a specific distance, or turn a specific angle.

- Positive distances, radii, or drive speeds mean driving forward. Negative means backward.
- Positive angles and turn rates mean turning right. Negative means left. So when viewed from the top, positive means clockwise and negative means counter-clockwise. 

```{admonition} Motor angels vs Drivebase angels
:class: important
It is important to note the difference between Motor angels and Drivebase angels.

- Motor angles indicate the amount of rotation of the axel of a motor, eg. 180&deg; will turn a wheel half a rotation.
- Drivebase angles indicate how far from straight the robot will turn, eg. 180&deg; will make the robot face backwards.
```

## Setup

To start using the drive base you first need to create a `left_motor` and a `right_motor` in the same way you did in the **[Motors tutorial](03_motors.md#initialisation)**.

You then need to create a drive base by calling 
**[`DriveBase(left_motor, right_motor, wheel_diameter, axle_track)`](https://code.pybricks.com/static/docs/v2.7.0/robotics.html#pybricks.robotics.DriveBase)**. 

- **`left_motor** &rarr; the name you gave the left motor
- **right_motor** &rarr; the name you gave the right motor
- **wheel_diameter** &rarr; the diameter of the robot's wheel in millimetres (for your robot use `56`)
- **axle_track** &rarr; the distance between the wheels in millimetres (for your robot use `80`)

Go ahead and create your first drive base:

1. **Create** a new file called `drive_base.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. **Run** your code

```{literalinclude} ./python_files/drive_base_output.py
:linenos:
```

Did you predict that your robot would do nothing? Actually it didn't do nothing, what it *did* do was initialise both motors and combined them to make a drive base called `my_robot`. The reason your robot did nothing was that you didn't give it any commands. Let's fix that by learning some commands you can use. 

```{admonition} Using the DriveBase motors individually
:class: note
After creating a DriveBase object, you can still use its two motors individually. If you start one motor, the other motor will automatically stop. Likewise, if a motor is already running and you make the drive base move, the original maneuver is cancelled and the drive base will take over.
```

## Driving Forever

### Driving Forever Functions

Pybricks has two function used to implement continuous driving of the drive base:

- **[`drive(speed, turn_rate)`](https://code.pybricks.com/static/docs/v2.7.0/robotics.html#pybricks.robotics.DriveBase.drive)** &rarr; Starts driving at the specified speed and turn rate.
- **[`stop()`](https://code.pybricks.com/static/docs/v2.7.0/robotics.html#pybricks.robotics.DriveBase.stop)** &rarr; Stops the robot by letting the motors spin freely.

### Driving Forever Examples

Use the code below to see these functions in use:

1. **Create** a new file called `drive_base_forever.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. **Run** your code

```{literalinclude} ./python_files/drive_base_output_forever.py
:linenos:
```

**Investigating** this code:

- **lines 3 - 7** &rarr; imports all the Pybricks command for use with your robot
- **line 10** &rarr; initialised the hub
- **lines 13 - 15** &rarr; initialises the drive base
- **line 18** &rarr; creates a infinite loop
- **line 19** &rarr; sets status light to white
- **line 20** &rarr; sets drive base to drive straight
- **line 21** &rarr;  waits half a second
- **line 23** &rarr; sets status light to red
- **line 24** &rarr; sets drive base to drive a left curve
- **line 25** &rarr;  waits half a second
- **line 27** &rarr; stops the drive base
- **line 28** &rarr; waits a second
- **line 30** &rarr; sets status light to white
- **line 31** &rarr; sets drive base to drive straight
- **line 32** &rarr;  waits half a second
- **line 34** &rarr; sets status light to green
- **line 35** &rarr; sets drive base to drive a right curve
- **line 36** &rarr;  waits half a second
- **line 38** &rarr; stops the drive base
- **line 39** &rarr; waits a second
 

Now **Modify the code**:

- what is lowest turning value to provide the sharpest turn?
- can you make the robot drive backwards?
- what happens if you comment out all the `wait()` commands?

## Driving Fixed

### Driving Fixed Functions

There are three different ways that you can program you drive base to drive a fixed amount:

- **[`straight(distance, then=Stop.HOLD, wait=True)`](https://code.pybricks.com/static/docs/v2.7.0/robotics.html#pybricks.robotics.DriveBase.straight)** &rarr; Drives straight for a given distance (mm) and then stops.
- **[`turn(angle, then=Stop.HOLD, wait=True)`](https://code.pybricks.com/static/docs/v2.7.0/robotics.html#pybricks.robotics.DriveBase.turn)** &rarr; Turns in place by a given angle and then stops.
- [`curve(radius, angle, then=Stop.HOLD, wait=True)`](https://code.pybricks.com/static/docs/v2.7.0/robotics.html#pybricks.robotics.DriveBase.curve) &rarr; Drives an arc along a circle of a given radius (mm), by a given angle.

There is also a function to change the setting used by the three functions above:

- **[`settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)`](https://code.pybricks.com/static/docs/v2.7.0/robotics.html#pybricks.robotics.DriveBase.settings)** &rarr; Configures the speed and acceleration used by `straight()`, `turn()`, and `curve()`
- **[`settings()`](https://code.pybricks.com/static/docs/v2.7.0/robotics.html#pybricks.robotics.DriveBase.settings)** &rarr; If you give no arguments, this returns the current values as a tuple.

### Driving Fixed Example

Use the code below to see these functions in use:

1. **Create** a new file called `drive_base_fixed.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. **Run** your code

```{literalinclude} ./python_files/drive_base_output_fixed.py
:linenos:
```

- **lines 3 - 7** &rarr; imports all the Pybricks command for use with your robot
- **line 10** &rarr; initialised the hub
- **lines 13 - 15** &rarr; initialises the drive base
- **line 18** &rarr; creates a infinite loop
- **line 19** &rarr; sets status light to yellow
- **line 20** &rarr; configures the drive base for:
  - straight speed `200` mm/s
  - straight_acceleration `200` mm/s<sup>2</sup>
  - turn rate `200` deg/s
  - turn acceleration `200` deg/s<sup>2</sup>
- **line 21** &rarr; prints current drive base configuration
- **line 22** &rarr; drives the robot strait for 200mm
- **line 23** &rarr; turns the robot in place for 90&deg;
- **line 24** &rarr; drives the robot in a 180&deg; arc with a radius of 100mm
- **line 19** &rarr; sets status light to magenta
- **line 20** &rarr; configures the drive base for:
  - straight speed `500` mm/s
  - straight_acceleration `500` mm/s<sup>2</sup>
  - turn rate `500` deg/s
  - turn acceleration `500` deg/s<sup>2</sup>
- **line 21** &rarr; prints current drive base configuration
- **line 22** &rarr; drives the robot strait for 200mm
- **line 23** &rarr; turns the robot in place for 90&deg;
- **line 24** &rarr; drives the robot in a 180&deg; arc with a radius of 100mm

Explore the code by modifying it:

- what is the fastest effective values for straight speed, straight_acceleration, turn rate and turn acceleration?
- what is the slowest effective values for straight speed, straight_acceleration, turn rate and turn acceleration?
- what happens when you use negative values for straight speed, straight_acceleration, turn rate and turn acceleration?

## Calibration

The values you entered for **wheel_diameter** and the **axle_track** were estimates measured with a ruler. 

In practice, most wheels compress slightly under the weight of the robot. To verify, make your robot drive 1000 mm using `my_robot.straight(1000)` and measure how far it really travelled. 

Change the `DriveBase` values as follows:

- robot doesn't drive far enough &rarr; decrease the `wheel_diameter` value slightly
- robot drives too far &rarr; increase the `wheel_diameter` value slightly.

Motor shafts and axles bend slightly under the load of the robot, causing the ground contact point of the wheels to be closer to the midpoint of your robot. To verify, make your robot turn 720 degrees using my_robot.turn(720) and check that it is back in the same place.

Change the `DriveBase` values as follows:

- robot doesn't turns far enough &rarr; increase the `axle_track` value slightly.
- robot turns too far &rarr; decrease the `axle_track` value slightly.

When making these adjustments, always adjust the wheel_diameter first, as done above. Be sure to test both turning and driving straight after you are done.
