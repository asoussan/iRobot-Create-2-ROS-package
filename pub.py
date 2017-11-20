#!/usr/bin/env python
from __future__ import print_function
from pycreate2 import Create2
import time
import rospy

def ir_pub():
        rospy.init_node('ir_value')
        pub=rospy.Publisher('ir_val')
        rate=rospy.Rate(1)
        while not rospy.is_shutdown():
           rospy.loginfo(ir_msg)
           pub.publish(ir_msg)
           rate.sleep()

if __name__ == "__main__":
        port = '/dev/ttyUSB0'
        baud = {
                'default': 115200
        }

        bot = Create2(port=port, baud=baud['default'])

        bot.start()

        bot.full()

        sensor_state = [0,0,0,0,0,0]

        print('Starting ...')

        while True:
                # Packet 100 contains all sensor data.
                sensor_state[0] = bot.get_sensors().light_bumper_left
                sensor_state[1] = bot.get_sensors().light_bumper_front_left
                sensor_state[2] = bot.get_sensors().light_bumper_center_left
                sensor_state[3] = bot.get_sensors().light_bumper_center_right
                sensor_state[4] = bot.get_sensors().light_bumper_front_right
                sensor_state[5] = bot.get_sensors().light_bumper_right

                print('==============Updated Sensors==============')
                print(sensor_state)
                time.sleep(2)
