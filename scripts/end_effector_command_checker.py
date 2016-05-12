#!/usr/bin/env python

import rospy
from baxter_pykdl import baxter_kinematics
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

commandPositionPublisher = rospy.Publisher("end_effector_command_pose_stamped_checked", PoseStamped, queue_size=1)

checked = True
def commandCheckCallback(data):
	global checked
	if not (data.data.find("done") < 0):
                rospy.loginfo("command checked")
		checked = True

def callback(data):
        global checked

        if not checked:
                rospy.loginfo('Uncheck command.')
                #return
        checked = False
	commandPositionPublisher.publish(data)
	

def subscribe():
        rospy.Subscriber("end_effector_command_pose_stamped", PoseStamped, callback)
	rospy.Subscriber("end_effector_command_check", String, commandCheckCallback)
	rospy.spin();
	
def main():
	rospy.init_node("ikfast_transform", anonymous=True)

	try:
		subscribe()
	except():
		pass

if __name__ == '__main__':
	main()
