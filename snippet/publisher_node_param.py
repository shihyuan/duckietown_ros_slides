#!/usr/bin/env python
import rospy
from std_msgs.msg import String #Imports msg
# Initialize the node with rospy
rospy.init_node('publisher_node')
# Create publisher
publisher = rospy.Publisher("topic",String,queue_size=1)
# Set parameter if doesn't exist
if not rospy.has_param("~place"):
    rospy.set_param("~place","Duckietown")
# Define Timer callback
def callback(event):
    # Read parameter
    place = rospy.get_param("~place")
    msg = String()
    msg.data = "Hello %s!" %(place)
    publisher.publish(msg)
# Create timer 
rospy.Timer(rospy.Duration.from_sec(1.0),callback)
# spin to keep the script for exiting
rospy.spin()