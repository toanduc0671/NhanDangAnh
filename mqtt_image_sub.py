import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))

  client.subscribe("topic")
  

def on_message(client, userdata, msg):
  f = open('receive.jpg','w')
  f.write(msg.payload)
  f.close()
  print 'image received'
  
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.13", 1883, 60)

client.loop_forever()