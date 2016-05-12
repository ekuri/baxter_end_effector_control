# ROS End Effector Control Package for Baxter

## About
To know what this package is, pleased refer to the [wiki](https://github.com/ekuri/baxter_end_effector_control/wiki) of this package:

## Build and Run

### Environment
To successfully build this package, the following library of C++ is required:
* stdc++
* boost

### Denpendency
The following package of ROS is required:
* roscpp
* rospy
* tf
* geometry_msgs
* visualization_msgs
* interactive_markers
* [trac_ik](https://bitbucket.org/traclabs/trac_ik.git)

To auto-fix the dependencies, you can try ```rosdep install --from-paths src --ignore-src --rosdistro indigo -y``` under the root directory of workspace that contain this package

### Build Package
Simply run ```catkin_make``` under the root directory of workspace that contain this package

### Run
#### Common
Run following command before any control type lists bellow:
>```roslaunch baxter_end_effector_control end_effector_control.launch```

Add argument: ```rviz:true``` to enable visualization, ```debug_output:true``` to enable debug output, ```solver:=kdl``` to use kdl ik solver

###### marker control
>```rosrun baxter_end_effector_control end_effector_marker_control```

###### keyboard control
> ```rosrun baxter_end_effector_control end_effector_keyboard_control.py```
