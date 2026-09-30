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
