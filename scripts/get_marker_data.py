#!/usr/bin/env python

import rospy
import roslib
import tf

from geometry_msgs.msg import PoseArray



#Define a class
class Whycon_detect():

	def __init__(self):
		rospy.init_node('whycon_detection', anonymous = True)
    		rospy.Subscriber('/whycon/poses', PoseArray, self.callback)

	def callback(self,received_data):
		whycon_coordinates=dict()		
 		rec_posesdata=received_data.poses
		for i in range(len(rec_posesdata)):
			pos_list=list()
			pos_list.extend((round(rec_posesdata[i].position.x,3),round(rec_posesdata[i].position.y,3),round(rec_posesdata[i].position.z,3)))
			whycon_coordinates[i]=pos_list
    		#rospy.loginfo(whycon_coordinates)	
		print(whycon_coordinates)
	
if __name__=="__main__":
	marker = Whycon_detect()
	while not rospy.is_shutdown():
		rospy.spin()
