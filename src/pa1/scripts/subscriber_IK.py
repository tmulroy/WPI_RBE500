#!/usr/bin/env python
# Author: Michael Boyte & Robbie Todd II
# Date: June 21, 2022
# Project: HW3
# Class: RBE500
# File Description:
# Calculates out Inverse Kinematics and response with q1 q2 and d3
#
import rospy
from pa1.srv import HT,HTResponse
import math

# used to store joint variables
class joint_variables(object):
    def __init__(self, q1, q2, d3):
        self.q1 = q1
        self.q2 = q2
        self.d3 = d3


# setup DH parameterss struct to used to store all the DH parameters #
class dh_params(object):
    def __init__(self, q3, d1, d2, a1, a2, a3, alpha1, alpha2, alpha3):
        self.q3 = q3
        self.d1 = d1
        self.d2 = d2
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.alpha1 = alpha1
        self.alpha2 = alpha2
        self.alpha3 = alpha3


# calculate out the homogeneous matrix once all variables are known #
def calculate_ht(dh_params, jnt_vars):
    # variables #
    q1 = jnt_vars.q1
    q2 = jnt_vars.q2
    # q3 = dh_params.q3
    d1 = dh_params.d1
    # d2 = dh_params.d2
    d3 = jnt_vars.d3
    a1 = dh_params.a1
    a2 = dh_params.a2
    a3 = dh_params.a3
    # alpha1 = dh_params.alpha1
    # alpha2 = dh_params.alpha2
    # alpha3 = dh_params.alpha3

    # homogeneous matrix #
    HT = [[math.cos(q1) * math.cos(q2) - math.sin(q1) * math.sin(q2),
           -math.cos(q1) * math.sin(q2) - math.cos(q2) * math.sin(q1), 0,
           a1 * math.cos(q1) + a2 * math.cos(q1) * math.cos(q2) - a2 * math.sin(q1) * math.sin(q2)],
          [math.cos(q1) * math.sin(q2) + math.cos(q2) * math.sin(q1),
           math.cos(q1) * math.cos(q2) - math.sin(q1) * math.sin(q2), 0,
           a1 * math.sin(q1) + a2 * math.cos(q1) * math.sin(q2) + a2 * math.cos(q2) * math.sin(q1)],
          [0, 0, 1, d1 + d3],
          [0, 0, 0, 1]]

    return HT

# calculating the Inverse Kinematics #
def ik(dh_params, ht):
    # variables #
    # q1 = dh_params.q1
    # q2 = dh_params.q2
    # q3 = dh_params.q3
    d1 = dh_params.d1
    # d2 = dh_params.d2
    # d3 = dh_params.d3
    a1 = dh_params.a1
    a2 = dh_params.a2
    a3 = dh_params.a3
    # alpha1 = dh_params.alpha1
    # alpha2 = dh_params.alpha2
    # alpha3 = dh_params.alpha3

    ## IK Position
    # calculate d3
    x = ht[0][3]
    y = ht[1][3]
    z = ht[2][3]
    d3_ik = z - d1

    # calculate q2
    r = math.sqrt(x ** 2 + y ** 2)
    D_q2 = (a1 ** 2 + a2 ** 2 - r ** 2) / (2 * a1 * a2)
    C_q2_pos = math.sqrt(1 - D_q2 ** 2)
    C_q2_neg = -math.sqrt(1 - D_q2 ** 2)
    A_q2_pos = math.atan2(C_q2_pos, D_q2)
    A_q2_neg = math.atan2(C_q2_neg, D_q2)
    q2_pos_ik = math.pi - A_q2_pos
    q2_neg_ik = math.pi - A_q2_neg

    # calculating q1
    alpha = math.atan2(y, x)
    D_q1 = (a1 ** 2 + r ** 2 - a2 ** 2) / (2 * a1 * r)
    C_q1_pos = math.sqrt(1 - D_q1 ** 2)
    C_q1_neg = -math.sqrt(1 - D_q1 ** 2)
    beta_pos = math.atan2(C_q1_pos, D_q1)
    beta_neg = math.atan2(C_q1_neg, D_q1)
    q1_pos_ik = alpha - beta_pos
    q1_neg_ik = alpha - beta_neg

    ## IK Orientation
    HT11 = ht[0][0]
    pos_test = math.cos(q1_pos_ik) * math.cos(q2_pos_ik) - math.sin(q1_pos_ik) * math.sin(q2_pos_ik)
    neg_test = math.cos(q1_neg_ik) * math.cos(q2_neg_ik) - math.sin(q1_neg_ik) * math.sin(q2_neg_ik)

    if abs(abs(pos_test) - abs(HT11)) < 10 ** -10:
        q1_ik = q1_pos_ik
        q2_ik = q2_pos_ik

    if abs(abs(neg_test) - abs(HT11)) < 10 ** -10:
        q1_ik = q1_neg_ik
        q2_ik = q2_neg_ik

    jnt_vars = joint_variables(q1_ik, q2_ik, d3_ik)

    return jnt_vars


# callback function used by subscriber #
def callback(data):
    # variables #
    print("Calculating joint variables!")
    dh_parm = dh_params(0, 5, 0, 5, 2, 0, 0, 0, 0)
    ht = [[data.ht11, data.ht12, data.ht13, data.ht14],
          [data.ht21, data.ht22, data.ht23, data.ht24],
          [data.ht31, data.ht32, data.ht33, data.ht34],
          [data.ht41, data.ht42, data.ht43, data.ht44]]

    joint_variables = ik(dh_parm, ht)

    joint = HTResponse()
    joint.q1 = ((joint_variables.q1) * (180 / math.pi))
    joint.q2 = ((joint_variables.q2) * (180 / math.pi))
    joint.d3 = joint_variables.d3

    return joint

# main function #
def IK_subscriber():
    # ros node setup #
    rospy.init_node('subscriber_ik')
    service = rospy.Service("set_coordinates", HT, callback)
    rospy.spin()  # keep node running

# main #
if __name__ == "__main__":
    IK_subscriber()