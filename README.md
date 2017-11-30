# iRobot Create 2 ROS package

The following python code allows the user to obtain a distance reading from the six IR sensors located on the front bumper of the iRobot Create 2. This ROS code is meant to be run on the Raspberry Pi 3 and be connected to the iRobot via serial port. It is essential to download the *pycreate2* package below in order for the pub/sub to work properly.


## Intro
Things needed before starting:

iRobot Create 2:
http://www.irobot.com/About-iRobot/STEM/Create-2.aspx

Raspberry Pi 3:
https://www.amazon.com/CanaKit-Raspberry-Complete-Starter-Kit/dp/B01C6Q2GSY

=> flash fresh image of Ubuntu 16.04 LTS

ROS Kinetic:
http://wiki.ros.org/Installation/UbuntuARM

**Also visit http://wiki.ros.org for all things ROS related - like setting up packages and workspace**

Pycreate2 Python Package: 
https://pypi.python.org/pypi/pycreate2

**Be sure to run "roscore" so nodes can communicate through master!**

Be sure to set these environment variables by adding the following to .bashrc:
export ROS_MASTER_URI=http://<ip_address>:11311
export ROS_IP=<ip_address>
source ./.bashrc

## ROS

### **Initialize Workspace**
In order to set up the workspace, the following commands should be typed into the terminal:
mkdir ~/irobot/src
cd ~/irobot/src
catkin_init_workspace
cd ..
catkin_make
source /devel/setup.bash

### **Create Package**
In order to create the package, the following commands should be typed into the terminal:
cd ~/irobot/src
git clone https://github.com/asoussan/iRobot-Create-2-ROS-package
cd ~/irobot
rosdep update
rosdep install --from-path src -i -y
catkin_make
source /devel/setup.bash

### **Publisher (ir_pub)**
The publisher initializes the node and defines the frequency of the message. The serial port of the Raspberry Pi is defined here as well as the baud rate. This progran also starts the iRobot and sets it to __full__ mode. A value indicating the distance of an object from each sensor in a 1x6 array is the message. The sensor sate is initialized to [0,0,0,0,0,0] when nothing is obstructing, but a higher value indicates an object is closer. Until the program is shut down, each sensor state will continuously update at a given frequency.

Once the rosmaster is launched, we can run the publisher in a separate window by entering:
rosrun iRobot-Create-2-ROS-package pub.py

The terminal should display the values from each sensor at a given frequency.

### **Subscriber (ir_sub)**
The subscriber indicates which message the program will subscribe, in this case, *ir_val* is the message from the publisher. This program allows us to obtain the data from the six IR sensors in order to be used for other tasks, such as controlling the motor speeed for navigation. The result of the subscriber should be similar to that of the publisher, and output "I receive [0,0,0,0,0,0]" when nothing is obstructing the iRobot.

Similar to the publisher, we will run the subscriber in a separate window by entering:
rosrun iRobot-Create-2-ROS-package sub.py

The publisher and subscriber should be placed into the same package.
