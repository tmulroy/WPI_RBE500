#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
from hw1.srv import *

def multiply_two_nums_client(x,y):
    rospy.wait_for_service('multiply_two_nums')
    try:
        multiply_two_nums = rospy.ServiceProxy('multiply_two_nums', MultiplyTwoNums)
        resp1 = multiply_two_nums(x,y)
        return resp1.product
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s*%s"%(x,y))
    print("%s * %s = %s"%(x,y, multiply_two_nums_client(x,y)))
