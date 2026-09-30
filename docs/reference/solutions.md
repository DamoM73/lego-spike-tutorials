# Exercise Solutions

These are **a** solution to each exercise. There are many ways to solve a programming problem. If your program produces the required result, it solves the problem.

## Program Structure

### Exercise 1

The hub beeps every time the loop repeats, instead of once at the start. Code in the setup section only runs once. Code inside the main loop runs every time the loop goes around, which is once every second in this program.

### Exercise 2

```python linenums="1"
--8<-- "solutions/start/program_structure/ex2_right_button.py"
```

### Exercise 3

```python linenums="1"
--8<-- "solutions/start/program_structure/ex3_traffic_light.py"
```

## Status Light

### Exercise 1

```python linenums="1"
--8<-- "solutions/hub/status_light/ex1_school_colours.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/hub/status_light/ex2_sos.py"
```

### Exercise 3

```python linenums="1"
--8<-- "solutions/hub/status_light/ex3_police_light.py"
```

## Light Matrix

### Exercise 1

```python linenums="1"
--8<-- "solutions/hub/light_matrix/ex1_my_face.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/hub/light_matrix/ex2_countdown.py"
```

### Exercise 3

```python linenums="1"
--8<-- "solutions/hub/light_matrix/ex3_name_and_heart.py"
```

### Exercise 4

After 99, the display shows `>` instead of the number. The display only has 5×5 pixels, which is only enough room for two digits, so `number()` can only show numbers from −99 to 99. The program keeps counting, but the display can't show the bigger numbers.

## Speaker

### Exercise 1

```python linenums="1"
--8<-- "solutions/hub/speaker/ex1_siren.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/hub/speaker/ex2_new_tune.py"
```

### Exercise 3

The answer is different for everyone. Most people can hear from about 20 Hz up to somewhere between 15,000 and 20,000 Hz, and the highest sounds get harder to hear as we get older. The hub's speaker is very small, so it can't play very low sounds well, and they may sound quiet or buzzy. Outside our hearing range the speaker may still be vibrating, but our ears can't detect it.

## Buttons

### Exercise 1

```python linenums="1"
--8<-- "solutions/hub/buttons/ex1_more_buttons.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/hub/buttons/ex2_counter.py"
```

### Exercise 3

```python linenums="1"
--8<-- "solutions/hub/buttons/ex3_both_buttons.py"
```

## IMU

### Exercise 1

```python linenums="1"
--8<-- "solutions/hub/imu/ex1_face_up.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/hub/imu/ex2_spirit_level.py"
```

### Exercise 3

```python linenums="1"
--8<-- "solutions/hub/imu/ex3_turn_counter.py"
```

## Motor

### Exercise 1

```python linenums="1"
--8<-- "solutions/motors/motor/ex1_stopping_test.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/motors/motor/ex2_both_wheels.py"
```

### Exercise 3

The wheels turn one after the other. `run_angle()` waits until the motor has finished before the program moves to the next line, so the right wheel only starts once the left wheel has stopped. Adding `wait=False` to the left motor's `run_angle()` lets the program move straight on, so both wheels turn together.

### Exercise 4

```python linenums="1"
--8<-- "solutions/motors/motor/ex4_clock_hand.py"
```

## Motor as a Sensor

### Exercise 1

```python linenums="1"
--8<-- "solutions/motors/motor_sensor/ex1_dial.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/motors/motor_sensor/ex2_mirror.py"
```

### Exercise 3

```python linenums="1"
--8<-- "solutions/motors/motor_sensor/ex3_bump_reverse.py"
```

## Driving

### Exercise 1

```python linenums="1"
--8<-- "solutions/drivebase/driving/ex1_square.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/drivebase/driving/ex2_figure_eight.py"
```

### Exercise 3

With a turn rate of `90` the robot drives in a circle to the right, and with `-90` it drives in a circle to the left. With `360` it turns much faster, so the circle is much smaller. The turn rate is how many degrees the robot turns each second while it drives forwards, so a bigger turn rate means a tighter circle, and the sign chooses right or left.

### Exercise 4

```python linenums="1"
--8<-- "solutions/drivebase/driving/ex4_slow_fast.py"
```

## Drive Base as a Sensor

### Exercise 1

```python linenums="1"
--8<-- "solutions/drivebase/drivebase_sensor/ex1_tape_measure.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/drivebase/drivebase_sensor/ex2_stop_at_500.py"
```

### Exercise 3

```python linenums="1"
--8<-- "solutions/drivebase/drivebase_sensor/ex3_protractor.py"
```

## Gyro Driving

### Exercise 1

```python linenums="1"
--8<-- "solutions/drivebase/gyro_driving/ex1_triangle.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/drivebase/gyro_driving/ex2_there_and_back.py"
```

### Exercise 3

The square with the gyro usually finishes much closer to the start. On a slippery surface the wheels slip during turns, so the wheels turn the right amount but the robot doesn't. Wheel counting can't detect this, so each turn is a bit short or long and the errors add up. The gyro measures how far the robot actually turned, so it keeps turning until the robot really has turned 90°.

## Force Sensor

### Exercise 1

```python linenums="1"
--8<-- "solutions/sensors/force/ex1_force_meter.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/sensors/force/ex2_start_button.py"
```

### Exercise 3

With a threshold of `0`, the light is on all the time, because the force is always at least 0 N, even when nothing is touching the button. With `15`, the light never turns on, because the sensor can only measure up to about 10 N, so the force can never reach 15 N. The threshold needs to be between these values for `pressed()` to be useful.

## Colour Sensor

### Exercise 1

```python linenums="1"
--8<-- "solutions/sensors/colour/ex1_colour_match.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/sensors/colour/ex2_night_light.py"
```

### Exercise 3

```python linenums="1"
--8<-- "solutions/sensors/colour/ex3_stop_on_line.py"
```

The threshold of `20` is an example. Measure the reflection of the black line and of the mat, and choose a number about halfway between them.

## Distance Sensor

### Exercise 1

```python linenums="1"
--8<-- "solutions/sensors/distance/ex1_parking_sensor.py"
```

### Exercise 2

```python linenums="1"
--8<-- "solutions/sensors/distance/ex2_stop_before_wall.py"
```

### Exercise 3

The exact numbers depend on the sensor, but readings usually become unreliable closer than a few centimetres and further than about 2 metres, where the sensor returns `2000`. A jumper absorbs much of the sound, so the echo is too weak and the reading may jump around or show `2000`. A wall at an angle reflects the sound away from the sensor, like a ball bouncing off at an angle, so the echo doesn't come back to the sensor.
