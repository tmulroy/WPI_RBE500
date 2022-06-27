#!/usr/bin/env python3
import math
import rospy
from fk.msg import JointVariables

def callback(q):

    rospy.loginfo(rospy.get_caller_id() + "I heard ----- %s", q)
    theta1 = q.q1
    theta2 = q.q2
    theta3 = q.q3
    theta4 = q.q4
    theta5 = q.q5
    theta6 = q.q5

    fk = [[
       math.sin(theta6)*(math.cos(theta4 + math.pi/2)*math.sin(theta1) + math.sin(theta4 + math.pi/2)*(math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2))) + math.cos(theta6)*(math.cos(theta5)*(math.sin(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2))) + math.sin(theta5)*(math.cos(theta4 + math.pi/2)*math.sin(theta1) + math.cos(theta1)*math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta1)*math.cos(theta2 + math.pi/2)*math.sin(theta3))), math.cos(theta6)*(math.cos(theta4 + math.pi/2)*math.sin(theta1) + math.sin(theta4 + math.pi/2)*(math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2))) - math.sin(theta6)*(math.cos(theta5)*(math.sin(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2))) + math.sin(theta5)*(math.cos(theta4 + math.pi/2)*math.sin(theta1) + math.cos(theta1)*math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta1)*math.cos(theta2 + math.pi/2)*math.sin(theta3))), math.sin(theta5)*(math.sin(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2))) + math.cos(theta5)*(math.cos(theta4 + math.pi/2)*math.sin(theta1) + math.cos(theta1)*math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta1)*math.cos(theta2 + math.pi/2)*math.sin(theta3)),
       150*math.cos(theta1) + 600*math.cos(theta1)*math.cos(theta2 + math.pi/2) + 85*math.sin(theta5)*(math.sin(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) -math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2))) + 85*math.cos(theta5)*(math.cos(theta4 + math.pi/2)*math.sin(theta1) + math.cos(theta1)*math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta1)*math.cos(theta2 + math.pi/2)*math.sin(theta3)) - 120*math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) + 120*math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2)
    ],
    [
       -math.cos(theta6)*(math.cos(theta5)*(math.cos(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2))) - math.sin(theta5)*(math.cos(theta3)*math.sin(theta1)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta4 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta1)*math.sin(theta3))) - math.sin(theta6)*(math.cos(theta1)*math.cos(theta4 + math.pi/2) + math.sin(theta4 + math.pi/2)*(math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2))), math.sin(theta6)*(math.cos(theta5)*(math.cos(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2))) - math.sin(theta5)*(math.cos(theta3)*math.sin(theta1)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta4 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta1)*math.sin(theta3))) - math.cos(theta6)*(math.cos(theta1)*math.cos(theta4 + math.pi/2) + math.sin(theta4 + math.pi/2)*(math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2))), math.cos(theta5)*(math.cos(theta3)*math.sin(theta1)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta4 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta1)*math.sin(theta3)) - math.sin(theta5)*(math.cos(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2))),
       150*math.sin(theta1) + 600*math.cos(theta2 + math.pi/2)*math.sin(theta1) - 85*math.sin(theta5)*(math.cos(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2))) + 85*math.cos(theta5)*(math.cos(theta3)*math.sin(theta1)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta4 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta1)*math.sin(theta3)) + 120*math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - 120*math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2)
    ],
    [
       - math.cos(theta6)*(math.sin(theta5)*(math.cos(theta3)*math.cos(theta2 + math.pi/2) - math.sin(theta3)*math.sin(theta2 + math.pi/2)) - math.cos(theta5)*math.cos(theta4 + math.pi/2)*(math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta3))) - math.sin(theta6)*math.sin(theta4 + math.pi/2)*(math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta3)),                                                                                                                                                                                math.sin(theta6)*(math.sin(theta5)*(math.cos(theta3)*math.cos(theta2 + math.pi/2) - math.sin(theta3)*math.sin(theta2 + math.pi/2)) - math.cos(theta5)*math.cos(theta4 + math.pi/2)*(math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta3))) - math.cos(theta6)*math.sin(theta4 + math.pi/2)*(math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta3)),
       math.cos(theta4 + math.pi/2)*math.sin(theta5)*(math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta3)) - math.cos(theta5)*(math.cos(theta3)*math.cos(theta2 + math.pi/2) - math.sin(theta3)*math.sin(theta2 + math.pi/2)),                                                                                                                                                                     600*math.sin(theta2 + math.pi/2) + 120*math.cos(theta3)*math.sin(theta2 + math.pi/2) + 120*math.cos(theta2 + math.pi/2)*math.sin(theta3) - 85*math.cos(theta5)*(math.cos(theta3)*math.cos(theta2 + math.pi/2) - math.sin(theta3)*math.sin(theta2 + math.pi/2)) + 85*math.cos(theta4 + math.pi/2)*math.sin(theta5)*(math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta3)) + 475
    ],
    [0,0,0,1]
    ]

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

    rospy.Subscriber("forward_kinematics", JointVariables, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
