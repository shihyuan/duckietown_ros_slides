#!/usr/bin/env python
import rospy
from pkg_name_msgs.msg import Duckie
# Define callback functoin
def callback(msg):
	rospy.loginfo("%s is %s." %(msg.name,msg.state))
# Initialize the node with rospy
rospy.init_node("subscriber_node")
# Create subscriber
subscriber = rospy.Subscriber("topic", Duckie, callback)

rospy.spin() #Keeps the script for exiting