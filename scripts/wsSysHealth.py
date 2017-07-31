#!/usr/bin/env python
import web
import rospy
from std_msgs.msg import Bool

urls = (
    '/sysHealth', 'sysHealth'
)

app = web.application(urls, globals())

class sysHealth:        
    def GET(self):
        output = 'good'
        return output

def sysHealthPublish():
    pub = rospy.Publisher('sysHealth', Bool, queue_size=10)
    rospy.init_node('sysHealth', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        pub.publish(True)
        rate.sleep()

if __name__ == "__main__":
    app.run()
    sysHealthPublish()

