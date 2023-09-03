# Motors as sensors

```{topic} In this lesson you will:
- learn to read the motor speed
- learn to read the motor angle
- learn to reset the motor angle
- learn to read the torque applied to the motor
- learn to check if the motor has stalled
```

```{admonition} Pybrick Documentation
:class: important
To explore all Pybricks' features check the **[Pybricks documentaion](https://docs.pybricks.com/en/stable/index.html)**. This can also be seen in the right-hand panel of the Pybricks IDE.
```

In the **[tutorial on motors](03_motors.md)** it was explained that the motors on the robot have encoders that can read the rotation of the motor axel. This encoder also means that motors can be used as sensors to provide input to the robot.

## Motor Measurement Functions

You can get measurements from the motors using the following Pybrick functions:

- **[`speed()→ int: deg/s`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.speed)** &rarr; Gets the speed of the motor (deg/s).
- [[`angle()→ int: deg`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.angle)](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.angle) &rarr; Gets the rotation angle of the motor (deg).
- **[`load()→ int: mNm`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.load)** &rarr; Estimates the load that holds back the motor when it tries to move (mNm).
- **[`stalled()→ bool`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.stalled)** &rarr; Checks if the motor is currently stalled.

Pybricks also provides a configuration function:

- **[`reset_angle(angle=None)`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.reset_angle)** &rarr; Sets the accumulated rotation angle of the motor to a desired value.

## Motor Measurement Example

We will use the code below to see these functions work:

Now explore how this functions works.

1. **Create** a new file called `motor_inputs.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. When **running** your code you will need to interact with the robot:
    - to get a speed reading of the wheel, press the **left button**
    - to get the wheel to return to it's starting point, simultaneously press the **left button** and the **right button**.
    - to get the torque load and stall reading, press and hold the **right button** then gradually slow the left wheel with your hand until t stops.  

```{literalinclude} ./python_files/motors_input.py
:linenos:
```

```{admonition} Investigate
- **lines 3 - 7** &rarr; imports all the Pybricks command for use with your robot
- **line 10** &rarr; initialises the hub
- **line 11** &rarrl initialises the left motor (you will only use one)
- **line 13** &rarr; sets the current wheel posistion (angel) as angel `0` (the starting angle)
- **line 16** &rarr; starts infinite loop
- **line 17** &rarr; checks for pressed buttons and stores them in `pressed`
- **line 19** &rarr; checks if both the left and right buttons are currently pressed
- **line 20** &rarr; prints the current accumulated left motor angle
- **line 21** &rarr; send the left motor back to angle `0`
- **line 22** &rarr; prints the current accumulated left motor angle
- **line 24** &rarr; checks if left button is pressed
- **line 25** &rarr; starts the left motor running at 300degs/s
- **line 26** &rarr; allows a quater of a second for the motor to get up to speed
- **line 27** &rarr; reads the left motor's speed and prints it
- **line 28** &rarr; waits another half a second
- **line 29** &rarr; stops the left motor
- **line 31** &rarr; checks if the right button is pressed
- **line 32** &rarr; starts left motor running at 300deg/s
- **line 33** &rarr; checks if the left motor is stalled (prevented from moving)
- **line 34** &rarr; prints stalled
- **line 35 - 36** &rarr; if motor is not stalled then read and print the torque load that the left wheel is experiencing
- **line 38 - 39** &rarr; if no button is being pressed, stop the left motor
```

```{admonition} Modify
:class: caution
- what happens if you move **line 13** inside the main loop?
- what happens if you comment out **line 26**?
- what happens if you comment out **line 25** and then physically turn the wheel when holding the left button?
- what happens if you comment out **line 32** and then physically turn the wheel when holding the right button?
```
