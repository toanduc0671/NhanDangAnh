import paho.mqtt.publish as publish

with open("test.jpg", 'rb') as f:
	filecontent = f.read()

#f= open("test.jpg")
#filecontent = f.read()

byteArr = bytearray(filecontent)

publish.single('topic', byteArr, qos=1, hostname = "192.168.1.13")