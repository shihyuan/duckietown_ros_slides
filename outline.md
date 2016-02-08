
# Intro

## What is ROS?
http://wiki.ros.org/ROS/Introduction

## Why ROS?
* open-source
* active community with 3000+ packages
    - Drivers for sensor
    - Modern algorithms/capabilities
* python for accessibility, C++ for performance
* Well thoughtout inframestructure and extensive documentation/examples 
* Doesn't support windows (which is a pro)

## Concepts Overview
http://wiki.ros.org/ROS/Concepts
* Packages
* Nodes
* Messages
* Master and Communication
* Parameter Server
* Topics
* Services
* Bags

## Packages
http://wiki.ros.org/Packages
Organization tool
* Dependency during build and run time
* Modularity
* Avoid namespace conflict

Structure (Folders)
* Folders (Shoow tree)
    - src
    - script
    - include
    - launch
    - msg
    - srv
* Files
    - CMakeList.txt (For build, python need this too)
    - package.xml (For dependency and build order)

Tools
* rospack profile
* roscd
* rospkg
* catkin_create_pkg

Example
* roscd duckietown

## Nodes and Topics
http://wiki.ros.org/Nodes
http://wiki.ros.org/Topics

Nodes and Topics
* Each node has it's own processes
* Communicate with each other through publishing/subscribing to topics
* Example: Part of the ROS diagram
* Nodes can be run on different machines
    - Figures
* There can be multiple nodes of the same type, but their names have to be unique. (More on this later in the namespaces)
* Topic Types (Message)

Commandline Tools and Demos
* rosrun
    - commandline remapping
    - Can be done in launch file to save a lot of typing
* rosnode list
* rosnode info
* rostopic list
* rostopic info 
* rqt_graph

Best practice and code snippet
* rospy.subscriber with the ~
* rospy.publisher with the ~
    - Do we need to edit the source code all the time? No, we do remapping at launch time.
    - Might not be a big deal for python, but imagine having to recompile everytime the name of a topic changes.
* rospy.init
* rospy.spin
* code organization

## Master
http://wiki.ros.org/Master
* Think of it as telephone operators in the old days.
    - Picture
* One major difference from the operator analogy: the traffic does not go through the master once publisher and subscribers are connected.
    - Node A publishing topic_a
    - Node B want to subscribe to topic_a, it asks the ROS Master for the dedicated address of Node A and topic_a
    - Node B and Node A then communicates directly through TCP/IP (UDP optioins available too).
    - Master sit back and relax

Commandline tools and demos
* roscore
* ROS_MASTER_URI
* ros_out?

## Messages
http://wiki.ros.org/msg
Messages define topic types with a straight-forward syntax.
A topic must have a message type associate with it.
* Common msg types: bool, string, float etc.
* std_msgs, geometry_msgs, nav_msgs, etc
* Header is important.
    - timestamp
    - frame_id
* duckietown_msgs
    - All non standard msgs use in Duckietown are in duckietown_msgs
    - Use composition of existing msgs instead of creating a new one from scratch
    - Example: WheelsCmdStamped.msg?

Commandline tools
* rosmsg show

## Launch Files
Node and Topic Namespaces
* Avoid leading `/` at all cost

Think of them as ROS specific scripts

* tags
    - node
    - launch
    - group
    - arg
    - if and unless

Node
* attributes
    - pkg
    - name
    - ns
    - machine
    - output
* elements
    - remap
    - rosparam
    - param


## Duckietown ROS Diagram

### Perception

### Control

### Localization

### Planning & Coordination



## Duckietown Guidelines
Too much details at this point I think.

### Config?
* In duckietown/config/config_name/pkg_name/node_name/param_file_name.yaml
    - You can easily backup a configuration for all nodes by copying the `config_name` folder
* The name of a node must ends with `_node`.
* Each node should have a launch file with the same name. This launch file is referred to as the elemental launch file.
* 