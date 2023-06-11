# Introduction

## What is this?
This is a detailed demo of how we make a ros2 lidar obstacle avoidance robot the package is we used here is ros2 humble. 

## What are the outcomes
- A robot that can avoid obstacles and move around in a room
- A robot that can be controlled by a joystick or keyboard
- A robot that can map the room and save the map (using slam_toolbox)
- A robot that can navigate to a goal point (using nav2)

## What are the hardware requirements
Right now we are going to use only simulatin using gazebo and ros2. So, you don't need any hardware to run this demo. But if you want to run this demo on a real robot, you need the following hardware:
- A lidar sensor (3d lidar is recommended -can get it from iphone)
- A motor controller
- A motor
- A raspberry pi or any other computer to run ros2 (raspberry pi is recommended)
- A joystick (optional)
- A camera (webcam is recommended)

## What are the software requirements
- Ubuntu 22.04
- ros2 humble
- ros2 humble packages 
    - ros2 humble (libgazebo_ros_diff_drive)
    - ros2 humble (libgazebo_ros_laser)
    - ros2 humble (libgazebo_ros_camera)
    - ros2 humble slam_toolbox
    - ros2 humble nav2
    - ros2 humble teleop_twist_keyboard_gui and teleop_twist_joystick_gui

## How to install the software requirements
- Refer to the [installation guide](Ros2_humble_installation.md) to install ros2 humble and its packages
