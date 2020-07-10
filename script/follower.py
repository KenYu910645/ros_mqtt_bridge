#!/usr/bin/env python
import rospy
import sys
# MQTT
from ros_mqtt_bridge import  Ros_mqtt_bridge

def main(args):
    #----- Init node ------# 
    rospy.init_node('ros_mqtt_bridge_follower', anonymous=False)
    
    # init ros_mqtt_bridge
    ros_mqtt_bridge = Ros_mqtt_bridge(client_id="mqtt_follower", broker_ip="10.0.0.1", port=1883, keepalive=10, clean_session=True)
    # ros_mqtt_bridge init publisher
    # ros_mqtt_bridge.init_publisher(ros_topic = "ros_cmd_master", mqtt_topic = "mqtt_cmd", data_type = "geometry_msgs/Twist")
    ros_mqtt_bridge.init_tf_subscriber(frame_id = "car2/map", child_id = "car2/base_link_peer",mqtt_topic="mqtt_base_link")    
    r = rospy.Rate(10) #call at 10HZ
    while (not rospy.is_shutdown()):
        r.sleep()

if __name__ == '__main__':
    try:
       main(sys.argv)
    except rospy.ROSInterruptException:
        pass
