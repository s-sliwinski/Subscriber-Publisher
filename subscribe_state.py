#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState

def callback(data):
    print data.position

def state():

    rospy.init_node('jointState', anonymous=True)

    rospy.Subscriber("/joint_states", JointState, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    state()
