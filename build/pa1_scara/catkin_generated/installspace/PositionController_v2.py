#!/usr/bin/env python3
import math
import rospy
import numpy
from sensor_msgs.msg import JointState
from gazebo_msgs.srv import ApplyJointEffort, ApplyJointEffortRequest
from std_msgs.msg import Float64

def ApplyJointEffortToGazebo(joint_effort):
    # Service: /gazebo/apply_joint_effort
    #   msg: '{joint_name: "left_back_wheel_joint", effort: -0.2, start_time: 0, duration: -1}'
    rospy.wait_for_service('/gazebo/apply_joint_effort')
    try:
       apply_joint_effort = rospy.ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)
       joint_str = '{joint_name: "L2_to_end_effector", effort: -0.2, start_time: 0, duration: -1}'
       resp1 = apply_joint_effort(joint_str)
       print(f'response from apply_joint_effort: {resp1}')
    except rospy.ServiceException as e:
       print("Service call failed: %s"%e)

def PDControllerLogic(reference_position, current_position):
    dt = 1/50
    kd = 20
    kp = 0.1
    error = reference_position - current_position
    error_derivative = error/dt
    print(f'reference position: {reference_position}')
    print(f'current_position: {current_position}')
    print(f'error: {error}')
    print(f'error_derivative: {error_derivative}')
    force = kd*error_derivative + kp*error
    print(f'force: {force}')
    return force

def PositionController(joint_states, reference_position=3):
    rospy.loginfo(rospy.get_caller_id() + "I heard ----- %s", joint_states)

    # if reference_position != 0:
    #     print('received a reference position')
    #     joint_effort = PDControllerLogic(reference_position, current_position)
    #     ApplyJointEffortToGazebo(joint_effort)
    #
    # else:
    #     print('did not receive a reference position')
    current_position = joint_states.position[0]
    print(f'positoin: {current_position}')
    print('received a reference position')
    joint_effort = PDControllerLogic(reference_position, current_position)
    ApplyJointEffortToGazebo(joint_effort)

def listener():
    # Take in user input
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/joint_states", JointState, PositionController)
    rospy.Subscriber("/reference_position", Float64, PositionController)
    rospy.spin()

if __name__ == '__main__':
    listener()
