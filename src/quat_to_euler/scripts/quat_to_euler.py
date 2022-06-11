#!/usr/bin/env python
import math
import rospy
from geometry_msgs.msg import Quaternion

def callback(q):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", q)

    # roll (x-axis-rotation)
    sinr_cosp = 2 * (q.w * q.x + q.y * q.z)
    cosr_cosp = 1 - 2 * (q.x * q.x + q.y * q.y)
    roll = math.atan2(sinr_cosp, cosr_cosp)

    # pitch (y-axis rotation)
    sinp = 2 * (q.w * q.y - q.z * q.z)
    if abs(sinp) >= 1:
        pitch = math.copysign(pi/2,sinp)
    else:
        pitch = math.asin(sinp)

    # yaw (z-axis rotation)
    siny_cosp = 2 * (q.w * q.z + q.x * q.y)
    cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
    yaw = math.atan2(siny_cosp, cosy_cosp)

    rospy.loginfo(f'{rospy.get_caller_id()} Euler Angles are: \n \u03A8 (roll): {roll} \n \u03F4 (pitch): {pitch} \n \u03A8 (yaw): {yaw}')

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("quat_convert", Quaternion, callback)


    rospy.spin()

if __name__ == '__main__':
    listener()
