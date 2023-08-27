# Hub Outputs

```{topic} In this lesson you will:
- the output features on the Spike Prime Hub
```

```{admonition} Pybrick Documentation
:class: important
To explore all Pybricks' features check the **[Pybricks documentaion](https://docs.pybricks.com/en/stable/index.html)**. This can also be seen in the right-hand panel of the Pybricks IDE.
```

The Spike Prime Hub has many features that can be used to produce output for the robot.

```{admonition} Output and Input
:class: note
Imagine that you want the robot to explore a room all by itself. When the robot uses its sensors to see if there are obstacles ahead and decides to turn left, that's the **input**. It's like the robot figuring out what's around it. 

Then, when the robot actually turns and goes in the new direction, that's the **output**. It's the robot taking action based on what it learned from its sensors. 

So, input is when the robot gathers information, and output is the robot using that information to make decisions and move around. It's like the robot's way of thinking and moving on its own!
```

## The Hub Status Light

The Hub Status Light is around the Power button and it is blue by default.

![Hub Status Light](assets/primehub_light.png)

Pybricks has four commands for the status light:

- **[`light.on(color)`](https://docs.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.light.on)** &rarr; Turns on the light at the specified colour.
- **[`light.off()`](https://docs.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.light.off)** &rarr; Turns off the light.
- **[`light.blink(color, durations)`](https://docs.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.light.blink)** &rarr; Blinks the light at a given colour by turning it on and off for given durations.
- **[`light.animate(colors, interval)`](https://docs.pybricks.com/en/stable/hubs/primehub.html#pybricks.hubs.PrimeHub.light.animate)** &rarr; Animates the light with a sequence of colours, shown one by one for the given interval.

```{admonition} PRIMM
Throughout this course we will use the **PRIMM** process to reinforce our learning. **PRIMM** stands for **Predict**, **Run**, **Investigate**, **Modify**, and **Make**. It reflects effective programming practices and encourages curiosity in programming.

**Predict**: Before you run the code you need to predict what you think will happen. Go ahead and have a guess at what you think will happen.

**Run**: Then run the program and see how accurate your prediction was. If your prediction was incorrect, how was the result different?

**Investigate**: Go through the code and work out what each line of code does.

**Modify**: Edit the code. Change it around and see that results your get

**Make**: Use your new understanding of the code to make a different program.
```

You will now use all four status light command:

1. **Create** a new file called `hub_light.py`
2. **Type** the code below into the file
3. **Predict** what you think will happen.
4. **Run** your code

```{literalinclude} ./python_files/hub_output_status_light.py
:linenos:
```

Time to **investigate** the code:

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

Try **modifying** the code:

- can you display different colours?
- can you change the timing of the blink?
- can you change the timing of the animation?
- what happens when you comment out (put a `#` in front) all the `wait` commands?
- 