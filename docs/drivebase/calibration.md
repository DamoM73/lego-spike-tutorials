# Calibration

!!! learn "On this page we will learn"
    - why a drive base needs calibrating
    - how to calibrate the wheel diameter
    - how to calibrate the axle track
    - how to record the calibrated values

!!! terms "Terminology"
    - **calibration** – testing a device and adjusting its settings until its movements or measurements are accurate.

The `wheel_diameter` and `axle_track` values in our drive base were measured with a ruler, so they are only close. **Calibration** means testing the robot and adjusting these values until it drives and turns accurately.

## Why calibrate?

- Rubber tyres squash a little under the robot's weight, so the wheels act slightly smaller than they measure.
- Axles bend a little under load, so the wheels touch the ground slightly closer together than they measure.
- A small error adds up. If the robot is 2% short on every 1 metre drive, it is 10 cm short after 5 metres.

## What we need

- our robot
- a tape measure or metre ruler
- masking tape to mark a start line
- a clear floor space of at least 1.2 metres

## The calibration program

Create a new file called `calibration.py` and run the code below.

- Press the **left button** to drive 1000 mm straight.
- Press the **right button** to turn 360° on the spot.

```python linenums="1"
--8<-- "examples/drivebase/calibration/calibrate/main.py"
```

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → creates the left motor in Port E, with anticlockwise as its positive direction.
    - **line 10** → creates the right motor in Port F, with clockwise as its positive direction.
    - **line 11** → joins the two motors into a drive base called `my_robot`, using the values we are testing.
    - **line 14** → starts the main loop, which repeats forever.
    - **line 15** → gets the buttons being pressed and stores them in `pressed`.
    - **line 16** → checks if the left button is pressed…
    - **line 17** → …waits half a second so our hand is clear of the robot…
    - **line 18** → …then drives straight for 1000 mm.
    - **line 19** → otherwise, checks if the right button is pressed…
    - **line 20** → …waits half a second…
    - **line 21** → …then turns the robot 360° to the right.

## Step 1: Calibrate the wheel diameter

Always calibrate the wheel diameter first, because it also affects turning.

1. Put a strip of masking tape on the floor as a start line, and line up the front of the robot with it.
2. Press the **left button**.
    - The robot drives forwards 1000 mm and stops.
3. Measure how far the front of the robot actually travelled.
4. Change `wheel_diameter` on line 11:
    - if the robot didn't go far enough → **decrease** `wheel_diameter` slightly, such as from `56` to `55.5`
    - if the robot went too far → **increase** `wheel_diameter` slightly
5. Repeat until the robot stops within about 5 mm of 1000 mm.

## Step 2: Calibrate the axle track

1. Put a small piece of tape on the floor to mark where the front of the robot is pointing.
2. Press the **right button**.
    - The robot turns one full circle and stops.
3. Check where the robot is pointing now.
4. Change `axle_track` on line 11:
    - if the robot didn't turn far enough → **increase** `axle_track` slightly, such as from `80` to `81`
    - if the robot turned too far → **decrease** `axle_track` slightly
5. Repeat until the robot finishes pointing at the tape.

!!! tip "Test on the surface we'll use"
    Tyres grip carpet, tables and competition mats differently. Calibrate on the surface the robot will drive on.

## Step 3: Record the values

!!! warning "Write them down"
    Record your calibrated `wheel_diameter` and `axle_track` values. Use them in the `DriveBase` line of every program for this robot from now on.

Test both the straight drive and the turn one last time with the final values, because changing one value can slightly change the other result.
