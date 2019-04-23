

I'm able to display data from two topics but I can't do use and compute data in real time from these two topics in ROS (written in Python code).

Have you got any idea to stock this data and compute in real time ?

Thanks ;)

#!/usr/bin/env python

import rospy
import string
from std_msgs.msg import String 
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float64
import numpy as np


class ListenerVilma:

    def __init__(self):
        self.orientation = rospy.Subscriber('/orientation', Float64MultiArray , self.orientation_callback)
        self.velocidade = rospy.Subscriber('/velocidade', Float64MultiArray, self.velocidade_callback)

    def orientation_callback(self, orientation):
        print orientation

    def velocidade_callback(self, velocidade):
        print velocidade


if __name__ == '__main__':
   rospy.init_node('listener', anonymous=True)
   myVilma = ListenerVilma()
   rospy.spin()

