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
```
## Kết quả:

![](https://raw.githubusercontent.com/toanduc0671/NhanDangAnh/main/image/Screenshot%202021-06-05%20172933.png)