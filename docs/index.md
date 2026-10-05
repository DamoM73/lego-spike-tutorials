# Lego Spike Python Coding

Short, practical examples for programming the LEGO SPIKE Prime robot in Python using Pybricks.

## How to use this site

1. Start with **Getting Started** to set up Pybricks, connect the robot and learn how every program is structured.
2. Then go to the page for the part of the robot we want to use:
    - **Hub** → the status light, light matrix, speaker, buttons and motion sensor built into the hub
    - **Motors** → controlling one motor at a time, and using a motor as a sensor
    - **Drive Base** → controlling both wheels together to drive and turn the robot
    - **Sensors** → the force, colour and distance sensors
3. **Planning** shows how to plan a robot project with IPO tables, flowcharts and pseudocode.
4. **Reference** has the full example programs, the solutions to every exercise and the licence.

## How each page works

Every hub, motor, drive base and sensor page follows the same layout:

- **Connect it** → which port the device uses and key facts about it
- **Set it up** → the code needed before using the device
- **Methods** → a table of every method, followed by a short example of each
- **Code explanation** → click to open a line-by-line explanation of each example
- **Exercises** → practice tasks, with solutions on the [Exercise Solutions](reference/solutions.md) page

## Callouts

Coloured boxes called **callouts** highlight different kinds of information. Each type of callout has its own colour and icon, so we can tell at a glance what it's for.

!!! learn "Learning intentions"
    This callout is at the top of every tutorial page. It lists what we will learn on that page.

!!! terms "Terminology"
    This callout comes straight after the learning intentions. It lists the new technical terms on the page, with a short definition of each. Every term is also on the [Glossary](reference/glossary.md) page.

!!! primm "PRIMM"
    This callout comes after each example program. It asks us to **predict** what the code will do, **run** it, and **investigate** how it works. Sometimes it asks us to **modify** the code.

!!! note "Code explanation"
    This callout comes after each PRIMM callout and gives a line-by-line explanation of the example program. On the tutorial pages it starts closed, so we can make our own prediction first. Click its title to open it.

!!! tip "Tip"
    This callout gives extra information, such as definitions, background facts, comparisons and hints.

!!! warning "Warning"
    This callout warns us about mistakes that are easy to make, or things that will stop our program or robot working.

## Code blocks

Programs are shown in **code blocks** like this one:

```python linenums="1"
from pybricks.hubs import PrimeHub

hub = PrimeHub()
hub.display.text("Hi")
```

- The **line numbers** on the left match the line numbers used in the Code explanation.
- The **copy** button in the top-right corner of a code block copies the code, so we can paste it into Pybricks.

## Tutorial files

Download all the examples and exercise starter files: [lego_spike_tutorials.zip](downloads/lego_spike_tutorials.zip). See [Setup](start/setup.md#tutorial-files) for how to use them.
