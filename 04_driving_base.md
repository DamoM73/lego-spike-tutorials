# Drive Base

```{topic} In this lesson you will:
- learn what a drive base is and how it can be to command your robot
- set up a drive base on your robot
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

- Motor angels indicate the amount of rotation of the axel of a motor, eg. 180&deg; will turn a wheel half a rotation.
- Drivebase angels indicate how far from straight the robot will turn, eg. 180&deg; will make the robot face backwards.
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

## Driving forever



## Driving fixed



## Calibration

