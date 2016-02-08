#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class SelfTalkingNode(object):
    def __init__(self):
        # Initialize publisher
        self.pub_topic = rospy.Publisher("~topic_name",String, queue_size=1)
        # Create a timer that calls the cbTimer method every 1.0 second
        self.timer = rospy.Timer(rospy.Duration.from_sec(1.0),self.cbTimer)
        # Initailize a subscriber
        self.sub_topic = rospy.Subscriber("~topic_name", String, self.cbTopic, queue_size=1)

    def cbTimer(self,event):
        # Create the message
        msg = String()
        msg.data = "Hello, Duckietown!"
        self.pub_topic.publish(msg)

    def cbTopic(self,msg):
        # Print the received msg
        rospy.loginfo(msg)

if __name__ == '__main__':
    # Initialize the node with rospy
    rospy.init_node('node_name', anonymous=False)
    # Create a SelfTalkingNode object
    self_talking_node = SelfTalkingNode()
    # Keep this script from exiting to keep the node alive.
    rospy.spin()