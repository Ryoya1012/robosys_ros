#! /usr/bin/env python3

#SPDX-License-Identifer: GPL-2.0
#*Copyright (c) 2021 Ryoya Sato. All rights resrved.

import rospy
from std_msgs.msg import Int32

n = 1

def cb(message):
    global n
    n = message.data*3

if __name__ == '__main__':
    rospy.init_node('third')
    sub = rospy.Subscriber('twice', Int32, cb)
    pub = rospy.Publisher('third', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
