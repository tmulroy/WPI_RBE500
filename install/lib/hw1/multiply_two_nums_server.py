#!/usr/bin/env python3

from __future__ import print_function

from hw1.srv import MultiplyTwoNums,MultiplyTwoNumsResponse
import rospy

def handle_multiply_two_nums(req):
    print("Returning [%s * %s = %s]"%(req.a, req.b, (req.a * req.b)))
    return MultiplyTwoNumsResponse(req.a * req.b)

def multiply_two_nums_server():
    rospy.init_node('multiply_two_nums_server')
    s = rospy.Service('multiply_two_nums', MultiplyTwoNums, handle_multiply_two_nums)
    print("Ready to multiply two numbers.")
    rospy.spin()

if __name__ == "__main__":
    multiply_two_nums_server()
