import paho.mqtt.client as mqtt
import os
import time

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic")

def on_message(client, userdata, msg):
  f = open('receive.zip','w')
  f.write(msg.payload)
  f.close()
  print 'file received'

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.12", 1883, 60)

client.loop_forever()