# Glossary

This glossary lists every technical term introduced on this site, in alphabetical order. Each term links to the page where it is first explained, and each page lists its new terms in a Terminology callout at the top.

[A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [Y](#y)

## A

- **algorithm** – a step-by-step method for solving a problem. ([Developing Robot Code](../planning/developing-code.md))
- **ambient light** – the light around the sensor, measured without its own lights, from 0% (dark) to 100% (bright). ([Colour Sensor](../sensors/colour.md))
- **angular motor** – a motor that can turn an exact number of degrees because it has a built-in encoder. ([Motor](../motors/motor.md))
- **arc** – a path that follows part of a circle. ([Driving](../drivebase/driving.md))
- **axis** – an imaginary line that something turns around, such as the x, y and z axes of the hub. ([IMU](../hub/imu.md))
- **axle track** – the distance between where the two wheels touch the ground, in millimetres. ([Driving](../drivebase/driving.md))

## B

- **Boolean** – a value that can only be `True` or `False`. ([Motor as a Sensor](../motors/motor-sensor.md))
- **brightness** – how strongly a light shines, from `0` (off) to `100` (fully on). ([Light Matrix](../hub/light-matrix.md))

## C

- **calibration** – testing a device and adjusting its settings until its movements or measurements are accurate. ([Calibration](../drivebase/calibration.md))
- **character** – a single letter, digit or symbol. ([Light Matrix](../hub/light-matrix.md))
- **coasting** – cutting the power to a motor and letting it spin freely until friction stops it. ([Motor](../motors/motor.md))
- **colour sensor** – a sensor that detects the colour of a surface, how much light it reflects and how bright the room is. ([Colour Sensor](../sensors/colour.md))
- **comment** – a line starting with `#` that Python ignores, which we use to label and explain parts of our program. ([Program Structure](../start/program-structure.md))
- **constant** – a named value that never changes, such as `Color.RED`, which we use instead of typing the value itself. ([Status Light](../hub/status-light.md))
- **coordinate** – a pair of numbers, `(row, column)`, that gives the position of a pixel on the light matrix. ([Light Matrix](../hub/light-matrix.md))

## D

- **DC motor** – a simple motor without an encoder that can only be turned on and off and have its power set. ([Motor](../motors/motor.md))
- **decision block** – a diamond in a flowchart that asks a question and splits the flow depending on the answer. ([Flowcharts](../planning/flowcharts.md))
- **default value** – the value a parameter uses when we don't give one, such as a 500 Hz beep for 100 ms. ([Speaker](../hub/speaker.md))
- **digital system** – a system that takes input from the real world, processes it and produces output, such as our robot. ([Developing Robot Code](../planning/developing-code.md))
- **distance sensor** – an ultrasonic sensor that works out how far away an object is by timing how long the echo of its sound takes to return. ([Distance Sensor](../sensors/distance.md))
- **documentation** – the official guide written by the people who made a code library, which lists every method and its parameters. ([Status Light](../hub/status-light.md))
- **drift** – small errors that add up over time so the robot ends up facing or travelling somewhere different from what we planned. ([Gyro Driving](../drivebase/gyro-driving.md))
- **drive base** – two wheel motors joined together in code so we can drive and turn the whole robot instead of controlling each motor. ([Driving](../drivebase/driving.md))
- **duty cycle** – the percentage of full power sent to a motor, without the motor trying to keep a constant speed. ([Motor](../motors/motor.md))

## E

- **echo** – a sound wave that bounces back off an object. ([Distance Sensor](../sensors/distance.md))
- **encoder** – a sensor built into a motor that counts how many degrees the motor has turned. ([Motor](../motors/motor.md))
- **event** – something that happens which the program needs to respond to, such as a button being pressed, which the main loop listens for and then handles. ([Program Structure](../start/program-structure.md))
- **event-driven programming** – a style of programming where the program keeps checking for things to happen and then responds to them. ([Program Structure](../start/program-structure.md))

## F

- **firmware** – special software built into a device that makes it work correctly every time we turn it on. ([Setup](../start/setup.md))
- **flow arrow** – an arrow in a flowchart that shows the path the program takes, in the direction of the arrowhead. ([Flowcharts](../planning/flowcharts.md))
- **flowchart** – a diagram that uses shapes and arrows to show the steps in a process and the order they happen in. ([Developing Robot Code](../planning/developing-code.md))
- **for loop** – a loop that repeats its indented lines a set number of times, such as 4 times for the sides of a square. ([Gyro Driving](../drivebase/gyro-driving.md))
- **force sensor** – a sensor like a button that can tell whether it is touched or pressed and measure how hard it is pressed. ([Force Sensor](../sensors/force.md))
- **frequency** – how high or low a sound is, where a higher frequency gives a higher pitch. ([Speaker](../hub/speaker.md))
- **function indicator** – a red dashed box in a flowchart that surrounds a function, from its start terminal to its end terminal. ([Flowcharts](../planning/flowcharts.md))

## G

- **gyroscope** – a sensor, often called a gyro, that measures how fast something is turning. ([Gyro Driving](../drivebase/gyro-driving.md))

## H

- **heading** – the direction the hub or robot is facing, measured as how many degrees it has turned around the z-axis. ([IMU](../hub/imu.md))
- **hertz** – the unit (Hz) used to measure frequency. ([Speaker](../hub/speaker.md))
- **hub** – the programmable brick at the centre of the robot that runs our programs and that the motors and sensors plug into. ([Setup](../start/setup.md))

## I

- **IDE** – an Integrated Development Environment, which is an app for writing and running code, such as the Pybricks IDE. ([Setup](../start/setup.md))
- **import** – to bring commands from a code library into our program so we can use them, such as the Pybricks commands for the hub and motors. ([Program Structure](../start/program-structure.md))
- **IMU** – an inertial measurement unit, which is a sensor inside the hub that senses how it is moving and which way it is facing. ([IMU](../hub/imu.md))
- **indentation** – the spaces at the start of a line, which Python uses to decide which lines belong inside a loop or an `if`. ([Program Structure](../start/program-structure.md))
- **inflow** – a flow arrow going into a flowchart block. ([Flowcharts](../planning/flowcharts.md))
- **input** – information the program gathers from the world, such as which buttons are pressed or what a sensor reads. ([Program Structure](../start/program-structure.md))
- **input/output block** – a parallelogram in a flowchart that shows information moving between the program and the real world. ([Flowcharts](../planning/flowcharts.md))
- **IPO table** – an Input, Process, Output table that maps out what a system takes in, what it decides and what it does. ([Developing Robot Code](../planning/developing-code.md))

## L

- **LEGO SPIKE Prime** – the LEGO robotics kit that provides our robot's hardware, including the hub, motors and sensors. ([Setup](../start/setup.md))
- **library** – a collection of ready-made code, such as Pybricks, that we can use in our own programs. ([Status Light](../hub/status-light.md))
- **light matrix** – the 5×5 grid of lights on the front of the hub that can show pixels, icons, numbers and letters. ([Light Matrix](../hub/light-matrix.md))
- **list** – a group of several values kept in order inside square brackets. ([Light Matrix](../hub/light-matrix.md))
- **load** – how hard something is pushing against a motor while it runs, measured in millinewton metres. ([Motor as a Sensor](../motors/motor-sensor.md))
- **loop indicator** – a grey dashed box in a flowchart that surrounds a loop. ([Flowcharts](../planning/flowcharts.md))

## M

- **main loop** – the part of a program that runs over and over, waiting for events and reacting to them until the program is stopped. ([Program Structure](../start/program-structure.md))
- **method** – a command that belongs to an object, such as the hub's light, and makes it do something or tells us about it. ([Status Light](../hub/status-light.md))
- **millisecond** – one thousandth of a second, so 1000 ms is 1 second. ([Program Structure](../start/program-structure.md))

## N

- **newton** – the unit (N) used to measure force, where 1 N is roughly the force of holding a 100 g block of chocolate. ([Force Sensor](../sensors/force.md))

## O

- **object** – a thing in our program, such as a motor or sensor, that we create in the setup and then control with its methods. ([Motor](../motors/motor.md))
- **orientation** – which way something is facing, such as which side of the hub counts as the top of the display. ([Light Matrix](../hub/light-matrix.md))
- **outflow** – a flow arrow coming out of a flowchart block. ([Flowcharts](../planning/flowcharts.md))
- **output** – the action a program takes based on its decision, such as changing a light or moving a motor. ([Program Structure](../start/program-structure.md))

## P

- **parameter** – a value we put inside a method's brackets to tell it exactly what to do, such as which colour to show. ([Status Light](../hub/status-light.md))
- **pitch** – turning around the y-axis, like a plane pointing its nose up or down. ([IMU](../hub/imu.md))
- **pixel** – one single light in the light matrix. ([Light Matrix](../hub/light-matrix.md))
- **placeholder** – code that does nothing, such as `pass`, used to fill a gap until we write the real code. ([Developing Robot Code](../planning/developing-code.md))
- **port** – the socket on the hub that a motor or sensor is plugged into, such as `Port.E`. ([Motor](../motors/motor.md))
- **positive direction** – the way a motor turns when we give it a positive speed, either clockwise or anticlockwise. ([Motor](../motors/motor.md))
- **process** – the part of a program that decides what to do with the input information. ([Program Structure](../start/program-structure.md))
- **process block** – a rectangle in a flowchart that shows a step inside the program, such as a calculation or storing a value. ([Flowcharts](../planning/flowcharts.md))
- **pseudocode** – a plan for our code written in plain words, without worrying about the rules of a programming language. ([Developing Robot Code](../planning/developing-code.md))
- **Pybricks** – the software that runs on the robot, together with the app we use to write programs for it in Python. ([Setup](../start/setup.md))
- **Python** – the text-based programming language we use to write our robot programs. ([Setup](../start/setup.md))

## R

- **radius** – the distance from the centre of a circle to its edge, such as from the centre of an arc to the robot. ([Driving](../drivebase/driving.md))
- **random number** – a number picked by chance, such as a whole number from −180 to 180. ([Developing Robot Code](../planning/developing-code.md))
- **reflected light** – the amount of the sensor's own light that bounces back from a surface, from 0% (black) to 100% (white). ([Colour Sensor](../sensors/colour.md))
- **requirement** – something specific that a system needs to do, such as stopping when an object is within 100 mm. ([Developing Robot Code](../planning/developing-code.md))
- **return value** – a value that a method gives back to our program, such as the current volume. ([Speaker](../hub/speaker.md))
- **roll** – turning around the x-axis, like a plane dipping one wing. ([IMU](../hub/imu.md))
- **running in the background** – carrying on by itself once started while the rest of the program keeps running. ([Status Light](../hub/status-light.md))

## S

- **sensor** – a device that detects something about the world around the robot, such as pressure, distance or colour. ([Setup](../start/setup.md))
- **set** – a group of values with no order, such as the buttons being pressed right now, which is empty when there are none. ([Buttons](../hub/buttons.md))
- **setup** – the first part of a program, which runs only once and prepares the hub, motors, sensors and variables for the main loop. ([Program Structure](../start/program-structure.md))
- **stalling** – when a motor is trying to move but can't, even at full power. ([Motor as a Sensor](../motors/motor-sensor.md))
- **status light** – the coloured light around the hub's power button, which our programs can turn on, blink and cycle through colours. ([Status Light](../hub/status-light.md))
- **string** – a piece of text made up of characters, written inside quotation marks. ([Light Matrix](../hub/light-matrix.md))

## T

- **target angle** – the exact position a motor turns to, measured from where it was when the program started. ([Motor](../motors/motor.md))
- **tempo** – the speed of a tune, measured in beats per minute. ([Speaker](../hub/speaker.md))
- **terminal** – the area at the bottom of the IDE where anything our program prints is shown. ([Setup](../start/setup.md))
- **terminal block** – a rounded rectangle that starts or ends a process in a flowchart. ([Flowcharts](../planning/flowcharts.md))
- **threshold** – a set value that a reading must reach before the program counts it, such as the force needed for a press. ([Force Sensor](../sensors/force.md))
- **tracing** – following a flowchart step by step with test values to check every path works. ([Flowcharts](../planning/flowcharts.md))
- **tuple** – a group of values inside round brackets, such as `(10, -5)`, that a method can return all at once. ([IMU](../hub/imu.md))
- **turn rate** – how fast the robot turns, in degrees per second. ([Driving](../drivebase/driving.md))

## U

- **ultrasound** – sound that is too high-pitched for people to hear. ([Distance Sensor](../sensors/distance.md))

## V

- **variable** – a named place that stores a value our program can use and change, such as a count. ([Light Matrix](../hub/light-matrix.md))
- **volume** – how loud a sound is, from `0` (silent) to `100` (loudest). ([Speaker](../hub/speaker.md))

## W

- **wheel diameter** – the width of a wheel in millimetres, measured straight across through its centre. ([Driving](../drivebase/driving.md))
- **wheel slip** – when the wheels turn without the robot moving the same distance, which makes the drive base's measurements wrong. ([Drive Base as a Sensor](../drivebase/drivebase-sensor.md))
- **while loop** – a loop that repeats the indented lines under it while its condition is true, so `while True:` repeats forever. ([Program Structure](../start/program-structure.md))

## Y

- **yaw** – turning around the z-axis, like a car turning left or right. ([IMU](../hub/imu.md))
