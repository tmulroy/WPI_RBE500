#!/usr/bin/env python
import math
import rospy
from sensor_msgs.msg import JointState

def callback(q):

    rospy.loginfo(rospy.get_caller_id() + "I heard ----- %s", q)
    theta1 = q.q1
    theta2 = q.q2
    d3 = q.q3

    fk = [[],
    [],
    [],
    [0,0,0,1]]

    orientation = [
        [ fk[0][0],fk[0][1],fk[0][2] ],
        [ fk[1][0],fk[1][1],fk[1][2] ],
        [ fk[0][0],fk[0][1],fk[0][2] ]
    ]

    position = [
        [ fk[0][3] ],
        [ fk[1][3] ],
        [ fk[2][3] ]
    ]

    # print entire forward kinematics transformation matrix
    print(f'\nFORWARD KINEMATICS TRANSFORMATION MATRIX: \n \n{fk[0]} \n {fk[1]} \n {fk[3]} \n')

    # print orientation
    print(f'ORIENTATION: \n \n {orientation[0]} \n {orientation[1]} \n {orientation[2]} \n')

    # print position
    print(f'POSITION: \n \n {position[0]} \n {position[1]} \n {position[2]}')

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/joint_states", JointState, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
