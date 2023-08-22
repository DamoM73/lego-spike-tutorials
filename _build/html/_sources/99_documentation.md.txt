# Spike Prime Python API

## App module

The `app` module is used communicate between hub and app.

### Bargraph

The `bargraph` module is used make bar graphs in the SPIKE App

To use the `bargraph` module simply import the module like so:

```{code-block} python
:linenos:
from app import bargraph
```

#### bargraph.change

`change(color: int, value: float) -> None`

- `color: int` &rarr; A colour from the `color` module
- `value: float` &rarr; The value

#### bargraph.clear_all

`clear_all() -> None`

#### bargraph.get_value

`get_value(color: int) -> Awaitable`

- `color: int` &rarr; A colour from the `color` module

#### bargraph.hide

`hide() -> None`

#### bargraph.set_value

`set_value(color: int, value: float) -> None`

- `color: int` &rarr; A colour from the `color` module
- `value: float` &rarr; The value

#### bargraph.show

`show(fullscreen: bool) -> None`

- `fullscreen: bool` &rarr; Show in full screen

### Display

The `display` module is used to show images in the SPIKE App

To use the `display` module simply import the module like so:

```{code-block} python
:linenos:
from app import display
```

#### display.hide

`hide() -> None`

#### display.image

`image(image: int) -> None`

- image: int &rarr; The id of the image to show. The range of available images is 1 to 21. There are constants in the display module for these.

#### display.show

`show(fullscreen: bool) -> None`

- `fullscreen: bool` &rarr; Show in full screen

#### display.text

`text(text: str) -> None`

`text: str`

- The text to display

#### display.constants

- `IMAGE_ROBOT_1` &rarr; `1`
- `IMAGE_ROBOT_2` &rarr; `2`
- `IMAGE_ROBOT_3` &rarr; `3`
- `IMAGE_ROBOT_4` &rarr; `4`
- `IMAGE_ROBOT_5` &rarr; `5`
- `IMAGE_HUB_1` &rarr; `6`
- `IMAGE_HUB_2` &rarr; `7`
- `IMAGE_HUB_3` &rarr; `8`
- `IMAGE_HUB_4` &rarr; `9`
- `IMAGE_AMUSEMENT_PARK` &rarr; `10`
- `IMAGE_BEACH` &rarr; `11`
- `IMAGE_HAUNTED_HOUSE` &rarr; `12`
- `IMAGE_CARNIVAL` &rarr; `13`
- `IMAGE_BOOKSHELF` &rarr; `14`
- `IMAGE_PLAYGROUND` &rarr; `15`
- `IMAGE_MOON` &rarr; `16`
- `IMAGE_CAVE` &rarr; `17`
- `IMAGE_OCEAN` &rarr; `18`
- `IMAGE_POLAR_BEAR` &rarr; `19`
- `IMAGE_PARK` &rarr; `20`
- `IMAGE_RANDOM` &rarr; `21`

### Linegraph

The `linegraph` module is used make line graphs in the SPIKE App

To use the `linegraph` module simply import the module like so:

```{code-block} python
:linenos:
from app import linegraph
```

#### linegraph.clear

`clear(color: int) -> None`

- `color: int` &rarr; A colour from the `color` module

#### linegraph.clear_all

`clear_all() -> None`

#### linegraph.get_average

`get_average(color: int) -> Awaitable`

- `color: int` &rarr; A colour from the `color` module

#### linegraph.get_last

`get_last(color: int) -> Awaitable`

- `color: int` &rarr; A colour from the `color` module

#### linegraph.get_max

`get_max(color: int) -> Awaitable`

- `color: int` &rarr; A colour from the `color` module

#### linegraph.get_min

`get_min(color: int) -> Awaitable`

- `color: int` &rarr; A colour from the `color` module

#### linegraph.hide

`hide() -> None`

#### linegraph.plot

`plot(color: int, x: float, y: float) -> None`

- `color: int` &rarr; A colour from the `color` module
- `x: float` &rarr; The X value
- `y: float` &rarr; The Y value

#### linegraph.show

`show(fullscreen: bool) -> None`

- `fullscreen: bool` &rarr; Show in full screen

### Music

The `music` module is used make music in the SPIKE App

To use the `music` module simply import the module like so:

```{code-block} python
:linenos:
from app import music
```

#### music.play_drum

`play_drum(drum: int) -> None`

- `drum: int` &rarr; The drum name. See all available values in the `app.sound` module.

#### music.play_note

`play_note(instrument: int, note: int, duration: int) -> None`

- `instrument: int` &rarr; The instrument name. See all available values in the `app.music` module.
- `note: int` &rarr; The midi note to play (`0`-`130`)
- `duration: int` &rarr; The duration in milliseconds

#### music.constants

- `DRUM_BASS` &rarr; `2`
- `DRUM_BONGO` &rarr; `13`
- `DRUM_CABASA` &rarr; `15`
- `DRUM_CLAVES` &rarr; `9`
- `DRUM_CLOSED_HI_HAT` &rarr; `6`
- `DRUM_CONGA` &rarr; `14`
- `DRUM_COWBELL` &rarr; `11`
- `DRUM_CRASH_CYMBAL` &rarr; `4`
- `DRUM_CUICA` &rarr; `18`
- `DRUM_GUIRO` &rarr; `16`
- `DRUM_HAND_CLAP` &rarr; `8`
- `DRUM_OPEN_HI_HAT` &rarr; `5`
- `DRUM_SIDE_STICK` &rarr; `3`
- `DRUM_SNARE` &rarr; `1`
- `DRUM_TAMBOURINE` &rarr; `7`
- `DRUM_TRIANGLE` &rarr; `12`
- `DRUM_VIBRASLAP` &rarr; `17`
- `DRUM_WOOD_BLOCK` &rarr; `10`
- `INSTRUMENT_BASS` &rarr; `6`
- `INSTRUMENT_BASSOON` &rarr; `14`
- `INSTRUMENT_CELLO` &rarr; `8`
- `INSTRUMENT_CHOIR` &rarr; `15`
- `INSTRUMENT_CLARINET` &rarr; `10`
- `INSTRUMENT_ELECTRIC_GUITAR` &rarr; `5`
- `INSTRUMENT_ELECTRIC_PIANO` &rarr; `2`
- `INSTRUMENT_FLUTE` &rarr; `12`
- `INSTRUMENT_GUITAR` &rarr; `4`
- `INSTRUMENT_MARIMBA` &rarr; `19`
- `INSTRUMENT_MUSIC_BOX` &rarr; `17`
- `INSTRUMENT_ORGAN` &rarr; `3`
- `INSTRUMENT_PIANO` &rarr; `1`
- `INSTRUMENT_PIZZICATO` &rarr; `7`
- `INSTRUMENT_SAXOPHONE` &rarr; `11`
- `INSTRUMENT_STEEL_DRUM` &rarr; `18`
- `INSTRUMENT_SYNTH_LEAD` &rarr; `20`
- `INSTRUMENT_SYNTH_PAD` &rarr; `21`
- `INSTRUMENT_TROMBONE` &rarr; `9`
- `INSTRUMENT_VIBRAPHONE` &rarr; `16`
- `INSTRUMENT_WOODEN_FLUTE` &rarr; `13`

### Sound

The `sound` module is used play sounds in the SPIKE App

To use the `sound` module simply import the module like so:

```{code-block} python
:linenos:
from app import sound
```

#### sound.play

- `play(sound_name: str, volume: int &rarr; 100, pitch: int &rarr; 0, pan: int &rarr; 0) -> Awaitable`

Play a sound in the SPIKE App

- `sound_name: str` &rarr; The sound name as seen in the Word Blocks sound extension
- `volume: int` &rarr; The volume (`0`-`100`)
- `pitch: int` &rarr; The pitch of the sound
- `pan: int` &rarr; The pan effect determines which speaker is emitting the sound, with `-100` being only the left speaker, `0` being normal, and `100` being only the right speaker.

#### sound.set_attributes

`set_attributes(volume: int, pitch: int, pan: int) -> None`

- `volume: int` &rarr; The volume (`0`-`100`)
- `pitch: int` &rarr; The pitch of the sound
- `pan: int` &rarr; The pan effect determines which speaker is emitting the sound, with `-100` being only the left speaker, `0` being normal, and `100` being only the right speaker.

#### sound.stop

`stop() -> None`

## Colour module

The `color` module contains all the colour constants to use with the `color_matrix`, `color_sensor` and `light` modules.

To use the `color` module, add the following import statement to your project:

```{code-block} python
:linenos:
import color
```

### color.constants

- `BLACK` &rarr; `0`
- `MAGENTA` &rarr; `1`
- `PURPLE` &rarr; `2`
- `BLUE` &rarr; `3`
- `AZURE` &rarr; `4`
- `TURQUOISE` &rarr; `5`
- `GREEN` &rarr; `6`
- `YELLOW` &rarr; `7`
- `ORANGE` &rarr; `8`
- `RED` &rarr; `9`
- `WHITE` &rarr; `10`
- `UNKNOWN` &rarr; `-1`

## Colour Matrix module

To use the `color_matrix` module, add the following import statement to your project:

```{code-block} python
:linenos:
import color_matrix
```

All functions in the module should be called inside the `color_matrix` module as a prefix like so:

```{code-block} python
:linenos:
color_matrix.set_pixel(port.A, 1, 1, color.BLUE, 10)
```

### color_matrix.clear

`clear(port: int) -> None`

Turn off all pixels on a Colour Matrix

```{code-block} python
:linenos:
from hub import port
import color_matrix

color_matrix.clear(port.A)
```

- `port: int` &rarr; A port from the `port` submodule in the `hub` module

### color_matrix.get_pixel

`get_pixel(port: int, x: int, y: int) -> tuple[int, int]`

Retrieve a specific pixel represented as a tuple containing the colour and intensity

```{code-block} python
:linenos:
from hub import port
import color_matrix

# Print the colour and intensity of the 0,0 pixel on the Colour Matrix connected to port A 
print(color_matrix.get_pixel(port.A, 0, 0))
```

- `port: int` &rarr; A port from the `port` submodule in the `hub` module
- `x: int` &rarr; The X value (`0`-`2`)
- `y: int` &rarr; The Y value (`0`-`2`)

### color_matrix.set_pixel

`set_pixel(port: int, x: int, y: int, pixel: tuple[color: int, intensity: int]) -> None`

Change a single pixel on a Colour Matrix

```{code-block} python
:linenos:
from hub import port
import color
import color_matrix

# Change the colour of the 0,0 pixel on the Colour Matrix connected to port A 
color_matrix.set_pixel(port.A, 0, 0, (color.RED, 10))

# Print the colour of the 0,0 pixel on the Colour Matrix connected to port A 
print(color_matrix.get_pixel(port.A, 0, 0)[0])
```

- `port: int` &rarr; A port from the `port` submodule in the `hub` module
- `x: int` &rarr; The X value (`0`-`2`)
- `y: int` &rarr; The Y value (`0`-`2`)
- `pixel: tuple[color: int, intensity: int]` &rarr; Tuple containing colour and intensity, meaning how bright to light up the pixel

### color_matrix.show

`show(port: int, pixels: list[tuple[int, int]]) -> None`

Change all pixels at once on a Colour Matrix

```{code-block} python
:linenos:
from hub import port
import color
import color_matrix

# Update all pixels on Colour Matrix using the show function 

# Create a list with 18 items (colour and intensity pairs) 
pixels = [(color.BLUE, 10)] * 9 

# Update all pixels to show same colour and intensity 
color_matrix.show(port.A, pixels)
```

- `port: int` &rarr; A port from the `port` submodule in the `hub` module
- `pixels: list[tuple[int, int]]` &rarr; A list containing colour and intensity value tuples for all 9 pixels.

## Colour Sensor module

The `color_sensor` module enables you to write code that reacts to specific colours or the intensity of the reflected light.

To use the `color_sensor` module, add the following import statement to your project:

```{code-block} python
:linenos:
import color_sensor
```

All functions in the module should be called inside the `color_sensor` module as a prefix like so:

```{code-block} python
:linenos:
color_sensor.reflection(port.A)
```

The Colour Sensor can recognise the following colours:

- Red
- Green
- Blue
- Magenta
- Yellow
- Orange
- Azure
- Black
- White

### color_sensor.color

`color(port: int) -> int`

Returns the colour value of the detected colour. Use the color module to map the colour value to a specific colour.

```{code-block} python
:linenos:
import color_sensor
from hub import port
import color

if color_sensor.color(port.A) is color.RED:
    print("Red detected")
```

- `port: int` &rarr; A port from the `port` submodule in the `hub` module

### color_sensor.reflection

`reflection(port: int) -> int`

Retrieves the intensity of the reflected light (`0`-`100`%).

- `port: int` &rarr; A port from the `port` submodule in the `hub` module

### color_sensor.rgbi

`rgbi(port: int) -> tuple[int, int, int, int]`

Retrieves the overall colour intensity and intensity of red, green and blue.

Returns `tuple[red: int, green: int, blue: int, intensity: int]`

- `port: int` &rarr; A port from the `port` submodule in the `hub` module

## Device module

The `device` module enables you to write code to get information about devices plugged into the hub.

To use the `device` module, add the following import statement to your project:

```{code-block} python
:linenos:
import device

```

All functions in the module should be called inside the `device` module as a prefix like so:

```{code-block} python
:linenos:
device.device_id(port.A)
```

### device.data

`data(port: int) -> tuple[int]`

Retrieve the raw LPF-2 data from a device.

- `port: int` &rarr; A port from the `port` submodule in the `hub` module

### device.device_id

`device_id(port: int) -> int`

Retrieve the device ID of a device. Each device has an ID based on its type.

- `port: int` &rarr; A port from the `port` submodule in the `hub` module

### device.get_duty_cycle

`get_duty_cycle(port: int) -> int`

Retrieve the duty cycle for a device. Returned values are in the range `0` to `10000`

- `port: int` &rarr; A port from the `port` submodule in the `hub` module

### device.ready

`ready(port: int) -> bool`

When a device is attached to the hub it might take a short amount of time before it's ready to accept requests.
Use ready to test for the readiness of the attached devices.

- `port: int` &rarr; A port from the `port` submodule in the `hub` module

### device.set_duty_cycle

`set_duty_cycle(port: int, duty_cycle: int) -> None`

Set the duty cycle on a device. Range 0 to 10000

- `port: int` &rarr; A port from the `port` submodule in the `hub` module
- `duty_cycle: int` &rarr; The PWM value (`0`-`10000`)

### device.constants

- `COLOR_SENSOR` &rarr; `61`
- `FORCE_SENSOR` &rarr; `63`

## Distance Sensor module

The `distance_sensor` module enables you to write code that reacts to specific distances or lights up the Distance Sensor in different ways.

To use the `distance_sensor` module, add the following import statement to your project:

```{code-block} python
:linenos:
import distance_sensor
```

All functions in the module should be called inside the `distance_sensor` module as a prefix like so:

```{code-block} python
:linenos:
distance_sensor.distance(port.A)
```

### distance_sensor.clear

`clear(port: int) -> None`

Turns off all the lights in the Distance Sensor connected to port.

- `port: int` &rarr; A port from the `port` submodule in the `hub` module

### distance_sensor.distance

`distance(port: int) -> int`

Retrieve the distance in millimetres captured by the Distance Sensor connected to port. If the Distance Sensor cannot read a valid distance it will return -1.

- `port: int` &rarr; A port from the `port` submodule in the `hub` module

### distance_sensor.get_pixel

`get_pixel(port: int, x: int, y: int) -> int`

Retrieve the intensity of a specific light on the Distance Sensor connected to port.

- `port: int` &rarr; A port from the `port` submodule in the `hub` module
- `x: int` &rarr; The X value (`0` - `3`)
- `y: int` &rarr; The Y value, range (`0` - `3`)

### distance_sensor.set_pixel

`set_pixel(port: int, x: int, y: int, intensity: int) -> None`

Changes the intensity of a specific light on the Distance Sensor connected to port.

- `port: int` &rarr; A port from the `port` submodule in the `hub` module
- `x: int` &rarr; The X value (`0` - `3`)
- `y: int` &rarr; The Y value, range (`0` - `3`)
- `intensity: int` &rarr; How bright to light up the pixel

### distance_sensor.show

`show(port: int, pixels: list[int]) -> None`

Change all the lights at the same time.

```{code-block} python
:linenos:
from hub import port
import distance_sensor

# Update all pixels on Distance Sensor using the show function 

# Create a list with 4 identical intensity values 
pixels = [100] * 4 

# Update all pixels to show same intensity 
distance_sensor.show(port.A, pixels)
```

- `port: int` &rarr; A port from the `port` submodule in the `hub` module
- `pixels: bytes` A list containing intensity values for all 4 pixels.

## Force Sensor module

The `force_sensor` module contains all functions and constants to use the Force Sensor.

To use the `force_sensor` module, add the following import statement to your project:

```{code-block} python
:linenos:
import force_sensor
```

All functions in the module should be called inside the `force_sensor` module as a prefix like so:

```{code-block} python
:linenos:
force_sensor.force(port.A)
```

### force_sensor.force

`force(port: int) -> int`

Retrieves the measured force as decinewton. Values range from `0` to `100`

```{code-block} python
:linenos:
from hub import port
import force_sensor

print(force_sensor.force(port.A))
```

- `port: int` &rarr; A port from the `port` submodule in the `hub` module

### force_sensor.pressed

`pressed(port: int) -> bool`

Tests whether the button on the sensor is pressed. Returns `True` if the force sensor connected to the `port` is pressed.

```{code-block} python
:linenos:
from hub import port
import force_sensor

print(force_sensor.pressed(port.A))
```

- `port: int` &rarr; A port from the `port` submodule in the `hub` module

### force_sensor.raw

`raw(port: int) -> int`

Returns the raw, uncalibrated force value of the force sensor connected on port `port`

```{code-block} python
:linenos:
from hub import port
import force_sensor

print(force_sensor.raw(port.A))
```

- `port: int` &rarr; A port from the `port` submodule in the `hub` module

## Hub module

### Button

To use the `button` module, add the following import statement to your project:

```{code-block} python
:linenos:
from hub import button
```

All functions in the module should be called inside the `button` module as a prefix like so:

```{code-block} python
:linenos:
button.pressed(button.LEFT)
```

#### button.pressed

`int pressed(button: int) -> int`

This module allows you to react to buttons being pressed on the hub. You must first import the `button` module to use the buttons.

```{code-block} python
:linenos:
from hub import button

left_button_press_duration = 0

# Wait for the left button to be pressed 
while not button.pressed(button.LEFT):
    pass

# As long as the left button is being pressed, update the `left_button_press_duration` variable 
while button.pressed(button.LEFT):
    left_button_press_duration = button.pressed(button.LEFT)

print("Left button was pressed for " + str(left_button_press_duration) + " milliseconds")
```

- `button: int` &rarr; A button from the `button` submodule in the `hub` module

#### button.constants

- `LEFT` &rarr; `1` - Left button next to the power button on the SPIKE Prime hub
- `RIGHT` &rarr; `2` - Right button next to the power button on the SPIKE Prime hub

### Light

The `light` module includes functions to change the colour of the light on the SPIKE Prime hub.

To use the `light` module, add the following import statement to your project:

```{code-block} python
:linenos:
from hub import light
```

All functions in the module should be called inside the `light` module as a prefix like so:

```{code-block} python
:linenos:
light.color(color.RED)
```

#### light.color

`color(light: int, color: int) -> None`

Change the colour of a light on the hub.

```{code-block} python
:linenos:
from hub import light
import color

# Change the light to red 
light.color(light.POWER, color.RED)
```

- `light: int` &rarr; The light on the hub
- `color: int` &rarr; A colour from the `color` module

#### light.constants

- `POWER` &rarr; `0` - The power button. On SPIKE Prime it's the button between the left and right buttons.
- `CONNECT` &rarr; `1` - The light around the Bluetooth connect button on SPIKE Prime.

### Light Matrix

To use the `light_matrix` module, add the following import statement to your project:

```{code-block} python
:linenos:
from hub import light_matrix
```

All functions in the module should be called inside the `light_matrix` module as a prefix like so:

```{code-block} python
:linenos:
light_matrix.write("Hello World")
```

#### light_matrix.clear

`clear() -> None`

Switches off all of the pixels on the Light Matrix.

```{code-block} python
:linenos:
from hub import light_matrix
import time
# Update pixels to show an image on Light Matrix, and then turn them off using the clear function 

# Show a small heart 
light_matrix.show_image(2)

# Wait for two seconds 
time.sleep_ms(2000)

# Switch off the heart 
light_matrix.clear()
```

#### light_matrix.get_orientation

`get_orientation() -> int`

Retrieve the current orientation of the Light Matrix.

Can be used with the following constants:

- `orientation.UP`
- `orientation.LEFT`
- `orientation.RIGHT`
- `orientation.DOWN`

#### light_matrix.get_pixel

`get_pixel(x: int, y: int) -> int`

Retrieve the intensity of a specific pixel on the Light Matrix.

```{code-block} python
:linenos:
from hub import light_matrix

# Show a heart 
light_matrix.show_image(1)

# Print the value of the centre pixel's intensity 
print(light_matrix.get_pixel(2, 2))
```

- `x: int` &rarr; The X value, range (`0` - `4`)
- `y: int` &rarr; The Y value, range (`0` - `4`)

#### light_matrix.set_orientation

`set_orientation(top: int) -> int`

Change the orientation of the Light Matrix. All subsequent calls will use the new orientation.

Can be used with the following constants:

- `orientation.UP`
- `orientation.LEFT`
- `orientation.RIGHT`
- `orientation.DOWN`

- `top: int` &rarr; The side of the hub to be the top

#### light_matrix.set_pixel

`set_pixel(x: int, y: int, intensity: int) -> None`

Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix.

```{code-block} python
:linenos:
from hub import light_matrix
# Turn on the pixel in the centre of the hub 
light_matrix.set_pixel(2, 2, 100)
```

- `x: int` &rarr; The X value, range (`0` - `4`)
- `y: int` &rarr; The Y value, range (`0` - `4`)
- `intensity: int` &rarr; How bright to light up the pixel

#### light_matrix.show

`show(pixels: list[int]) -> None`

Change all the lights at the same time.

```{code-block} python
:linenos:
from hub import light_matrix
# Update all pixels on Light Matrix using the show function 

# Create a list with 25 identical intensity values 
pixels = [100] * 25 

# Update all pixels to show same intensity 
light_matrix.show(pixels)
```

- `pixels: Iterable` &rarr; A list containing light intensity values for all 25 pixels.

#### light_matrix.show_image

`show_image(image: int) -> None`

Display one of the built-in images on the display.

```{code-block} python
:linenos:
from hub import light_matrix
# Update pixels to show an image on Light Matrix using the show_image function 

# Show a smiling face 
light_matrix.show_image(light_matrix.IMAGE_HAPPY)
```

- `image: int` &rarr; The id of the image to show. The range of available images is `1` to `67`. There are constants in the `light_matrix` module for these.

#### light_matrix.write

`write(text: str, intensity: int = 100, time_per_character: int = 500) -> Awaitable`

Displays text on the Light Matrix, one letter at a time, scrolling from right to left, except if there is a single character to show (which will not scroll)

```{code-block} python
:linenos:
from hub import light_matrix
# White a message to the hub 
light_matrix.write("Hello, world!")
```

- `text: str` &rarr; The text to display
- `intensity: int` &rarr; How bright to light up the pixel
- `time_per_character: int` &rarr; How long to show each character on the display

#### light_matrix.constants

- `IMAGE_HEART` &rarr; `1`
- `IMAGE_HEART_SMALL` &rarr; `2`
- `IMAGE_HAPPY` &rarr; `3`
- `IMAGE_SMILE` &rarr; `4`
- `IMAGE_SAD` &rarr; `5`
- `IMAGE_CONFUSED` &rarr; `6`
- `IMAGE_ANGRY` &rarr; `7`
- `IMAGE_ASLEEP` &rarr; `8`
- `IMAGE_SURPRISED` &rarr; `9`
- `IMAGE_SILLY` &rarr; `10`
- `IMAGE_FABULOUS` &rarr; `11`
- `IMAGE_MEH` &rarr; `12`
- `IMAGE_YES` &rarr; `13`
- `IMAGE_NO` &rarr; `14`
- `IMAGE_CLOCK12` &rarr; `15`
- `IMAGE_CLOCK1` &rarr; `16`
- `IMAGE_CLOCK2` &rarr; `17`
- `IMAGE_CLOCK3` &rarr; `18`
- `IMAGE_CLOCK4` &rarr; `19`
- `IMAGE_CLOCK5` &rarr; `20`
- `IMAGE_CLOCK6` &rarr; `21`
- `IMAGE_CLOCK7` &rarr; `22`
- `IMAGE_CLOCK8` &rarr; `23`
- `IMAGE_CLOCK9` &rarr; `24`
- `IMAGE_CLOCK10` &rarr; `25`
- `IMAGE_CLOCK11` &rarr; `26`
- `IMAGE_ARROW_N` &rarr; `27`
- `IMAGE_ARROW_NE` &rarr; `28`
- `IMAGE_ARROW_E` &rarr; `29`
- `IMAGE_ARROW_SE` &rarr; `30`
- `IMAGE_ARROW_S` &rarr; `31`
- `IMAGE_ARROW_SW` &rarr; `32`
- `IMAGE_ARROW_W` &rarr; `33`
- `IMAGE_ARROW_NW` &rarr; `34`
- `IMAGE_GO_RIGHT` &rarr; `35`
- `IMAGE_GO_LEFT` &rarr; `36`
- `IMAGE_GO_UP` &rarr; `37`
- `IMAGE_GO_DOWN` &rarr; `38`
- `IMAGE_TRIANGLE` &rarr; `39`
- `IMAGE_TRIANGLE_LEFT` &rarr; `40`
- `IMAGE_CHESSBOARD` &rarr; `41`
- `IMAGE_DIAMOND` &rarr; `42`
- `IMAGE_DIAMOND_SMALL` &rarr; `43`
- `IMAGE_SQUARE` &rarr; `44`
- `IMAGE_SQUARE_SMALL` &rarr; `45`
- `IMAGE_RABBIT` &rarr; `46`
- `IMAGE_COW` &rarr; `47`
- `IMAGE_MUSIC_CROTCHET` &rarr; `48`
- `IMAGE_MUSIC_QUAVER` &rarr; `49`
- `IMAGE_MUSIC_QUAVERS` &rarr; `50`
- `IMAGE_PITCHFORK` &rarr; `51`
- `IMAGE_XMAS` &rarr; `52`
- `IMAGE_PACMAN` &rarr; `53`
- `IMAGE_TARGET` &rarr; `54`
- `IMAGE_TSHIRT` &rarr; `55`
- `IMAGE_ROLLERSKATE` &rarr; `56`
- `IMAGE_DUCK` &rarr; `57`
- `IMAGE_HOUSE` &rarr; `58`
- `IMAGE_TORTOISE` &rarr; `59`
- `IMAGE_BUTTERFLY` &rarr; `60`
- `IMAGE_STICKFIGURE` &rarr; `61`
- `IMAGE_GHOST` &rarr; `62`
- `IMAGE_SWORD` &rarr; `63`
- `IMAGE_GIRAFFE` &rarr; `64`
- `IMAGE_SKULL` &rarr; `65`
- `IMAGE_UMBRELLA` &rarr; `66`
- `IMAGE_SNAKE` &rarr; `67`

### Motion Sensor

To use the Motion Sensor module, add the following import statement to your project:

```{code-block} python
:linenos:
from hub import motion_sensor
```

All functions in the module should be called inside the motion_sensor module as a prefix like so:

```{code-block} python
:linenos:
motion_sensor.up_face()
```

#### motion_sensor.acceleration

`acceleration(raw_unfiltered: bool) -> tuple[int, int, int]`

Returns a tuple containing x, y & z acceleration values as integers. The values are in mg (0.001 g)

- `raw_unfiltered: bool` &rarr; If we want the data back raw and unfiltered

#### motion_sensor.angular_velocity

`angular_velocity(raw_unfiltered: bool) -> tuple[int, int, int]`

Returns a tuple containing x, y & z angular velocity values as integers. The values are decidegrees per second

- `raw_unfiltered: bool` &rarr; If we want the data back raw and unfiltered

#### motion_sensor.gesture

`gesture() -> int`

Returns the gesture recognised.

Possible values are:

- `motion_sensor.TAPPED`
- `motion_sensor.DOUBLE_TAPPED`
- `motion_sensor.SHAKEN`
- `motion_sensor.FALLING`
- `motion_sensor.UNKNOWN`

#### motion_sensor.get_yaw_face

`get_yaw_face() -> int`

Retrieve the face of the hub that yaw is relative to.
If you put the hub on a flat surface with the face returned pointing up, when you rotate the hub only the yaw will update

- `motion_sensor.TOP` &rarr; The SPIKE Prime hub face with the USB charging port.
- `motion_sensor.FRONT` &rarr; The SPIKE Prime hub face with the Light Matrix.
- `motion_sensor.RIGHT` &rarr; The right side of the SPIKE Prime hub when facing the front hub face.
- `motion_sensor.BOTTOM` &rarr; The side of the SPIKE Prime hub where the battery is.
- `motion_sensor.BACK` &rarr; The SPIKE Prime hub face where the speaker is.
- `motion_sensor.LEFT` &rarr; The left side of the SPIKE Prime hub when facing the front hub face.

#### motion_sensor.quaternion

`quaternion() -> tuple[float, float, float, float]`

Returns the hub orientation quaternion as a tuple[w: float, x: float, y: float, z: float].

#### motion_sensor.reset_tap_count

`reset_tap_count() -> None`

Reset the tap count returned by the `tap_count` function

#### motion_sensor.reset_yaw_angle

`reset_yaw_angle(angle: int) -> None`

Change the yaw angle offset. The angle set will be the new yaw value.

- `angle: int`

#### motion_sensor.set_yaw_face

`set_yaw_face(up: int) -> bool`

Change what hub face is used as the yaw face. If you put the hub on a flat surface with this face pointing up, when you rotate the hub only the yaw will update

- `up: int` &rarr; The hub face that should be set as the upwards facing hub face.

Available values are:

- `motion_sensor.TOP` &rarr; The SPIKE Prime hub face with the USB charging port.
- `motion_sensor.FRONT` &rarr; The SPIKE Prime hub face with the Light Matrix.
- `motion_sensor.RIGHT` &rarr; The right side of the SPIKE Prime hub when facing the front hub face.
- `motion_sensor.BOTTOM` &rarr; The side of the SPIKE Prime hub where the battery is.
- `motion_sensor.BACK` &rarr; The SPIKE Prime hub face where the speaker is.
- `motion_sensor.LEFT` &rarr; The left side of the SPIKE Prime hub when facing the front hub face.

#### motion_sensor.stable

`stable() -> bool` &rarr; Whether or not the hub is resting flat.

#### motion_sensor.tap_count

`tap_count() -> int`

Returns the number of taps recognised since the program started or last time `motion_sensor.reset_tap_count()` was called.

#### motion_sensor.tilt_angles

`tilt_angles() -> tuple[int, int, int]`

Returns a tuple containing yaw pitch and roll values as integers. Values are decidegrees

#### motion_sensor.up_face

`up_face() -> int`

Returns the Hub face that is currently facing up:

- `motion_sensor.TOP` &rarr; The SPIKE Prime hub face with the USB charging port.
- `motion_sensor.FRONT` &rarr; The SPIKE Prime hub face with the Light Matrix.
- `motion_sensor.RIGHT` &rarr; The right side of the SPIKE Prime hub when facing the front hub face.
- `motion_sensor.BOTTOM` &rarr; The side of the SPIKE Prime hub where the battery is.
- `motion_sensor.BACK` &rarr; The SPIKE Prime hub face where the speaker is.
- `motion_sensor.LEFT` &rarr; The left side of the SPIKE Prime hub when facing the front hub face.

#### motion_sensors.constants

- `TAPPED` &rarr; `0`
- `DOUBLE_TAPPED` &rarr; `1`
- `SHAKEN` &rarr; `2`
- `FALLING` &rarr; `3`
- `UNKNOWN` &rarr; `-1`
- `TOP` &rarr; `0` - The SPIKE Prime hub face with the Light Matrix.
- `FRONT` &rarr; `1` - The SPIKE Prime hub face where the speaker is.
- `RIGHT` &rarr; `2` - The right side of the SPIKE Prime hub when facing the front hub face.
- `BOTTOM` &rarr; `3` - The side of the SPIKE Prime hub where the battery is.
- `BACK` &rarr; `4` - The SPIKE Prime hub face with the USB charging port.
- `LEFT` &rarr; `5` - The left side of the SPIKE Prime hub when facing the front hub face.

### Port

This module contains constants that enables easy access to the ports on the SPIKE Prime hub. Use the constants in all functions that take a `port` parameter.

To use the `port` module, add the following import statement to your project:

```{code-block} python
:linenos:
from hub import port
```

All functions in the module should be called inside the `port` module as a prefix like so:

```{code-block} python
:linenos:
port.A
```

#### port.constants

- `A` &rarr; `0` - The Port that is labelled **A** on the Hub.
- `B` &rarr; `1` - The Port that is labelled **B** on the Hub.
- `C` &rarr; `2` - The Port that is labelled **C** on the Hub.
- `D` &rarr; `3` - The Port that is labelled **D** on the Hub.
- `E` &rarr; `4` - The Port that is labelled **E** on the Hub.
- `F` &rarr; `5` - The Port that is labelled **F** on the Hub.

### hub.device_uuid

`device_uuid() -> str`

Retrieve the device ID.

### hub.hardware_id

`hardware_id() -> str`

Retrieve the hardware ID.

### hub.power_off

`power_off() -> int`

Turns off the hub.

### hub.temperature

`temperature() -> int`

Retrieve the hub temperature. Measured in decidegrees Celsius (d°C) which is 1/10 of a degree Celsius (°C)
