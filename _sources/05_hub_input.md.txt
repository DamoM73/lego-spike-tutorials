# Hub Inputs

```{topic} In this lesson you will:
- learn how to detect the hub buttons being pushed
- learn how to detect the orienation of the hub
```

```{admonition} Pybrick Documentation
:class: important
To explore all Pybricks' features check the **[Pybricks documentaion](https://docs.pybricks.com/en/stable/index.html)**. This can also be seen in the right-hand panel of the Pybricks IDE.
```

The Prime Hub has two features that can provide input to the robot

- buttons
- inertial measurement unit (IMU)

## Buttons

The Prime Hub has four buttons, as shown below.

![Hub Buttons](assets/primehub_buttons.png)

### Buttons Functions

Pybricks has only one function to detect the pressing of a button:

- **[`buttons.pressed()→ Collection[Button]`](https://code.pybricks.com/static/docs/v2.7.0/hubs/primehub.html#pybricks.hubs.PrimeHub.buttons.pressed)** &rarr; Checks which buttons are currently pressed.
  - returns a **tuple** of buttons currently being pressed.
  - button values are:
    - `Button.LEFT`
    - `Button.RIGHT`
    - `Button.CENTER`
    - `Button.BLUETOOTH`

### Buttons Example

Now explore how this functions works.

1. **Create** a new file called `buttons.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. **Run** your code

```{literalinclude} ./python_files/hub_input_buttons.py
:linenos:
```

```{admonition} Investigate
- **lines 3 - 7** &rarr; imports all the Pybricks command for use with your robot
- **line 10** &rarr; initialised the hub
- **line 14** &rarr; creates an infinite loop
- **line 15** &rarr; checks to see what buttons are currently being pressed and saves the to `pressed`
- **line 17** &rarr; checks to see if `Button.LEFT` is one of the buttons being pressed
- **line 18** &rarr; displays a left arrow on the light matrix
- **line 19** &rarr; checks to see if `Button.RIGHT` is one of the buttons being pressed
- **line 20** &rarr; displays a right arrow on the light matrix
- **line 21** &rarr; checks to see if `Button.CENTER` is one of the buttons being pressed
- **line 22** &rarr; displays a circle on the light matrix
- **line 21** &rarr; checks to see if `Button.BLUETOOTH` is one of the buttons being pressed
- **line 22** &rarr; displays a **B** on the light matrix
- **line 26** &rarr; turns the display off.
```

```{admonition} Modify
:class: caution
- make the light matrix display a down arrow if both `Button.LEFT` and `Button.RIGHT` are being pressed
```

## IMU

The IMU is a sensor that can detect how the robot is moving. The sensor is configured around the **x-axis**, **y-axis** and **z-axis** as indicated in the image below.

![hub axes](assets/hub_axis.png)

Rotation along each axis has a specific name:

- **Roll** is rotation along the x-axis
- **Pitch** is rotation along the y-axis
- **Yaw** is rotation along the z-axis, but it is **not yet implemented**.

### IMU Orientation Functions

Pybricks offers two functions that informs the hub's orientation:

- **[`imu.up()→ Side`](https://code.pybricks.com/static/docs/v2.7.0/hubs/primehub.html#pybricks.hubs.PrimeHub.imu.up)** &rarr; Checks which side of the hub currently faces upward.
  - side values are:
    - Side.TOP
    - Side.BOTTOM
    - Side.LEFT
    - Side.RIGHT
    - Side.FRONT
    - Side.BACK.
- **[`imu.tilt()→ Tuple[int, int]`](https://code.pybricks.com/static/docs/v2.7.0/hubs/primehub.html#pybricks.hubs.PrimeHub.imu.tilt)** &rarr; Returns the pitch and roll angles in a tuple (pitch, roll)

### IMU Orientation Example

Use the code below to explore how these functions works.

1. **Create** a new file called `imu_orientation.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. **Run** your code

```{literalinclude} ./python_files/hub_input_imu_orientation.py
:linenos:
```

```{admonition} Investigate
- **lines 3 - 7** &rarr; imports all the Pybricks command for use with your robot
- **line 10** &rarr; initialised the hub
- **line 13** &rarr; creates an infinite loop
- **line 14** &rarr; gets which side of the hub is facing up and stores it in `up`
- **line 15** &rarr; gets the tuple containing the tilt values, stores the first tuple value in `pitch` and the second tuple value in `roll`
- **line 17** &rarr; prints the values of `up`, `pitch` and `roll` to the Pybricks terminal
```

```{admonition} Modify
:class: caution
- what is the highest and lowest roll value you can get?
- what is the highest and lowest pitch value you can get?
- what happens if you remove both `"\t",` from **line 17**?
```
