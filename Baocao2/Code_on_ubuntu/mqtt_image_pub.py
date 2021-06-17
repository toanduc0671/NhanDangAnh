import paho.mqtt.publish as publish
import os
import time

os.system("zip -r dulieu.zip gg")
time.sleep(0.5)

with open("dulieu.zip", 'rb') as f:
        filecontent = f.read()

#f= open("dulieu.zip")
#filecontent = f.read()
#byteArr = bytearray(filecontent)

publish.single('topic', filecontent, qos=1, hostname = "192.168.1.12")