import paho.mqtt.publish as publish
import json
import base64

data = {}
with open('test.png', mode='rb') as file:
    img = file.read()
#with open('test2.png', mode='rb') as file:
#    img2 = file.read()    
with open('gg.txt', mode='rb') as file:
    text = file.read()
    
data['img'] = base64.b64encode(img)
#data['img2'] = base64.b64encode(img2)
data['text'] = text
byteArr = json.dumps(data)


publish.single('nhandanganh', byteArr, qos=1, hostname = "192.168.1.16")
