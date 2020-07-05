#!/usr/bin/env python
import rospy
import sys
# ROS msg and libraries
from geometry_msgs.msg import Twist
from std_msgs.msg import String
# MQTT
from ros_mqtt_bridge import  Ros_mqtt_bridge

def main(args):
    #----- Init node ------# 
    rospy.init_node('ros_mqtt_bridge_leader', anonymous=False)
    # init ros_mqtt_bridge
    ros_mqtt_bridge = Ros_mqtt_bridge(client_id="mqtt_leader", broker_ip="10.0.0.1", port=1883, keepalive=10, clean_session=True)

    r = rospy.Rate(10) #call at 50HZ # Need to be faster than tf hz 
    while (not rospy.is_shutdown()):
        ros_mqtt_bridge.publish_tf(frame_id = "map", child_id = "base_link", mqtt_topic = "mqtt_base_link")
        r.sleep()

if __name__ == '__main__':
    try:
       main(sys.argv)
    except rospy.ROSInterruptException:
        pass
