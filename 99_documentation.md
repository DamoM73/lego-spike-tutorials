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
