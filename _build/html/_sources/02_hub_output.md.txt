# Hub Outputs

```{topic} In this lesson you will:
- the output features on the Spike Prime Hub
- learn how to change the status light
- learn how to display information on the light matrix
- learn how to produce sounds using the hub speaker
```

```{admonition} Pybrick Documentation
:class: important
To explore all Pybricks' features check the **[Pybricks documentaion](https://docs.pybricks.com/en/stable/index.html)**. This can also be seen in the right-hand panel of the Pybricks IDE.
```

The Spike Prime Hub has three features that can be used to produce output for the robot:

- Hub status light
- The light matrix
- A speaker

```{admonition} Output and Input
:class: note
Imagine that you want the robot to explore a room all by itself. When the robot uses its sensors to see if there are obstacles ahead and decides to turn left, that's the **input**. It's like the robot figuring out what's around it. 

Then, when the robot actually turns and goes in the new direction, that's the **output**. It's the robot taking action based on what it learned from its sensors. 

So, input is when the robot gathers information, and output is the robot using that information to make decisions and move around. It's like the robot's way of thinking and moving on its own!
```

## The Hub Status Light

The Hub Status Light is around the Power button and it is blue by default.

![Hub Status Light](assets/primehub_light.png)

### Status Light Functions

Pybricks has four functions for the status light:

- **[`light.on(color)`](https://docs.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.light.on)** &rarr; Turns on the light at the specified colour.
- **[`light.off()`](https://docs.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.light.off)** &rarr; Turns off the light.
- **[`light.blink(color, durations)`](https://docs.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.light.blink)** &rarr; Blinks the light at a given colour by turning it on and off for given durations.
- **[`light.animate(colors, interval)`](https://docs.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.light.animate)** &rarr; Animates the light with a sequence of colours, shown one by one for the given interval.

### Status Light Example

You will now use all four status light functions:

1. **Create** a new file called `hub_light.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. **Run** your code

```{literalinclude} ./python_files/hub_output_status_light.py
:linenos:
```

```{admonition} Investigate
- **lines 3 - 7** &rarr; imports all the Pybricks command for use with your robot
- **lines 9 - 10** &rarr; creates a PrimeHub and names it `hub`
- **line 14** &rarr; creates an endless loop
- **line 15** &rarr; changes the status light to `MAGENTA`
  - the **[color documentation](https://docs.pybricks.com/en/stable/parameters/color.html#color)** provides more details
- **line 16** &rarr; waits for 1000 milliseconds (ie. 1 second)
- **line 17** &rarr; blinks `RED` in the pattern on for 500ms, off 250ms, on 500ms, off 250ms
- **line 18** &rarr; waits for 1500 milliseconds
- **line 19** &rarr; moves through the three colours `GREEN`, `WHITE` then `ORANGE`, showing  each for 1000ms
- **line 20** &rarr; waits for 3000 milliseconds
- **line 21** &rarr; turns the light off
- **line 16** &rarr; waits for 1000 milliseconds
```

```{admonition} Modify
:class: caution
- can you display different colours?
- can you change the timing of the blink?
- can you change the timing of the animation?
- what happens when you comment out (put a `#` in front) all the `wait` functions?
```

## Light Matrix

The Spike Prime Hub has a five by five light matrix that can be used to display text and images, or individual pixels (light) can be accessed using their coordinates (see below).

![light matrix](assets/primehub_display.png)

### Light Matrix Functions

Pybricks has eight functions for the Light Matrix

- **[`display.orientation(up)`](https://docs.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.display.orientation)** &rarr; Sets the orientation of the light matrix display.
- **[`display.off()`](https://docs.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.display.off)** &rarr; Turns off all the pixels.
- **[`display.pixel(row, column, brightness=100)`](https://docs.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.display.pixel)** &rarr; Turns on one pixel at the specified brightness.
- **[`display.icon(icon)`](https://code.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.display.icon)** &rarr; Displays an icon, represented by a matrix of brightness: % values. **[A list of icons can be found here](https://docs.pybricks.com/en/stable/parameters/icon.html?highlight=icon#pybricks.parameters.Icon)**
- **[`display.animate(matrices, interval)`](https://code.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.display.animate)** &rarr; Displays an animation made using a list of images.
- **[`display.number(number)`](https://code.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.display.number)** &rarr; Displays a number in the range -99 to 99.
- **[`display.char(char)`](https://code.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.display.char)** &rarr; Displays a character or symbol on the light grid. 
- **[`display.text(text, on=500, off=50)`](https://code.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.display.text)** &rarr; Displays a text string, one character at a time, with a pause between each character. 

### Light Matrix Example

The code below uses all eight functions for the light matrix.

1. **Create** a new file called `speaker.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. **Run** your code

```{literalinclude} ./python_files/hub_output_light_matrix.py
:linenos:
```

```{admonition} Investigate
- **lines 3 - 7** &rarr; imports all the Pybricks command for use with your robot
  - make sure to add `Icon` to the end of **line 5**
- **lines 9 - 10** &rarr; creates a PrimeHub and names it `hub`
- **line 15** &rarr; creates an endless loop
- **lines 16 - 27** &rarr; changes which side of the hub is considered up and then displays the up arrow.
- **lines 29 - 30** &rarr; turns the display off for 1 second
- **lines 32 - 37** &rarr; turns on a number of pixels to show the meh face
- **lines 29 - 40** &rarr; turns the display off for 1 second
- **line 42** &rarr; makes an `Icon` list
- **line 43** &rarr; displays each icon in the icon list for 500ms
- **line 44** &rarr; waits for a second
- **lines 46 - 47** &rarr; turns the display off for 1 second
- **lines 49 - 56** &rarr; displays numbers and characters
- **lines 58 - 59** &rarr; turns the display off for 1 second
- **line 61** &rarr; displays the text `C3PO`
- **lines 63 - 54** &rarr; turns the display off for 2 seconds
```

```{admonition} Modify
:class: caution
- can you make the `Icon.HAPPY` spin around the display?
- can you change the meh face so the mouth uses the entire screen and the eyes are four pixels big?
- what happens if you comment out all the `wait` functions?
```

## Speaker

The Prime Hub has a speaker built in, which can be used to produce sounds.

### Speaker Functions

The hub's speaker has three functions:

- **[`speaker.volume(volume)`](https://code.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.speaker.volume)** &rarr;
  - If volume is given, sets the speaker volume.
  - If no volume is given, this method returns the current volume.
- **[`speaker.beep(frequency=500, duration=100)`](https://code.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.speaker.beep)** &rarr; Play a beep/tone.
- **[`speaker.play_notes(notes, tempo=120)`](https://code.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.speaker.play_notes)** &rarr; Plays a sequence of musical notes.

### Speaker Example

The example below uses the three speaker functions:

1. **Create** a new file called `light_matrix.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. **Run** your code

```{literalinclude} ./python_files/hub_output_speaker.py
:linenos:
```

```{admonition} Investigate
- **lines 3 - 7** &rarr; imports all the Pybricks command for use with your robot
- **lines 9 - 10** &rarr; creates a PrimeHub and names it `hub`
- **line 15** &rarr; creates an endless loop
- **line 17** &rarr; sets the speaker volume to 100%
- **lines 18 - 19** &rarr; read the current volume level and assigns it to `current_volume` then display it to the light matrix
- **line 20** &rarr; play a tone of 440Hz for 500ms
- **line 22** &rarr; sets the speaker volume to 50%
- **lines 23 - 24** &rarr; read the current volume level and assigns it to `current_volume` then display it to the light matrix
- **line 25** &rarr; play a tone of 440Hz for 500ms
- **lines 27 - 35** &rarr; a list containing the notes for Oh When The Saints
- **line 37** &rarr; play the notes in the `oh_when_the_saints` list at a tempo of 180bpm
```

```{admonition} Modify
:class: caution
- seeing what is the lowest volume beep you can hear
- seeing what is the lowest pitch beep you can hear
- seeing what is the highest pitch beep you can hear
- make the hub play a different tune
```
