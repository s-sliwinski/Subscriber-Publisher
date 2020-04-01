#!/usr/bin/env python
import rospy
from std_msgs.msg import String

seed = True

def getcommand():
    global seed
    if seed:
        seed = False
        return "moveRight"

    else:
        seed = True
        return "moveLeft"


def controller():
    pub = rospy.Publisher('/arm_controller/order', String, queue_size=10)
    rospy.init_node('armControl', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        command = getcommand()
        print command
        pub.publish(command)
        rate.sleep()

if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInterruptException:
        pass
