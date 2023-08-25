# Introduction

```{topic} In this lesson you will:
- install our IDE - Lego Spike App 3
- learn how to create Python files for the robot
- use the app to connect to your robot using Bluetooth
- check that your robot is configured correctly
- write and run your first Spike Prime program
```

![Spike Logo](assets/spike_logo.png)

## Install Spike App 3

You will be using the Lego Spike App 3 to program our robot, so the first thing you need to do is install the App.

To do this:

- go to the [LEGO Education SPIKE App download](https://education.lego.com/en-au/downloads/spike-app/software/)
- choose your operating system (Windows 11 users choose Windows 10)
- click the **Download** button
- run the downloaded file and keep clicking **next** to install the app
- when the app is installed it should automatically start

## Creating Python Files

Once we are in the app, there are a few steps to accessing the Python coding environment.

1. In the **Select you Spike solution** page, choose the **Spike Prime** option.
2. There are some steps you will only need to do the first time
   1. Click **Got it** on the next screen
   2. Click **DON'T SHOW ME THIS AGAIN** on the next screen, then click the **X**
   3. Click the settings cog icon ![cog icon](assets/setting.png) at the bottom lefthand corner of the window.
   4. Choose **General** and then click the **Enable Python projects** toggle.
   5. Finally, click the home icon

![enable python projects](assets/enable_python_projects.png)

3. Click **New Project**
4. Give your project a name (First Program), click Python and then click CREATE

![create new project](assets/create_new_project.png)

5. Finally we will delete all the code that has been prewritten for us. Hold **Ctrl** + **A** (**command** + **A** on macs) and then **delete**.

## Connect to Robot

You will use Bluetooth to connect to your robot. 

1. Click the yellow **Connect** icon in the top left of the screen
2. Turn you robot on by pressing and briefly holding the power button
3. Then click on **Green already updated**

![Green power button](assets/green_power_button.png)

4. Follow the instruction to **turn on Bluetooth**
5. Connect to your robot by choosing it's name from the list

## Check Configuration

Your robot has three sensors modules and two motors modules connected. 

| Module | Port | Purpose | Image |
| --- | --- | --- | --- |
| Ultrasonic Sensor | C | Detect the distance to object in front | ![Ultrasonic Sensor](assets/distance.png) |
| Force Sensor | F | Detect the amount of pressure applied | ![Force Sensor](assets/force.png) |
| Colour Sensor | D | Detect the colour of an object, or the amount of light reflected | ![Colour Sensor](assets/colour.png) |
| Motor | A B | Turns in response to commands from hub | ![Motor Sensor](assets/motor.png)

To successfully follow these tutorials, you need to make sure that they are all connected to the correct hub ports.

To check the port that modules are connected to, look at the top of the screen beside the connection icon. Make sure that each module is connected to the correct port. It should look like the image below.

![module icons](assets/modules_icons.png)

## First Program

Our final check is for you to run your first program.

