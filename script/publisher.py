#!/usr/bin/env python
import rospy
import sys
# ROS msg and libraries
from nav_msgs.msg import OccupancyGrid, Path # Global map 
from geometry_msgs.msg import Point, PoseArray, PoseStamped, Pose2D, Pose,PoseWithCovarianceStamped, Quaternion, Twist# Global path
from visualization_msgs.msg import Marker, MarkerArray # Debug drawing
from std_msgs.msg import String
import tf
# MQTT
from lucky_utility.mqtt.lib_mqtt import MQTT_OBJ
import time

class Ros_mqtt_bridge():
    def __init__(self, client_id , broker_ip , port , keepalive, clean_session):
        self.mqtt_obj = MQTT_OBJ(client_id, broker_ip, port, keepalive, clean_session)
    
    def publisher_cb(self, data):# This is Ros topic call back
        rc = mqtt_obj.publish("topic_1_to_2", "How are you doing today ?," + str(time.time()), qos = 0, retain = False) # non-blocking msg

    def topic_CB(client, userdata, message):# Callback fucntion
        print("[mqtt_example] topic_CB :  " + str(message.payload) + "(Q" + str(message.qos) + ", R" + str(message.retain) + ")")




    def init_mqtt_publisher(self, ros_topic, mqtt_obj, mqtt_topic, data_type):
        '''
        subscribe content in ros_topic , and relay it to MQTT topic and publish
        '''
        rospy.Subscriber("topic_cmd", data_type, publisher_cb)

def main(args):
    # ------Init MQTT Connection ------ #
    Ros_mqtt_bridge(client_id="solamr_1", broker_ip="broker.hivemq.com", port=1883, keepalive=10, clean_session=True)
    # MQTT subscribe
    init_mqtt_publisher("topic_cmd", "topic1_1_to_2", Twist)
    
    #----- Init node ------# 
    # Name of this node, anonymous means name will be auto generated.
    rospy.init_node('ros_mqtt_bridge', anonymous=False)
    #----- MQTT bridge publisher -------# 
    
    # Publish to 
    mqtt_obj.add_subscriber([("topic_2_to_1", 0, topic_CB)])
    pub_1 = rospy.Publisher('topic_reply'  , String ,queue_size = 10,  latch=True)
    
    r = rospy.Rate(10) #call at 10HZ
    while (not rospy.is_shutdown()):
        # Publish msg
        pub_1.publish(p)
        r.sleep()

if __name__ == '__main__':
    try:
       main(sys.argv)
    except rospy.ROSInterruptException:
        pass
