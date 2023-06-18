## Setup 
- Please install ros2 humble (use ubuntu version 22.04+)
- ```git clone https://github.com/Siddhu2502/curly-succotash```


Once cloned run 
- ```colcon build --symlink-install```
- ```source install/setup.bash``` (very important!)

Run the launch file
- ```ros2 launch lidar_robot launch_sim.launch.py``` (without world)
- ```ros2 launch lidar_robot launch_sim.launch.py world:=./src/lidar_robot/worlds/buildingworld.world ``` (with the world all in one launch file will be updated later)


## Running the robot and some other stuffs  
- Open 4 terminals and do ```source install/setup.bash``` (be inside the folder)
- Once done in the first terminal run the launch file command 

    - ### Using rviz2 part and playing with rviz 
        - run ```ros2 launch lidar_robot rsp.launch.py``` (in terminal 1)
        - run ```rviz2``` (in terminal 2)
            - please select ```fixed_frame = base_link```
            - Add ```tf and RobotModel```
            - navigate to RobotModel and select ```Description Topic = /robot_description```
        - run ```ros2 run joint_state_publisher_gui joint_state_publisher_gui ``` (in terminal 3)
    
    - ### Using rviz2 part and playing in gazebo
        - run ```ros2 launch lidar_robot launch_sim.launch.py``` (in terminal 1)
        - run ```ros2 run teleop_twist_keyboard_gui teleop_twist_keyboard_gui``` (in terminal 2)

