# Colour Sensor

```{topic} In this lesson you will:
- detect the colour of a surface or light source
- detect the amount of light reflected from a surface
- detect the amount of ambient light
```

```{admonition} Pybrick Documentation
:class: important
To explore all Pybricks' features check the **[Pybricks documentaion](https://docs.pybricks.com/en/stable/index.html)**. This can also be seen in the right-hand panel of the Pybricks IDE.
```

The color sensor has three main modes: color, reflected light, and ambient light. It can also be used as a light source.

- **Color** - In this mode, the colour sensor can differentiate eight different LEGO colors.
- **Reflected light intensity** - In this mode, the color sensor emits a light and measures the amount reflected back into itself from the surface you are testing.
- **Ambient light intensity** - In this mode, the colour sensor measures the amount of light in its environment, without producing its own light source.

![color light sensor](assets/sensor_color_lights.png)

To initialise the color sensor you must call the `ColorSensor()` class and nominate it's port. For example, with the robot you would use:

`color_sensor = ColorSensor(Port.D)`

## Color Sensor Functions

Pybricks provides three functions to interact with the color sensor:

- **[`color(surface=True)→ Color`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.color)** &rarr; Scans the color of a surface or an external light source.
  - Choose `True` to scan the color of objects and surfaces. Choose `False` to scan the color of screens and other external light sources.
- **[`reflection()→ int: %`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.reflection)** &rarr; Measures how much a surface reflects the light emitted by the sensor.
- **[`ambient()→ int: %`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.ambient)** &rarr; Measures the ambient light intensity.

Pybricks also has a configuring function to choose which colors can be returned by `color()`:

- **[`detectable_colors(colors)`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.detectable_colors)** &rarr; Specify only colors that you wish to detect in your application. This way, the full-color measurements are rounded to the nearest desired color, and other colors are ignored.

Finally Pybricks allows you to turn on the color sensor's lights:

- **[`lights.on(brightness)`](https://code.pybricks.com/static/docs/v2.7.0/pupdevices/colorsensor.html#pybricks.pupdevices.ColorSensor.lights.on)** &rarr; Turns on the lights at the specified brightness.

## Color Sensor Example

Check how to use each of these functions by using the following code.

1. **Create** a new file called `color_sensor.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. **Run** your code:
   - use the **left button** and **right button** to change color sensor's mode

```{literalinclude} ./python_files/color_sensor.py
:linenos:
```

```{admonition} Investigate
- **lines 3 - 7** &rarr; imports all the Pybricks command for use with your robot
- **line 10** &rarr; initialises the hub
- **line 11** &rarr; initialises the color sensor
- **line 12** &rarr; a list providing an indicator letter for the modes
- **line 13** &rarr; a flag variable which keeps track of which mode the color sensor should use
- **line 16** &rarr; creates the main loop
- **line 17** &rarr; detects any buttons that are currently pressed and stores the in `presses`
- **lines 19 - 21** &rarr; changes mode downwards if left button is pressed
   - `and mode > 0` ensures that the mode cannot go past `0`
   - `wait(250)` prevents a single press registering mutiple times
- **lines 22 - 24** &rarr; changes mode upwards if right button is pressed
   - `and mode < 3` ensures that the mode cannot go past `3`
   - `wait(250)` prevents a single press registering mutiple times
- **line 26** &rarr; displays the corresponsing mode character from `modes`
- **lines 28 - 29** &rarr; gets the surface color reading and prints it
- **lines 30 - 31** &rarr; gets the light color reading and prints it
- **lines 32 - 33** &rarr; gets the reflected light color reading and prints it
- **lines 34 - 35** &rarr; gets the ambient light color reading and prints it
```

```{admonition} Modify
:class: caution
- what happens when you comment out **line 21** and **line 24**?
- what happens if you remove `and mode > 0` from **line 19** and `and mode < 3` from **line 22**?
