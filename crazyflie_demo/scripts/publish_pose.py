#!/usr/bin/env python

import rospy
import tf
from geometry_msgs.msg import PoseStamped

if __name__ == '__main__':
    rospy.init_node('publish_pose', anonymous=True)
    worldFrame = rospy.get_param("~worldFrame", "world")
    name = rospy.get_param("~name")
    r = rospy.get_param("~rate")
    x = rospy.get_param("~x")
    y = rospy.get_param("~y")
    z = rospy.get_param("~z")

    rate = rospy.Rate(r)

    msg = PoseStamped()
    msg.header.seq = 0
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = worldFrame
    msg.pose.position.x = x
    msg.pose.position.y = y
    msg.pose.position.z = z
    quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)
    msg.pose.orientation.x = quaternion[0]
    msg.pose.orientation.y = quaternion[1]
    msg.pose.orientation.z = quaternion[2]
    msg.pose.orientation.w = quaternion[3]

    msg2 = PoseStamped()
    msg2.header.seq = 0
    msg2.header.stamp = rospy.Time.now()
    msg2.header.frame_id = worldFrame
    msg2.pose.position.x = x - 2
    msg2.pose.position.y = y - 0.5
    msg2.pose.position.z = z - 0.5
    quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)
    msg2.pose.orientation.x = quaternion[0]
    msg2.pose.orientation.y = quaternion[1]
    msg2.pose.orientation.z = quaternion[2]
    msg2.pose.orientation.w = quaternion[3]

    msg3 = PoseStamped()
    msg3.header.seq = 0
    msg3.header.stamp = rospy.Time.now()
    msg3.header.frame_id = worldFrame
    msg3.pose.position.x = x
    msg3.pose.position.y = y - 1.5
    msg3.pose.position.z = z - 1
    quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)
    msg3.pose.orientation.x = quaternion[0]
    msg3.pose.orientation.y = quaternion[1]
    msg3.pose.orientation.z = quaternion[2]
    msg3.pose.orientation.w = quaternion[3]

    pub = rospy.Publisher(name, PoseStamped, queue_size=1)

    modder = 100

    while not rospy.is_shutdown():
        msg.header.seq += 1
        msg.header.stamp = rospy.Time.now()
        pub.publish(msg)
        # if msg.header.seq < 900:
        #     if msg.header.seq % modder == 0:
        #         rospy.loginfo("1st WAYPOINT")
        #     msg.header.seq += 1
        #     msg.header.stamp = rospy.Time.now()
        #     pub.publish(msg)
        # elif msg.header.seq < 1500:
        #     if msg2.header.seq % modder == 0:
        #         rospy.loginfo("2nd WAYPOINT")
        #     msg.header.seq += 1
        #     msg2.header.seq = msg.header.seq
        #     msg2.header.stamp = rospy.Time.now()
        #     pub.publish(msg2)
        # else:
        #     if msg3.header.seq % modder == 0:
        #         rospy.loginfo("3rd WAYPOINT")
        #     msg.header.seq += 1
        #     msg3.header.seq = msg.header.seq
        #     msg3.header.stamp = rospy.Time.now()
        #     pub.publish(msg3)
        rate.sleep()
