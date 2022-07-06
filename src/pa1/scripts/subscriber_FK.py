#!/usr/bin/env python
# Author: Michael Boyte & Robbie Todd II
# Date: June 21, 2022
# Project: HW3
# Class: RBE500
# File Description:
# Takes in joint values from gazebo and calculates end effector and orientation
#

import rospy
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Pose
import math

# multiply 2 matrix #
def matrix_mult(A, B):
    # variables #
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    # iterating by row of A
    for i in range(len(A)):
        # iterating by column by B
        for j in range(len(B[0])):
            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# transform the matrix #
def transformation(q, d, a, alpha):
    temp = [[math.cos(math.radians(q)), -math.sin(math.radians(q))*math.cos(math.radians(alpha)), math.sin(math.radians(q))*math.sin(math.radians(alpha)), a*math.cos(math.radians(q))],
            [math.sin(math.radians(q)), math.cos(math.radians(q))*math.cos(math.radians(alpha)), -math.cos(math.radians(q))*math.sin(math.radians(alpha)), a*math.sin(math.radians(q))],
            [0, math.sin(math.radians(alpha)), math.cos(math.radians(alpha)), d],
            [0, 0, 0, 1]]
    return temp

# callback function used by subscriber #
def callback(data):
    # get final pose and publish Pose message #
    final_pose = angle_effector_pose(data)

    # call to publish pose #
    pub_pose(final_pose)

# function used to calculate the effector pose from angles #
def angle_effector_pose(joint_variables):
    # variables #
    a1 = 150
    a2 = 600
    a3 = 0
    alpha1 = 0
    alpha2 = 0
    alpha3 = 0
    d1 = 300
    d2 = 0
    q3 = 0

    # transform matrix #
    t01 = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]
    t12 = transformation((joint_variables.position[0])*180/math.pi, d1, a1, alpha1) # changed q1 to position
    t23 = transformation((joint_variables.position[1])*180/math.pi, d2, a2, alpha2) # changed q2 to velocity
    t34 = transformation(q3, (joint_variables.position[2])*180/math.pi, a3, alpha3) # changed d3 to 3 for hard code

    # multiply matrix #
    temp = matrix_mult(t01, t12)
    temp = matrix_mult(temp, t23)
    temp = matrix_mult(temp, t34)  # use as final pose

    return temp


# publisher of pose #
def pub_pose(final_pose):

    # get orientation #
    rot_diag_sum = final_pose[0][0] + final_pose[1][1] + final_pose[2][2]
    if(rot_diag_sum > 0):
        S = math.sqrt(rot_diag_sum+1.0) * 2
        qw = 0.25 * S
        qx = (final_pose[2][1] - final_pose[1][2]) / S
        qy = (final_pose[0][2] - final_pose[2][0]) / S
        qz = (final_pose[1][0] - final_pose[0][1]) / S
    elif((final_pose[0][0] > final_pose[1][1]) & (final_pose[0][0] > final_pose[2][2])):
        S = math.sqrt(1.0 + final_pose[0][0] - final_pose[1][1] - final_pose[2][2]) * 2
        qw = (final_pose[2][1] - final_pose[1][2]) / S
        qx = 0.25 * S
        qy = (final_pose[0][1] + final_pose[1][0]) / S
        qz = (final_pose[0][2] + final_pose[2][0]) / S
    elif(final_pose[1][1] > final_pose[2][2]):
        S = math.sqrt(1.0 + final_pose[1][1] - final_pose[0][0] - final_pose[2][2]) * 2
        qw = (final_pose[0][2] - final_pose[2][0]) / S
        qx = (final_pose[0][1] + final_pose[1][0]) / S
        qy = 0.25 * S
        qz = (final_pose[1][2] + final_pose[2][1]) / S
    else:
        S = math.sqrt(1.0 + final_pose[2][2] - final_pose[0][0] - final_pose[1][1]) * 2
        qw = (final_pose[1][0] - final_pose[0][1]) / S
        qx = (final_pose[0][2] + final_pose[2][0]) / S
        qy = (final_pose[1][2] + final_pose[2][1]) / S
        qz = 0.25 * S

    # set up for pose message #
    pose = Pose()

    # store position and orientation message #
    pose.position.x = final_pose[0][3]
    pose.position.y = final_pose[1][3]
    pose.position.z = final_pose[2][3]
    pose.orientation.x = qy
    pose.orientation.y = qx
    pose.orientation.z = qz
    pose.orientation.w = qw

    # publish message #
    pub = rospy.Publisher('pose', Pose, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    pub.publish(pose)
    rate.sleep()

# main function #
def angle_subscriber():
    # ros node setup #
    rospy.init_node('subscriber_fk')
    rospy.Subscriber("joint_states", JointState, callback)
    rospy.spin()  # keep node running

# main #
if __name__ == "__main__":
    angle_subscriber()
