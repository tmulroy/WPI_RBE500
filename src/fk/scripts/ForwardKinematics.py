#!/usr/bin/env python
import math
import rospy
import numpy
from fk.msg import JointVariables
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist



def forward_kinematics(q):
    # Calculate Forward Kinematics

    theta1 = q[0]
    theta2 = q[1]
    theta3 = q[2]
    theta4 = q[3]
    theta5 = q[4]
    theta6 = q[5]

    fk = [
    [
        math.cos((math.pi*theta6)/180)*(math.cos((math.pi*theta5)/180)*(math.sin((math.pi*theta1)/180)*math.sin((math.pi*(theta4 + 90))/180) - math.cos((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180)*math.cos((math.pi*(theta4 + 90))/180)) + math.sin((math.pi*theta5)/180)*(math.cos((math.pi*theta1)/180)*math.cos((math.pi*theta3)/180) + math.sin((math.pi*theta1)/180)*math.cos((math.pi*(theta4 + 90))/180))) + math.sin((math.pi*theta6)/180)*(math.sin((math.pi*theta1)/180)*math.cos((math.pi*(theta4 + 90))/180) + math.cos((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180)*math.sin((math.pi*(theta4 + 90))/180)),

        math.cos((math.pi*theta6)/180)*(math.sin((math.pi*theta1)/180)*math.cos((math.pi*(theta4 + 90))/180) + math.cos((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180)*math.sin((math.pi*(theta4 + 90))/180)) - math.sin((math.pi*theta6)/180)*(math.cos((math.pi*theta5)/180)*(math.sin((math.pi*theta1)/180)*math.sin((math.pi*(theta4 + 90))/180) - math.cos((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180)*math.cos((math.pi*(theta4 + 90))/180)) + math.sin((math.pi*theta5)/180)*(math.cos((math.pi*theta1)/180)*math.cos((math.pi*theta3)/180) + math.sin((math.pi*theta1)/180)*math.cos((math.pi*(theta4 + 90))/180))),

        math.cos((math.pi*theta5)/180)*(math.cos((math.pi*theta1)/180)*math.cos((math.pi*theta3)/180) + math.sin((math.pi*theta1)/180)*math.cos((math.pi*(theta4 + 90))/180)) - math.sin((math.pi*theta5)/180)*(math.sin((math.pi*theta1)/180)*math.sin((math.pi*(theta4 + 90))/180) - math.cos((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180)*math.cos((math.pi*(theta4 + 90))/180)),

        150*math.cos((math.pi*theta1)/180) + 720*math.cos((math.pi*theta1)/180)*math.cos((math.pi*theta3)/180) - 120*math.cos((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180) + 85*math.cos((math.pi*theta5)/180)*(math.cos((math.pi*theta1)/180)*math.cos((math.pi*theta3)/180) + math.sin((math.pi*theta1)/180)*math.cos((math.pi*(theta4 + 90))/180)) - 85*math.sin((math.pi*theta5)/180)*(math.sin((math.pi*theta1)/180)*math.sin((math.pi*(theta4 + 90))/180) - math.cos((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180)*math.cos((math.pi*(theta4 + 90))/180))
        ],

    [
        - math.cos((math.pi*theta6)/180)*(math.cos((math.pi*theta5)/180)*(math.cos((math.pi*theta1)/180)*math.sin((math.pi*(theta4 + 90))/180) + math.sin((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180)*math.cos((math.pi*(theta4 + 90))/180)) - math.sin((math.pi*theta5)/180)*(math.cos((math.pi*theta3)/180)*math.sin((math.pi*theta1)/180) - math.cos((math.pi*theta1)/180)*math.cos((math.pi*(theta4 + 90))/180))) - math.sin((math.pi*theta6)/180)*(math.cos((math.pi*theta1)/180)*math.cos((math.pi*(theta4 + 90))/180) - math.sin((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180)*math.sin((math.pi*(theta4 + 90))/180)),

        math.sin((math.pi*theta6)/180)*(math.cos((math.pi*theta5)/180)*(math.cos((math.pi*theta1)/180)*math.sin((math.pi*(theta4 + 90))/180) + math.sin((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180)*math.cos((math.pi*(theta4 + 90))/180)) - math.sin((math.pi*theta5)/180)*(math.cos((math.pi*theta3)/180)*math.sin((math.pi*theta1)/180) - math.cos((math.pi*theta1)/180)*math.cos((math.pi*(theta4 + 90))/180))) - math.cos((math.pi*theta6)/180)*(math.cos((math.pi*theta1)/180)*math.cos((math.pi*(theta4 + 90))/180) - math.sin((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180)*math.sin((math.pi*(theta4 + 90))/180)),

        math.cos((math.pi*theta5)/180)*(math.cos((math.pi*theta3)/180)*math.sin((math.pi*theta1)/180) - math.cos((math.pi*theta1)/180)*math.cos((math.pi*(theta4 + 90))/180)) + math.sin((math.pi*theta5)/180)*(math.cos((math.pi*theta1)/180)*math.sin((math.pi*(theta4 + 90))/180) + math.sin((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180)*math.cos((math.pi*(theta4 + 90))/180)),

        150*math.sin((math.pi*theta1)/180) + 720*math.cos((math.pi*theta3)/180)*math.sin((math.pi*theta1)/180) - 120*math.sin((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180) + 85*math.cos((math.pi*theta5)/180)*(math.cos((math.pi*theta3)/180)*math.sin((math.pi*theta1)/180) - math.cos((math.pi*theta1)/180)*math.cos((math.pi*(theta4 + 90))/180)) + 85*math.sin((math.pi*theta5)/180)*(math.cos((math.pi*theta1)/180)*math.sin((math.pi*(theta4 + 90))/180) + math.sin((math.pi*theta1)/180)*math.sin((math.pi*theta3)/180)*math.cos((math.pi*(theta4 + 90))/180))
    ],

    [
        math.cos((math.pi*theta6)/180)*(math.sin((math.pi*theta3)/180)*math.sin((math.pi*theta5)/180) + math.cos((math.pi*theta3)/180)*math.cos((math.pi*theta5)/180)*math.cos((math.pi*(theta4 + 90))/180)) - math.cos((math.pi*theta3)/180)*math.sin((math.pi*theta6)/180)*math.sin((math.pi*(theta4 + 90))/180),                                                                                                                                                                                                                             - math.sin((math.pi*theta6)/180)*(math.sin((math.pi*theta3)/180)*math.sin((math.pi*theta5)/180) +

        math.cos((math.pi*theta3)/180)*math.cos((math.pi*theta5)/180)*math.cos((math.pi*(theta4 + 90))/180)) - math.cos((math.pi*theta3)/180)*math.cos((math.pi*theta6)/180)*math.sin((math.pi*(theta4 + 90))/180),

        math.cos((math.pi*theta5)/180)*math.sin((math.pi*theta3)/180) - math.cos((math.pi*theta3)/180)*math.sin((math.pi*theta5)/180)*math.cos((math.pi*(theta4 + 90))/180),

        120*math.cos((math.pi*theta3)/180) + 720*math.sin((math.pi*theta3)/180) + 85*math.cos((math.pi*theta5)/180)*math.sin((math.pi*theta3)/180) - 85*math.cos((math.pi*theta3)/180)*math.sin((math.pi*theta5)/180)*math.cos((math.pi*(theta4 + 90))/180) + 1075
        ],

    [
        0,
        0,
        0,
        1
    ]
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
    # print(f'\nFORWARD KINEMATICS TRANSFORMATION MATRIX: \n \n{fk[0]} \n {fk[1]} \n {fk[3]} \n')

    # print orientation
    print(f'ORIENTATION: \n \n {orientation[0]} \n {orientation[1]} \n {orientation[2]} \n')

    # print position
    print(f'POSITION: \n \n {position[0]} \n {position[1]} \n {position[2]}')


def convert_quat_to_euler(q):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", q)

    # roll (x-axis-rotation)
    sinr_cosp = 2 * (q.w * q.x + q.y * q.z)
    cosr_cosp = 1 - 2 * (q.x * q.x + q.y * q.y)
    roll = math.atan2(sinr_cosp, cosr_cosp)

    # pitch (y-axis rotation)
    sinp = 2 * (q.w * q.y - q.z * q.z)
    if abs(sinp) >= 1:
        pitch = math.copysign(math.pi/2,sinp)
    else:
        pitch = math.asin(sinp)

    # yaw (z-axis rotation)
    siny_cosp = 2 * (q.w * q.z + q.x * q.y)
    cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
    yaw = math.atan2(siny_cosp, cosy_cosp)

    return [roll,pitch,yaw]

def inverse_kinematics(Pose):

    [roll,pitch,yaw] = convert_quat_to_euler(Pose.orientation)

    # theta1 = 0;
    # theta2 = 0;
    # theta3 = 0;
    # theta4 = 0;
    # theta5 = 0;
    # theta6 = 0;

    r07 = [[1,0,0],[0,1,0],[0,0,1]]


    # Given Vector O(Ox,Oy,Oz)
    Ox = Pose.position.x;
    Oy = Pose.position.y;
    Oz = Pose.position.z;
    O_vector = [[Ox],[Oy],[Oz]]

    # Calculate Vector d
    magnitude_d = 85;
    d_unit_vector = list(list(zip(*r07))[0])
    d_vector = [ d_unit_vector[0] * magnitude_d,d_unit_vector[1] * magnitude_d,d_unit_vector[2] * magnitude_d]

    # Calculate Vector Oc
    Oc_vector = [Ox - d_vector[0],Oy - d_vector[1],Oz - d_vector[2]]
    Xc = Oc_vector[0];
    Yc = Oc_vector[1];
    Zc = Oc_vector[2];

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

    # THETA 2
    D_theta2_beta = (a1*2 + r**2 + s**2 - a2**2)/(2*a1*math.sqrt(r**2 + s**2))

    # Calculate Beta
    C_pos_theta2_beta = math.sqrt(1 - D_theta2_beta**2)
    C_neg_theta2_beta = -math.sqrt(1 - D_theta2_beta**2)

    beta_pos = math.degrees(math.atan2(C_pos_theta2_beta,D_theta2_beta))
    beta_neg = math.degrees(math.atan2(C_neg_theta2_beta,D_theta2_beta))

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

    return [pos_IK,neg_IK]

def calculate_joint_velocities(twist):

    # PLEASE NOTE! This only calculates Jacobian for theta1, theta2, theta3.
    # SPherical wrist angles are fixed at 0, so not included.
    # ASSUMPTIONS:
    #               Position of ee is [500;100;1500]
    #               theta1 of 25 degrees
    #               theta2 of 45 degrees
    #               theta2 of 30 degrees

    rospy.loginfo(rospy.get_caller_id() + "I heard ----- %s", twist)
    x = twist.linear.x
    y = twist.linear.y
    z = twist.linear.z

    theta1 = 25
    theta2 = 45
    theta3 = 30
    theta4 = 0
    theta5 = 0
    theta6 = 0

    t01 = numpy.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    t12 = numpy.array([[math.cos(theta1),-math.sin(theta1)*math.cos(90),math.sin(theta1)*math.sin(90),150*math.cos(theta1)],
            [math.sin(theta1),math.cos(theta1)*math.cos(90),-math.cos(theta1)*math.sin(90),150*math.sin(theta1)],
            [0,math.sin(90),math.cos(90),475],
            [0,0,0,1]])
    t23 = numpy.array([[math.cos(theta2+90),-math.sin(theta2+90),0,600*math.cos(theta2+90)],
            [math.sin(theta2+90),math.cos(theta2+90),0,600*math.sin(theta2+90)],
            [0,0,1,0],
            [0,0,0,1]])
    t34 = numpy.array([[math.cos(theta3),-math.sin(theta3)*math.cos(90),math.sin(theta3)*math.sin(90),120*math.cos(theta3)],
            [math.sin(theta3),math.cos(theta3)*math.cos(90),-math.cos(theta3)*math.sin(90),120*math.sin(theta3)],
            [0,math.sin(90),math.cos(90),0],
            [0,0,0,1]])
    t45 = numpy.array([[math.cos(theta4+90),-math.sin(theta4+90)*math.cos(90),math.sin(theta4+90)*math.sin(90),0],
            [math.sin(theta4+90),math.cos(theta4+90),-math.cos(theta4+90)*math.sin(90),0],
            [0,math.sin(90),math.cos(90),720],
            [0,0,0,1]])
    t56 = numpy.array([[math.cos(theta5),-math.sin(theta5)*math.cos(-90),math.sin(theta5)*math.sin(-90),0],
            [math.sin(theta5),math.cos(theta5)*math.cos(-90),-math.cos(theta5)*math.sin(-90),0],
            [0,math.sin(-90),math.cos(-90),0],
            [0,0,0,1]])
    t67 = numpy.array([[math.cos(theta6),-math.sin(theta6),0,0],
            [math.sin(theta6),math.cos(theta6),0,0],
            [0,0,1,85],
            [0,0,0,1]])

    t07 = t01*t12*t23*t34*t45*t56*t67
    t02 = t01*t12
    t03 = t02*t23
    t04 = t03*t34
    t05 = t04*t45
    t06 = t05*t56
    t07 = t06*t67
    print(f't01: {t01}')
    # Calculate Jacobian
    # End Effector position vector
    Pe = [500,100,1500]

    # J1
    P01 = t01[0:3,3]
    z1 = t01[0:3,2]
    r = Pe - P01
    Jp1 = numpy.cross(z1,r)
    Jo1 = numpy.array(z1)
    J1 = numpy.concatenate((Jp1,Jo1))

    # J2
    P02 = t02[0:3,3]
    z2 = t02[0:3,2]
    r2 = Pe - P02
    Jp2 = numpy.cross(z2,r)
    Jo2 = numpy.array(z2)
    J2 = numpy.concatenate((Jp2,Jo2))

    # J3
    P03 = t03[0:3,3]
    z3 = t03[0:3,2]
    r3 = Pe - P03
    Jp3 = numpy.cross(z3,r)
    Jo3 = numpy.array(z3)
    J3 = numpy.concatenate((Jp3,Jo3))

    # J4
    P04 = t04[0:3,3]
    z4 = t04[0:3,2]
    r4 = Pe - P04
    Jp4 = numpy.cross(z4,r)
    Jo4 = numpy.array(z4)
    J4 = numpy.concatenate((Jp4,Jo4))

    # J5
    P05 = t05[0:3,3]
    z5 = t05[0:3,2]
    r5 = Pe - P05
    Jp5 = numpy.cross(z5,r)
    Jo5 = numpy.array(z5)
    J5 = numpy.concatenate((Jp5,Jo5))

    # J6
    P06 = t06[0:3,3]
    z6 = t06[0:3,2]
    r6 = Pe - P06
    Jp6 = numpy.cross(z6,r)
    Jo6 = numpy.array(z6)
    J6 = numpy.concatenate((Jp6,Jo6))

    Jarm = numpy.concatenate((J1, J2, J3))
    Jwrist = numpy.concatenate((J4,J5,J6))
    J = numpy.concatenate((Jarm, Jwrist))
    arm = numpy.array([J1, J2, J3, J4, J5, J6])
    reshaped_arm_Jacobian = arm.transpose()
    print(f'Jacobian: {reshaped_arm_Jacobian.shape}')

    # J_inverse = numpy.linalg.inv(reshaped_arm_Jacobian)

    # joint_velocities = numpy.matmul(reshaped_arm_Jacobian,numpy.array([x,y,z]))

def callback(Pose):
    # Convert quaternion orientation to euler angles
    # Calculate joint values (q1...q6) umath.sing IK
    # Verify result with FK
    rospy.loginfo(rospy.get_caller_id() + "I heard ----- %s", Pose)

    # joint_variables = inverse_kinematics(Pose)

    q_pos = joint_variables[0]
    q_neg = joint_variables[1]

    print(f'\n Positive Joint Angles Calculated from Inverse Kinematics: {q_pos} \n')
    print(f'\n Negative Joint Angles Calculated from Inverse Kinematics: {q_neg} \n')

    print(f'FORWARD KINEMATICS VERIFICATION \n')

    # Verify using forward kinematics
    print(f'Forward Kinematics Position Calculated from Positive Joint Angles: \n')
    forward_kinematics(q_pos)
    print(f'Forward Kinematics Position Calculated from Negative Joint Angles: \n')

    forward_kinematics(q_neg)






def listener():
    rospy.init_node('listener', anonymous=True)

    # rospy.Subscriber("forward_kinematics", JointVariables, callback)

    # rospy.Subscriber("pose", Pose, callback)
    rospy.Subscriber("velocity", Twist, calculate_joint_velocities)

    rospy.spin()

if __name__ == '__main__':
    listener()
