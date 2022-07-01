#!/usr/bin/env python3
import math
import rospy
import numpy
from fk.msg import JointVariables
from geometry_msgs.msg import Pose

# rostopic pub pose geometry_msgs/Pose "position:
#   x: 0.0
#   y: 0.0
#   z: 0.0
# orientation:
#   x: 0.0
#   y: 0.0
#   z: 0.0
#   w: 0.0"
def transpose(matrix):
    rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return rez

def forward_kinematics():
    # Calculate Forward Kinematics

    # theta1 = q.q1
    # theta2 = q.q2
    # theta3 = q.q3
    # theta4 = q.q4
    # theta5 = q.q5
    # theta6 = q.q5

    # fk = [[
    #    math.sin(theta6)*(math.cos(theta4 + math.pi/2)*math.sin(theta1) + math.sin(theta4 + math.pi/2)*(math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2))) + math.cos(theta6)*(math.cos(theta5)*(math.sin(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2))) + math.sin(theta5)*(math.cos(theta4 + math.pi/2)*math.sin(theta1) + math.cos(theta1)*math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta1)*math.cos(theta2 + math.pi/2)*math.sin(theta3))), math.cos(theta6)*(math.cos(theta4 + math.pi/2)*math.sin(theta1) + math.sin(theta4 + math.pi/2)*(math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2))) - math.sin(theta6)*(math.cos(theta5)*(math.sin(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2))) + math.sin(theta5)*(math.cos(theta4 + math.pi/2)*math.sin(theta1) + math.cos(theta1)*math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta1)*math.cos(theta2 + math.pi/2)*math.sin(theta3))), math.sin(theta5)*(math.sin(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2))) + math.cos(theta5)*(math.cos(theta4 + math.pi/2)*math.sin(theta1) + math.cos(theta1)*math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta1)*math.cos(theta2 + math.pi/2)*math.sin(theta3)),
    #    150*math.cos(theta1) + 600*math.cos(theta1)*math.cos(theta2 + math.pi/2) + 85*math.sin(theta5)*(math.sin(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) -math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2))) + 85*math.cos(theta5)*(math.cos(theta4 + math.pi/2)*math.sin(theta1) + math.cos(theta1)*math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta1)*math.cos(theta2 + math.pi/2)*math.sin(theta3)) - 120*math.cos(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2) + 120*math.cos(theta1)*math.cos(theta3)*math.cos(theta2 + math.pi/2)
    # ],
    # [
    #    -math.cos(theta6)*(math.cos(theta5)*(math.cos(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2))) - math.sin(theta5)*(math.cos(theta3)*math.sin(theta1)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta4 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta1)*math.sin(theta3))) - math.sin(theta6)*(math.cos(theta1)*math.cos(theta4 + math.pi/2) + math.sin(theta4 + math.pi/2)*(math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2))), math.sin(theta6)*(math.cos(theta5)*(math.cos(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2))) - math.sin(theta5)*(math.cos(theta3)*math.sin(theta1)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta4 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta1)*math.sin(theta3))) - math.cos(theta6)*(math.cos(theta1)*math.cos(theta4 + math.pi/2) + math.sin(theta4 + math.pi/2)*(math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2))), math.cos(theta5)*(math.cos(theta3)*math.sin(theta1)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta4 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta1)*math.sin(theta3)) - math.sin(theta5)*(math.cos(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2))),
    #    150*math.sin(theta1) + 600*math.cos(theta2 + math.pi/2)*math.sin(theta1) - 85*math.sin(theta5)*(math.cos(theta1)*math.sin(theta4 + math.pi/2) - math.cos(theta4 + math.pi/2)*(math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2))) + 85*math.cos(theta5)*(math.cos(theta3)*math.sin(theta1)*math.sin(theta2 + math.pi/2) - math.cos(theta1)*math.cos(theta4 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta1)*math.sin(theta3)) + 120*math.cos(theta3)*math.cos(theta2 + math.pi/2)*math.sin(theta1) - 120*math.sin(theta1)*math.sin(theta3)*math.sin(theta2 + math.pi/2)
    # ],
    # [
    #    - math.cos(theta6)*(math.sin(theta5)*(math.cos(theta3)*math.cos(theta2 + math.pi/2) - math.sin(theta3)*math.sin(theta2 + math.pi/2)) - math.cos(theta5)*math.cos(theta4 + math.pi/2)*(math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta3))) - math.sin(theta6)*math.sin(theta4 + math.pi/2)*(math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta3)),                                                                                                                                                                                math.sin(theta6)*(math.sin(theta5)*(math.cos(theta3)*math.cos(theta2 + math.pi/2) - math.sin(theta3)*math.sin(theta2 + math.pi/2)) - math.cos(theta5)*math.cos(theta4 + math.pi/2)*(math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta3))) - math.cos(theta6)*math.sin(theta4 + math.pi/2)*(math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta3)),
    #    math.cos(theta4 + math.pi/2)*math.sin(theta5)*(math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta3)) - math.cos(theta5)*(math.cos(theta3)*math.cos(theta2 + math.pi/2) - math.sin(theta3)*math.sin(theta2 + math.pi/2)),                                                                                                                                                                     600*math.sin(theta2 + math.pi/2) + 120*math.cos(theta3)*math.sin(theta2 + math.pi/2) + 120*math.cos(theta2 + math.pi/2)*math.sin(theta3) - 85*math.cos(theta5)*(math.cos(theta3)*math.cos(theta2 + math.pi/2) - math.sin(theta3)*math.sin(theta2 + math.pi/2)) + 85*math.cos(theta4 + math.pi/2)*math.sin(theta5)*(math.cos(theta3)*math.sin(theta2 + math.pi/2) + math.cos(theta2 + math.pi/2)*math.sin(theta3)) + 475
    # ],
    # [0,0,0,1]
    # ]

    # orientation = [
    #     [ fk[0][0],fk[0][1],fk[0][2] ],
    #     [ fk[1][0],fk[1][1],fk[1][2] ],
    #     [ fk[0][0],fk[0][1],fk[0][2] ]
    # ]
    #
    # position = [
    #     [ fk[0][3] ],
    #     [ fk[1][3] ],
    #     [ fk[2][3] ]
    # ]

    # # print entire forward kinematics transformation matrix
    # print(f'\nFORWARD KINEMATICS TRANSFORMATION MATRIX: \n \n{fk[0]} \n {fk[1]} \n {fk[3]} \n')
    #
    # # print orientation
    # print(f'ORIENTATION: \n \n {orientation[0]} \n {orientation[1]} \n {orientation[2]} \n')
    #
    # # print position
    # print(f'POSITION: \n \n {position[0]} \n {position[1]} \n {position[2]}')
    pass

def convert_quat_to_euler(q):
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

    ros.loginfo(f'roll: {roll} pitch: {pitch} yaw: {yaw}')
    theta1 = 0;
    theta2 = 0;
    theta3 = 0;
    theta4 = 0;
    theta5 = 0;
    theta6 = 0;

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

def callback(Pose):

    rospy.loginfo(rospy.get_caller_id() + "I heard ----- %s", Pose)

    # Convert quaternion orientation to euler angles
    # Calculate joint values (q1...q6) using IK
    # Verify result with FK
    inverse_kinematics(Pose)

def listener():
    rospy.init_node('listener', anonymous=True)

    # rospy.Subscriber("forward_kinematics", JointVariables, callback)

    rospy.Subscriber("pose", Pose, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
