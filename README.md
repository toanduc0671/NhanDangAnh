# Báo cáo chuyển tập tin ảnh bằng mqtt mosquitto python

1. **set-up VMs** <br />
em thực hiện trên hai con máy ảo sử dụng virtualbox <br />
- VM1 (chạy ubuntu) - ip: 192.168.1.14
- VM2 (chạy raspios) - ip: 192.168.1.13

2. **thực hiện cài đặt**
- Mosquitto Broker <br />
```bash
$ sudo apt-get update
$ sudo apt-get install mosquitto
```
- MQTT clients <br />
```bash
$ sudo apt-get install mosquitto-clients
```

- thư viện paho-mqtt <br />
```bash
$ pip install paho-mqtt
```

3. **code**

- mqtt_image_pub.py
```python
import paho.mqtt.publish as publish

with open("test.jpg", 'rb') as f:
	filecontent = f.read()

#f= open("test.jpg")
#filecontent = f.read()
byteArr = bytearray(filecontent)

publish.single('topic', byteArr, qos=1, hostname = "192.168.1.13")
```
---------------------

- mqtt_image_sub.py

```python
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  client.subscribe("topic")
  
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
  f = open('receive.jpg','w')
  f.write(msg.payload)
  f.close()
  print 'image received'
  
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.13", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
```
## Kết quả:

![](https://raw.githubusercontent.com/toanduc0671/NhanDangAnh/main/image/Screenshot%202021-06-05%20172933.png)