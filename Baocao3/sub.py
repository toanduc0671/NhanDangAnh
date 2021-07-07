import paho.mqtt.client as mqtt
import base64
import json
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  client.subscribe("nhandanganh")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
  gg = json.loads(msg.payload)
  with open('image_new1.png', mode='wb') as file:
    file.write(base64.b64decode(gg['img']))
    file.close()
    print 'file image received'


  with open('newtext.txt', mode='w') as file:
    file.write(gg['text'])
    file.close()
    print 'file text received'

client = mqtt.Client()
#client.username_pw_set("toan", "haihai")
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.16", 1883, 60)

client.loop_forever()

