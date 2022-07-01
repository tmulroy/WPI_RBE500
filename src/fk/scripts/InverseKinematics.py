#!/usr/bin/env python
import math
import rospy
import numpy
from fk.msg import JointVariables
from geometry_msgs.msg import Pose

def transpose(matrix):
    rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return rez

theta1 = 0;
theta2 = 0;
theta3 = 0;
theta4 = 0;
theta5 = 0;
theta6 = 0;

# Setup transformation matrices for end effector

# t01 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]];
# t12 = [[math.cos(theta1),-math.sin(theta1)*math.cos(90),math.sin(theta1)*math.sin(90),150*math.cos(theta1)],[math.sin(theta1),math.cos(theta1)*math.cos(90),-math.cos(theta1)*math.sin(90),150*math.sin(theta1)],[0,math.sin(90),math.cos(90),475],[0,0,0,1]]
# t23 = [[math.cos(theta2+90),-math.sin(theta2+90),0,600*math.cos(theta2+90)],[math.sin(theta2+90),math.cos(theta2+90),0,600*math.sin(theta2+90)],[0,0,1,0],[0,0,0,1]]
# t34 = [[math.cos(theta3),-math.sin(theta3)*math.cos(90),math.sin(theta3)*math.sin(90),120*math.cos(theta3)],[math.sin(theta3),math.cos(theta3)*math.cos(90),-math.cos(theta3)*math.sin(90),120*math.sin(theta3)],[0,math.sin(90)],[math.cos(90),0],[0,0,0,1]]
# t45 = [[math.cos(theta4+90),-math.sin(theta4+90)*math.cos(90),math.sin(theta4+90)*math.sin(90),0],[math.sin(theta4+90),math.cos(theta4+90),-math.cos(theta4+90)*math.sin(90),0],[0,math.sin(90),math.cos(90),720],[0,0,0,1]]
# t56 = [[math.cos(theta5),-math.sin(theta5)*math.cos(-90),math.sin(theta5)*math.sin(-90),0],[math.sin(theta5),math.cos(theta5)*math.cos(-90),-math.cos(theta5)*math.sin(-90),0],[0,math.sin(-90),math.cos(-90),0],[0,0,0,1]]
# t67 = [[math.cos(theta6),-math.sin(theta6),0,0],[math.sin(theta6),math.cos(theta6),0,0],[0,0,1,85],[0,0,0,1]]
# t07 = t01*t12*t23*t34*t45*t56*t67


# Build arm and spherical wrist rotation matrices

# r07 = [[t07(1,1),t07(1,2),t07(1,3)],[t07(2,1),t07(2,2),t07(2,3)],[t07(3,1),t07(3,2),t07(3,3)]]
r07 = [[1,0,0],[0,1,0],[0,0,1]]


# Given Vector O(Ox,Oy,Oz)
Ox = 500;
Oy = 100;
Oz = 1500;
O_vector = [[Ox],[Oy],[Oz]]

# Calculate Vector d
magnitude_d = 85;
d_unit_vector = list(list(zip(*r07))[0])
d_vector = [ d_unit_vector[0] * magnitude_d,d_unit_vector[1] * magnitude_d,d_unit_vector[2] * magnitude_d]

# print(f'd_vector: {d_vector[0]}')

# Calculate Vector Oc
Oc_vector = [Ox - d_vector[0],Oy - d_vector[1],Oz - d_vector[2]]
Xc = Oc_vector[0];
Yc = Oc_vector[1];
Zc = Oc_vector[2];

# print(f'Oc_vector: {Oc_vector}')


# INVERSE POSITION KINEMATICS
d = 150; #offset
d1 = 475;
a1 = 600;
a2 = math.sqrt(120**2 + 720**2);
r = math.sqrt(Xc**2 + Yc**2);
s = Zc - d1;


# THETA 1
D_theta1 = Xc/r;
theta1_pos = math.degrees(math.atan2(math.sqrt(1 - D_theta1**2), D_theta1))
theta1_neg = math.degrees(math.atan2(-math.sqrt(1 - D_theta1**2), D_theta1))


# print(f'theta1_pos {theta1_pos}')
# print(f'theta1_neg {theta1_neg}')

# THETA 2
D_theta2_beta = (a1*2 + r**2 + s**2 - a2**2)/(2*a1*math.sqrt(r**2 + s**2))

# print(f'D_theta2_beta: {D_theta2_beta}')
# Calculate Beta
C_pos_theta2_beta = math.sqrt(1 - D_theta2_beta**2)
C_neg_theta2_beta = -math.sqrt(1 - D_theta2_beta**2)

# print(f'C_pos_theta2_beta: {C_pos_theta2_beta}')
# print(f'C_neg_theta2_beta: {C_neg_theta2_beta}')
beta_pos = math.degrees(math.atan2(C_pos_theta2_beta,D_theta2_beta))
beta_neg = math.degrees(math.atan2(C_neg_theta2_beta,D_theta2_beta))

# print(f'beta_pos: {beta_pos}')
# print(f'beta_neg: {beta_neg}')

# Calculate Alpha
D_theta2_alpha = r/math.sqrt(r**2 + s**2)
C_pos_theta2_alpha = math.sqrt(1 - D_theta2_alpha**2)
C_neg_theta2_alpha = -math.sqrt(1 - D_theta2_alpha**2)
alpha_pos = math.degrees(math.atan2(C_pos_theta2_alpha,D_theta2_alpha))
alpha_neg = math.degrees(math.atan2(C_neg_theta2_alpha,D_theta2_alpha))

theta2_pos = alpha_pos - beta_pos;
theta2_neg = alpha_neg - beta_neg;


# THETA 3
D_theta3 = -((a1**2 + a2**2 - (r**2 + s**2))/(2*a1*a2))
theta3_pos = math.degrees(math.atan2(math.sqrt(1 - (D_theta3**2)), D_theta3))
theta3_neg = math.degrees(math.atan2(-math.sqrt(1 - (D_theta3**2)), D_theta3))



# INVERSE ORIENTATION KINEMATICS

r04 = [[math.cos(theta1_pos)*math.cos(theta2_pos+theta3_pos), -math.cos(theta1_pos)*math.sin(theta2_pos+theta3_pos), math.sin(theta1_pos)],[
        math.sin(theta1_pos)*math.cos(theta2_pos+theta3_pos), -math.sin(theta1_pos)*math.sin(theta2_pos+theta3_pos), -math.cos(theta1_pos)],[
        math.sin(theta2_pos+theta3_pos), math.cos(theta2_pos+theta3_pos), 0]]

transposed_r04 = numpy.transpose(r04)
# transposed_r04*r07
r47 = numpy.matmul(transposed_r04,r07)

# print(f'\nr47 {r47}')

# THETA 4
theta4_y_pos = math.cos(theta1_pos)*math.cos(theta2_pos+theta3_pos)*r07[0][2] + math.sin(theta1_pos)*math.cos(theta2_pos+theta3_pos)*r07[1][2] + math.sin(theta2_pos+theta3_pos)*r07[2][2]
theta4_x_pos = -math.cos(theta1_pos)*math.sin(theta2_pos+theta3_pos)*r07[0][2] - math.sin(theta1_pos)*math.sin(theta2_pos+theta3_pos)*r07[1][2] + math.cos(theta2_pos+theta3_pos)*r07[2][2]

theta4_y_neg = math.cos(theta1_neg)*math.cos(theta2_neg+theta3_neg)*r07[0][2] + math.sin(theta1_neg)*math.cos(theta2_neg+theta3_neg)*r07[1][2] + math.sin(theta2_neg+theta3_neg)*r07[2][2]
theta4_x_neg = -math.cos(theta1_neg)*math.sin(theta2_neg+theta3_neg)*r07[0][2] - math.sin(theta1_neg)*math.sin(theta2_neg+theta3_neg)*r07[1][2] + math.cos(theta2_neg+theta3_neg)*r07[2][2]


theta4_pos = math.degrees(math.atan2(theta4_y_pos,theta4_x_pos))
theta4_neg = math.degrees(math.atan2(theta4_y_neg,theta4_x_neg))

# THETA 5
theta5_y_pos = math.sin(theta1_pos)*r07[0][2] - math.cos(theta1_pos)*r07[1][2]
theta5_x_pos = math.sqrt(1 - (math.sin(theta1_pos)*r07[0][2] - math.cos(theta1_pos)*r07[1][2])**2 )

theta5_y_neg = math.sin(theta1_neg)*r07[0][2] - math.cos(theta1_neg)*r07[1][2]
theta5_x_neg = math.sqrt(1 - (math.sin(theta1_neg)*r07[0][2] - math.cos(theta1_neg)*r07[1][2])**2 )

theta5_pos = math.degrees(math.atan2(theta5_y_pos,theta5_x_pos))
theta5_neg = math.degrees(math.atan2(theta5_y_neg,theta5_x_neg))

# THETA 6
theta6_y_pos = -math.sin(theta1_pos)*r07[0][0] + math.cos(theta1_pos)*r07[1][0]
theta6_x_pos = math.sin(theta1_pos)*r07[0][1] - math.cos(theta1_pos)*r07[1][1]

theta6_y_neg = -math.sin(theta1_neg)*r07[0][0] + math.cos(theta1_neg)*r07[1][0]
theta6_x_neg = math.sin(theta1_neg)*r07[0][1] - math.cos(theta1_neg)*r07[1][1]

theta6_pos = math.degrees(math.atan2(theta6_y_pos,theta6_x_pos))
theta6_neg = math.degrees(math.atan2(theta6_y_neg,theta6_x_neg))

pos_IK = [theta1_pos,theta2_pos, theta3_pos, theta4_pos, theta5_pos, theta6_pos]
neg_IK = [theta1_neg,theta2_neg, theta3_neg, theta4_neg, theta5_neg, theta6_neg]

print(f'pos_IK: {pos_IK}')
