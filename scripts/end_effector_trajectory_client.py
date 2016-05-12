#!/usr/bin/env python
import rospy
import baxter_interface
from std_msgs.msg import String
from baxter_core_msgs.msg import JointCommand

commandCheckPublisher = rospy.Publisher("end_effector_command_check", String, queue_size=1)
def callback(data):
        current_limb = "right"
        if not(data.names[0].find("left") == -1):
            current_limb = "left"

        limb_interface = baxter_interface.limb.Limb(current_limb)
        jointCommand = dict(zip(data.names, data.command))
        limb_interface.set_joint_positions(jointCommand)
        # publish to command subscriber to check compute
        commandCheckPublisher.publish(String("done"))
        return 0

    
def listener():
    rospy.init_node('end_effector_trajectory_client', anonymous=True)
    fine = False
    rate = rospy.Rate(1)
    while not fine | rospy.is_shutdown():
        try:
            rs = baxter_interface.RobotEnable()
            rs.enable()
            fine = True
        except(OSError):
            rospy.logwarn("Can not enable robot.Will keep trying...")
            rate.sleep()
    if rospy.is_shutdown():
        return

    rospy.Subscriber("end_effector_command_solution", JointCommand, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
