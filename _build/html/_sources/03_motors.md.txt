# Motors

```{topic} In this lesson you will:
- the different methods of moving the Spike Prime motors
- make a motor run contiunously
- make a motor run for a specific time
- make a motor turn a specific number of degrees
```

```{admonition} Pybrick Documentation
:class: important
To explore all Pybricks' features check the **[Pybricks documentaion](https://docs.pybricks.com/en/stable/index.html)**. This can also be seen in the right-hand panel of the Pybricks IDE.
```

Although your robot only has on type of motor, the LEGO Spike Prime kit actually has two:

- Medium Angular Motor
- Large Angular Motor

![Angular motors](assets/pupmotors.png)

Both motors are run using the same code. The only difference is the relative power.

```{admonition} DC Motor vs Encoded Motors
:class: note
The Spike Prime motors are called Angular, because you can program them to turn an exact number of degrees. This is possible because they have a built-in sensor called an encoder. Encoders record how many degrees the motor has turned.

Motors without encoders are called DC motors (direct current). The only programming options DC motors provide are turn on and turn off.
```

## Initialisation

Before you can program the motors, you need to create initialize a motor object for each motor you wish to use.

This is achieved through calling the [`Motor` class](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor). You will need to pass minimum arguments:

- port &rarr; the port the motor is plugged into. You will need to use one of Pybricks' constants (eg. `Port.A`)
- positive direction &rarr; this is the direction you want the wheel to turn when you enter a positive speed value. You will need to use one of Pybricks' constants (eg. `Direction.CLOCKWISE`)

For example, to initialize the right motor on your robot your would use:

`right_motor = Motor(Port.B, Direction.CLOCKWISE)`

## Motor Running Forever

### Motor Running Forever Functions

There are two functions that make the motors run forever:

- **[`run(speed)`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.run)** &rarr; Runs the motor at a constant speed.
- **[`dc(duty)`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.dc)** &rarr; Rotates the motor at a given duty cycle (also known as “power”).

### Motor Running Forever Examples

Time to explore how these two functions can be used.

1. **Create** a new file called `motors_run_forever.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. **Run** your code

```{literalinclude} ./python_files/motors_output_run.py
:linenos:
```

**Investigating** this code:

- **lines 3 - 7** &rarr; imports all the Pybricks command for use with your robot
- **lines 10 - 12** initialises the components of your robot
  - **line 10** &rarr; initialise the hub
  - **line 11** &rarr; initialise the left motor in port A
    - Positive direction is counter-clockwise &rarr; look at the left wheel, which direction does it need to turn for your robot to move forwards?
  - **line 12** &rarr; initialise the right motor in port B
    - Positive direction is clockwise &rarr; look at the right wheel, which direction does it need to turn for your robot to move forwards?
- **line 15** &rarr; creates a infinite loop
- **line 16** &rarr; sets `left_motor` to `1000`. This turns the motor at 1000 degrees a second
- **line 17** &rarr; sets `right_motor` to `1000`. This turns the motor at 1000 degrees a second
- **line 18** &rarr; makes the robot wait for a second before moving onto the next command
- **line 20** &rarr; sets `left_motor` to `50`. This turns the motor at 50% power
- **line 21** &rarr; sets `right_motor` to `50`. This turns the motor at 50% power

**Modify** the code:

- what happens if both motors' positive direction is the same?
- what happens if you comment out all the wait commands?
- work out how many degrees per second is produced by a motor at 50% power.

## Motor Stop

### Motor Stop Functions

Pybricks provides three functions to stop motors, each having a slightly different effect:

- **[`stop()`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.stop)** &rarr; Stops the motor and lets it spin freely.
- **[`brake()`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.brake)** &rarr; Passively brakes the motor.
- **[`hold()`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.hold)** &rarr; Stops the motor and actively holds it at its current angle.

### Motor Stop Examples

Explore how these three functions can be used.

1. **Create** a new file called `motors_stop.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. **Run** your code

```{literalinclude} ./python_files/motors_output_stop.py
:linenos:
```

**Investigate** this code by unpacking it:

- **lines 3 - 7** &rarr; imports all the Pybricks command for use with your robot
- **lines 10 - 12** initialises the components of your robot
- **line 15** &rarr; creates a infinite loop
- **line 16** &rarr; set status light to green
- **lines 18 - 20** &rarr; runs both motors at 100% power for 1 second
- **lines 22 - 23** &rarr; stop both motors using the `stop()` method
- **line 24** wait half a second
- **line 26** &rarr; set status light to orange
- **lines 28 - 30** &rarr; runs both motors at 100% power for 1 second
- **lines 32 - 33** &rarr; stop both motors using the `brake()` method
- **line 34** wait half a second
- **line 36** &rarr; set status light to orange
- **lines 38 - 40** &rarr; runs both motors at 100% power for 1 second
- **lines 42 - 43** &rarr; stop both motors using the `hold()` method
- **line 44** wait half a second

```{admonition} Inidcating current robot logic
:class: note
One of the difficult aspects of programming robots is working out what part of the code the robot is currently running. This presents a signifiacnt problem when debugging problematic code.

One method to reduce this problem, is using outputs to indicate which part of the code is being run.

For example, the code above changes the colour of the status light to indicate which stopping method is used:

- green &rarr; `stop()`
- orange &rarr; `brake()`
- violet &rarr; `hold()`
```

Try **modifying** the code:

- what happens when you only stop one motor? Is it different for the different stopping functions?
- what happens when you comment out all the `wait` functions?

## Motor Fixed Amount

### Motor Fixed Amount Functions

Pybricks has four functions that can run a motor for a designated amount:

- **[`run_time(speed, time, then=Stop.HOLD, wait=True)`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.run_time)** &rarr; Runs the motor at a constant speed for a given amount of time.
- **[`run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.run_angle)** &rarr; Runs the motor at a constant speed by a given angle.
- **[`run_target(speed, target_angle, then=Stop.HOLD, wait=True)`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.run_target)** &rarr; Runs the motor at a constant speed towards a given target angle.
- **[`track_target(target_angle)`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/motor.html#pybricks.pupdevices.Motor.track_target)** &rarr; Tracks a target angle. This is similar to `run_target()`, but the usual smooth acceleration is skipped: it will move to the target angle as fast as possible.

```{admonition} Motors waiting
:class: note
You will notice that `run_time()`, `run_angle()` and `run_target()` have a parameter called `wait`. By default this is set to `True` which means the program will wait for the motor to finish it fixed movement before moving onto the next line of code.

If you want both motors to run simultaneously, you need to set `wait` to `False`.
```

### Motor Fixed Amount Example

Time to see these four functions in action.

1. **Create** a new file called `motors_run_fixed.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. **Run** your code

```{literalinclude} ./python_files/motors_output_fixed.py
:linenos:
```

**Investigating** this code:

- **lines 3 - 7** &rarr; imports all the Pybricks command for use with your robot
- **lines 10 - 12** initialises the components of your robot
- **line 15** &rarr; creates a infinite loop
- **line 16** &rarr; set status light to brown
- **line 18** &rarr; runs the left motor at 1000 d/s for 1 second, then coasts to a stop
- **line 19** &rarr; runs the right motor at 1000 d/s for 1 second, then coasts to a stop
- **line 21** &rarr; set status light to violet
- **line 23** &rarr; runs the left motor at 1000 d/s for 180&deg;
- **line 24** &rarr; runs the right motor at 1000 d/s for 180&deg;
- **line 26** &rarr; set status light to cyan
- **line 28** &rarr; sets the left motor's current position as 0&deg;
- **line 29** &rarr; sets the left motor's current position as 0&deg;
- **line 30** &rarr; runs the left motor at 1000 d/s to position 180&deg;
- **line 31** &rarr; runs the right motor at 1000 d/s to position 180&deg;
- **line 33** &rarr; set status light to gray
- **line 35** &rarr; sets the left motor's current position as 0&deg;
- **line 36** &rarr; sets the left motor's current position as 0&deg;
- **line 37** &rarr; rapidly changes the left motor's position to 180&deg;
- **line 38** &rarr; rapidly changes the right motor's position to 180&deg;
- **line 40** &rarr; waits 2 seconds

```{admonition} **run_angle()** vs **run_target()** vs **track_target()**
:class: note
If you want to turn a your motor a specific number of degree you are better off using `run_angle()`.

`run_target()` & `track_target` are better to use if you want to move a motor to a specific degree position between 0&deg; and 359&deg;.

Use `run_target()` if you want to control which direction the motor spins to get to the specified degree position.

Use `track_target()` if you want the motor to take the quickest direction to the specified degree position.
```

**Modify** the code:

- what happens when you add `False` as the last argument in **line 18**?
- what happens if you change `Stop.COAST` to `Stop.HOLD` in **line 18** and **line 19**?
- what happens if your comment out the `reset_angle()` lines?
