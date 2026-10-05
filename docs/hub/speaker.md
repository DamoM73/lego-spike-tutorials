# Speaker

!!! learn "On this page we will learn"
    - how to set the speaker's volume
    - how to play beeps
    - how to play a tune made of musical notes

!!! terms "Terminology"
    - **frequency** – how high or low a sound is, where a higher frequency gives a higher pitch.
    - **hertz** – the unit (Hz) used to measure frequency.
    - **volume** – how loud a sound is, from `0` (silent) to `100` (loudest).
    - **return value** – a value that a method gives back to our program, such as the current volume.
    - **default value** – the value a parameter uses when we don't give one, such as a 500 Hz beep for 100 ms.
    - **tempo** – the speed of a tune, measured in beats per minute.

The hub has a small built-in speaker. We can set its volume, play beeps and play tunes made of musical notes.

Possible uses:

- sound effects, such as a beep when a button is pressed
- warning sounds, such as a reversing beeper
- playing a tune when the robot finishes a task
- hearing when a sensor detects something, without looking at the robot

## Connect it

The speaker is built into the hub, so we don't need to connect anything.

- See [Setup](../start/setup.md#create-and-run-a-program) for how to create and run each example.
- **Frequency** is how high or low a sound is, measured in **hertz** (Hz). A higher frequency is a higher pitch.
- **Volume** goes from `0` (silent) to `100` (loudest).
- Times are in milliseconds (ms). 1000 ms is 1 second.

## Set it up

The speaker is part of the hub. We import the Pybricks commands, then create the hub in the setup:

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
| `hub.speaker.volume(volume)` | `volume`: 0–100 | int (%) when no value is given | Sets the volume. With no value, returns the current volume |
| `hub.speaker.beep(frequency=500, duration=100)` | `frequency`: Hz; `duration`: ms | none | Plays one beep |
| `hub.speaker.play_notes(notes, tempo=120)` | `notes`: list of note strings; `tempo`: beats per minute | none | Plays a tune |

### `volume()`

Sets how loud the speaker is for every sound after it. If we call `hub.speaker.volume()` with nothing in the brackets, it returns the current volume instead.

```python linenums="1"
--8<-- "examples/hub/speaker/volume/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → sets the speaker volume to 20%.
    - **line 12** → starts the main loop, which repeats forever.
    - **line 13** → plays a beep at the default pitch and length.
    - **line 14** → waits 1 second before the loop starts again.

### `beep()`

Plays one beep. We choose its frequency and how long it lasts. With no values, it plays a 500 Hz beep for 100 ms.

```python linenums="1"
--8<-- "examples/hub/speaker/beep/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 11** → starts the main loop, which repeats forever.
    - **line 12** → plays a 440 Hz beep (the note A) for 500 ms.
    - **line 13** → waits 500 ms before the loop starts again.

### `play_notes()`

Plays a list of notes as a tune. The **tempo** is the speed in beats per minute.

Each note is a string such as `"C4/4"`:

| Part | Example | Meaning |
| --- | --- | --- |
| Note | `C` | The note name, `A` to `G`, or `R` for a rest (silence) |
| Sharp or flat | `#` or `b` | Optional. `C#4/4` is C sharp |
| Octave | `4` | How high the note is. `C4` is middle C |
| Length | `/4` | `/1` is a whole note, `/2` a half note, `/4` a quarter note (one beat), `/8` an eighth note |

```python linenums="1"
--8<-- "examples/hub/speaker/play_notes/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **lines 9–14** → stores the notes for *When the Saints Go Marching In* as a list in `saints`.
    - **line 17** → starts the main loop, which repeats forever.
    - **line 18** → plays the notes in `saints` at 180 beats per minute.
    - **line 19** → waits 1 second before playing the tune again.

## Documentation

Documentation is the official guide written by the people who made the code library, and we can use it to look up every method and its parameters, including ones that aren't covered on this page.

- [Pybricks — Prime Hub speaker](https://docs.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.speaker.volume)

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `speaker` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#speaker) page.

### Exercise 1

Starter: `speaker/ex1_siren`

Can you make the hub sound like a siren by switching between a high beep and a low beep?

### Exercise 2

Starter: `speaker/ex2_new_tune`

Can you change the program so the hub plays a different tune, such as *Twinkle Twinkle Little Star*?

### Exercise 3

Starter: `speaker/ex3_hearing_range`

What are the lowest and highest beep frequencies you can hear? What happens outside that range? Why do you think this happens?
