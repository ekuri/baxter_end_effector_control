#!/usr/bin/env python

import rospy
from baxter_pykdl import baxter_kinematics
from std_msgs.msg import (String, Header)
from geometry_msgs.msg import PoseStamped

commandPositionPublisher = rospy.Publisher("end_effector_command_pose_stamped_checked", PoseStamped, queue_size=1)

checked = True
def commandCheckCallback(data):
	global checked
	if not (data.data.find("done") < 0):
                rospy.loginfo("command checked")
		checked = True

lastCheckTime = None
def callback(data):
        #global checked

        #if not checked:
                #rospy.loginfo('Uncheck command.')
                #return
        #checked = False

        global lastCheckTime
        if lastCheckTime + rospy.Duration(0.1) > data.header.stamp:
            rospy.loginfo('Command frequece too high. Ignored...')
            return
        lastCheckTime = data.header.stamp
        commandPositionPublisher.publish(data)
	

def subscribe():
        rospy.Subscriber("end_effector_command_pose_stamped", PoseStamped, callback)
	rospy.Subscriber("end_effector_command_check", String, commandCheckCallback)
	rospy.spin();
	
def main():
        global lastCheckTime
        rospy.init_node("ikfast_transform", anonymous=True)
        lastCheckTime = rospy.Time.now()
	try:
		subscribe()
	except():
		pass

if __name__ == '__main__':
	main()
