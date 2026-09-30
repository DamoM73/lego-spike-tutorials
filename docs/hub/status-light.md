# Status Light

!!! learn "On this page we will learn"
    - how to turn the status light on in different colours
    - how to turn it off
    - how to blink it and cycle through colours

The status light is the coloured light around the hub's power button. We can turn it on in different colours, blink it and cycle through colours.

Possible uses:

- showing which part of a program is running
- warning signals, such as flashing red near an obstacle
- showing a sensor reading as a colour
- team or robot identification

![Hub Status Light](../assets/primehub_light.png)

## Connect it

The status light is built into the hub, so we don't need to connect anything.

- See [Setup](../start/setup.md#create-and-run-a-program) for how to create and run each example.
- The light is off when a program starts.
- Colours are set with the `Color` constants, such as `Color.RED`. The available colours are `RED`, `ORANGE`, `YELLOW`, `GREEN`, `CYAN`, `BLUE`, `VIOLET`, `MAGENTA`, `WHITE`, `GRAY` and `BROWN`.
- Pybricks uses the American spelling `Color` in code, but we still write "colour" everywhere else.

## Set it up

The status light is part of the hub. We import the Pybricks commands, then create the hub in the setup:

```python linenums="1"
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Setup
hub = PrimeHub()
```

## Methods

| Method | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `hub.light.on(color)` | `color`: a `Color` | none | Turns the light on in the chosen colour |
| `hub.light.off()` | none | none | Turns the light off |
| `hub.light.blink(color, durations)` | `color`: a `Color`; `durations`: list of on and off times in ms | none | Blinks the light on and off, forever, while the program keeps running |
| `hub.light.animate(colors, interval)` | `colors`: list of `Color`s; `interval`: ms per colour | none | Cycles through the colours, forever, while the program keeps running |

### `on()`

Turns the status light on in a colour. It stays that colour until we change it or turn it off.

```python linenums="1"
--8<-- "examples/hub/status_light/on/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 11** → starts the main loop, which repeats forever.
    - **line 12** → turns the status light on in magenta.

### `off()`

Turns the status light off.

```python linenums="1"
--8<-- "examples/hub/status_light/off/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 11** → starts the main loop, which repeats forever.
    - **line 12** → turns the status light on in green.
    - **line 13** → waits 1000 milliseconds (1 second).
    - **line 14** → turns the status light off.
    - **line 15** → waits another second before the loop starts again.

### `blink()`

Blinks the light on and off. The `durations` list gives the times in milliseconds: on, off, on, off, and so on. The blinking carries on **in the background**, so the rest of the program keeps running.

```python linenums="1"
--8<-- "examples/hub/status_light/blink/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → starts blinking the light red: on for 500 ms, then off for 250 ms, over and over.
    - **line 12** → starts the main loop, which repeats forever.
    - **line 13** → does nothing, but keeps the program running so the light keeps blinking.

!!! tip "Why is `blink()` in the setup?"
    `blink()` and `animate()` keep running by themselves once they start, so we only need to call them once. If we called them inside the main loop, they would restart every time the loop went around.

### `animate()`

Shows each colour in a list for a set time, then starts the list again. Like `blink()`, it runs in the background.

```python linenums="1"
--8<-- "examples/hub/status_light/animate/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → starts cycling the light through green, white and orange, showing each colour for 1000 ms.
    - **line 12** → starts the main loop, which repeats forever.
    - **line 13** → does nothing, but keeps the program running so the animation keeps playing.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [Pybricks — Prime Hub light](https://docs.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.light.on)
- [Pybricks — Color](https://docs.pybricks.com/en/stable/parameters/color.html)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `status_light` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#status-light) page.

### Exercise 1

Starter: `status_light/ex1_school_colours`

Can you make the status light switch between your school colours, changing every second?

### Exercise 2

Starter: `status_light/ex2_sos`

Can you make the status light blink **SOS** in Morse code? SOS is three short blinks, three long blinks, then three short blinks. Make the long blinks three times as long as the short ones.

### Exercise 3

Starter: `status_light/ex3_police_light`

Can you make the status light flash between red and blue every quarter of a second, like a police car?
