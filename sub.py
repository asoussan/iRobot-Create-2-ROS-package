#!/usr/bin/env python
import rospy

from std_msgs.msg import Int32
# define the display text
def callback(data):
    rospy.loginfo("I receive %s", data.data)

# define the subscriber
def ir_sub():
    rospy.init_node('ir_sub')
    rospy.Subscriber('ir_val')
    rospy.spin()

if __name__=='__main__':
    ir_sub()
