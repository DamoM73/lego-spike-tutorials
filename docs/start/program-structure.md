# Program Structure

!!! learn "On this page we will learn"
    - what event-driven programming is
    - why every program has a setup section and a main loop
    - how to organise a program into input, process and output

!!! terms "Terminology"
    - **setup** – the first part of a program, which runs only once and prepares the hub, motors, sensors and variables for the main loop.
    - **main loop** – the part of a program that runs over and over, waiting for events and reacting to them until the program is stopped.
    - **event-driven programming** – a style of programming where the program keeps checking for things to happen and then responds to them.
    - **event** – something that happens which the program needs to respond to, such as a button being pressed, which the main loop listens for and then handles.
    - **while loop** – a loop that repeats the indented lines under it while its condition is true, so `while True:` repeats forever.
    - **import** – to bring commands from a code library into our program so we can use them, such as the Pybricks commands for the hub and motors.
    - **millisecond** – one thousandth of a second, so 1000 ms is 1 second.
    - **comment** – a line starting with `#` that Python ignores, which we use to label and explain parts of our program.
    - **input** – information the program gathers from the world, such as which buttons are pressed or what a sensor reads.
    - **process** – the part of a program that decides what to do with the input information.
    - **output** – the action a program takes based on its decision, such as changing a light or moving a motor.
    - **indentation** – the spaces at the start of a line, which Python uses to decide which lines belong inside a loop or an `if`.

Every robot program on this site has the same structure: a **setup** section that runs once, followed by a **main loop** that runs over and over. Once we know this structure, we can read any example and know where to add our own code.

## Event-driven programming

Robots need to respond to the world around them. A robot doesn't know when a button will be pressed or when a wall will appear in front of it, so it has to keep checking. This style of programming is called **event-driven programming**. It has two phases:

- **Setup** → prepares the robot for the main loop. It creates the hub, motors and sensors, and any variables the main loop will use. Setup **only runs once**.
- **Main loop** → where the robot waits for things to happen and then reacts to them. We say the robot **listens for events** and then **handles** them. The main loop keeps running until we stop the program.

!!! tip "The party analogy"
    Think of event-driven programming like holding a birthday party.

    First we set everything up. We buy the food and drinks, decorate the room and make a playlist. Each of these is done once. This is the **setup** phase.

    Once we're ready to party, we enter the **main loop**. We wait for things to happen (listen for events) and respond when they do (handle events):

    - the first guest arrives (event) → we welcome them (handle)
    - they give us a gift (event) → we open it (handle)
    - we feel thirsty (event) → we pour a drink (handle)
    - the cake arrives (event) → everyone sings happy birthday (handle)

## Setup and main loop

In Python, the main loop is a `while True:` loop. `True` is always true, so the loop never ends on its own. Everything indented under `while True:` is repeated.

```python linenums="1"
--8<-- "examples/start/program_structure/setup_and_loop/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 9** → plays one beep from the hub speaker.
    - **line 12** → starts the main loop, which repeats forever.
    - **line 13** → turns the status light green.
    - **line 14** → waits 500 milliseconds (half a second).
    - **line 15** → turns the status light off.
    - **line 16** → waits another 500 milliseconds before the loop starts again.

!!! tip "Comments"
    Lines starting with `#` are **comments**. Python ignores them. We use `# Setup` and `# Main loop` to label each part of our program.

## Input, process, output

Inside the main loop, most robot programs do three things, in order:

- **Input** → gather information, such as which buttons are pressed or what a sensor reads.
- **Process** → decide what to do with that information.
- **Output** → act on the decision, such as changing a light or moving a motor.

In larger programs we label these parts with `# Input`, `# Process` and `# Output` comments.

```python linenums="1"
--8<-- "examples/start/program_structure/input_process_output/main.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen. Be specific.
    2. **Run** the program. Press and hold the hub's left button, then let it go.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–5** → import the Pybricks commands for the hub, motors, sensors, settings and timing.
    - **line 8** → creates the hub and names it `hub`.
    - **line 11** → starts the main loop, which repeats forever.
    - **line 13** → gets the buttons that are being pressed right now and stores them in `pressed`.
    - **line 16** → checks if the left button is one of the pressed buttons…
    - **line 17** → …if it is, stores red in `colour`.
    - **line 18** → if it isn't…
    - **line 19** → …stores green in `colour`.
    - **line 22** → turns the status light on in the colour stored in `colour`.

!!! warning "Indentation matters"
    Python uses **indentation** (the spaces at the start of a line) to decide which lines belong inside the loop or the `if`. If a line isn't indented under `while True:`, it isn't part of the main loop.

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Starter files are in the `program_structure` folder of your tutorial files. Solutions are on the [Exercise Solutions](../reference/solutions.md#program-structure) page.

### Exercise 1

Starter: `program_structure/ex1_move_to_setup`

What happens if we move `hub.speaker.beep()` into the main loop? Why do you think this happens?

### Exercise 2

Starter: `program_structure/ex2_right_button`

Can you change the program so the status light turns blue while the right button is pressed? The left button should still turn it red.

### Exercise 3

Starter: `program_structure/ex3_traffic_light`

Can you create a traffic light program? It should:

- beep once when the program starts
- turn the status light green for 3 seconds
- turn it yellow for 1 second
- turn it red for 3 seconds
- repeat the green, yellow and red lights forever
