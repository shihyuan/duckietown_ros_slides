#!/usr/bin/env python
import rospy
from pkg_name_msgs.msg import Duckie
import random
# Initialize the node with rospy
rospy.init_node("publisher_node")
# Create publisher
publisher = rospy.Publisher("topic",Duckie,queue_size=1)
# Define Timer callback
def callback(event):
    msg = Duckie()
    msg.header.stamp = rospy.Time.now()
    msg.name = random.choice(["Shih-Yuan","Liam","Misha"])
    msg.state = random.choice([Duckie.STATE_HAPPY,Duckie.STATE_SUPER])
    publisher.publish(msg)
# Create timer 
rospy.Timer(rospy.Duration.from_sec(1.0),callback)
# spin to keep the script for exiting
rospy.spin() 