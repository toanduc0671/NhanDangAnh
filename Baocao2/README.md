# Báo cáo tuần 2
## gửi dữ liệu nén dạng zip từ ubuntu sang raspios và nhận diện khuôn mặt bằng ảnh

Thay vì gửi và nhận ảnh giữa 2 máy như trước thì trong bài báo cáo lần này em thực hiện gửi file dạng .zip từ máy Ubuntu rồi nhận và tự động giải nén đồng thời nhận diện khuôn mặt trên raspberry pi <br />

## Dưới đây là các bước demo:
### Test trường hợp nhận dạng fail:

### Trên máy ubuntu:

**Ảnh trên ubuntu**: <br />
![](https://raw.githubusercontent.com/toanduc0671/NhanDangAnh/main/image/week2/Chris_on_ubuntu.png)

```bash
$ python3 mqtt_image_pub.py
```

```python
import paho.mqtt.publish as publish
import os
import time

os.system("zip -r dulieu.zip gg")
time.sleep(0.5)

with open("dulieu.zip", 'rb') as f:
        filecontent = f.read()

publish.single('topic', filecontent, qos=1, hostname = "192.168.1.12")
```

Sau khi chạy file *mqtt_image_pub.py*, thư mục **gg** sẽ được nén thành dulieu.zip và đẩy sang máy raspberry pi qua bản tin mqtt 

![](https://raw.githubusercontent.com/toanduc0671/NhanDangAnh/main/image/week2/run_pub.png)

---------------------------------------------------------
### Trên máy raspberrypi:

Tại raspberry pi, mqtt_image_sub.py đã được chạy từ trước để subcribe tới broker mqtt. Sau khi chạy file public trên bên ubuntu thì raspberry pi sẽ báo nhận được file dulieu.zip. <br />
![](https://raw.githubusercontent.com/toanduc0671/NhanDangAnh/main/image/week2/run_sub.png) <br />

```python
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
```

**Ảnh trên raspberry pi**: <br />
![](https://raw.githubusercontent.com/toanduc0671/NhanDangAnh/main/image/week2/Biden_on_pi.png)
```bash
$ python face_recognize.py
```
Cũng giống như file *mqtt_image_sub.py*, ở trên raspberry pi được chạy sẵn cả file face_recognize.py nên chỉ cần tại máy ubuntu gửi file nén sang sẽ tự động nhận dạng khuôn mặt trong ảnh. <br />

Ở đây em sử dụng thư viện dlib OpenCV và framework face-recognition [https://pypi.org/project/face-recognition/](https://pypi.org/project/face-recognition/). <br />
Em thấy sử dụng model này, thư viện của nó hỗ trợ tận răng 😅 không mất công train tập dữ liệu như bài lần trước em làm, và độ chính xác khá cao, em test với nhiều trường hợp đều cho ra kết quả đúng. Do không phải sử dụng những thư viện xử lý hình ảnh để train cũng giúp nó nhẹ hơn và so với việc cài đặt ở lần trước thì lần này dễ dàng và nhanh hơn rất nhiều. <br />


```python
import face_recognition
import os
import time

while True:
    check0 = os.path.isdir('/home/pi/Desktop/gg/')
    check1 = os.path.isfile('/home/pi/Desktop/receive.zip')
    if check0==True:
        known_image = face_recognition.load_image_file("joebiden.png")
        unknown_image = face_recognition.load_image_file("/home/pi/Desktop/gg/chris.png")

        biden_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

        print(results)

        time.sleep(3)
        os.system("rm receive.zip")
        os.system("rm -r gg/")

#     time.sleep(5)
#     if check0==True & check1 ==True:
#         os.system("rm receive.zip")
#         os.system("rm -r gg/")
```

Trường hợp này sẽ trả về kết quả **Fail** do khuôn mặt trong 2 bức ảnh không phải của cùng một người. Sau khi trả về kết quả thì code này sẽ xoá file zip cùng với folder *gg* nhận được sau giải nén đi để đợi lần nhận dữ liệu tiếp theo từ máy ubuntu và lại tự động quá trình này. <br />

![](https://raw.githubusercontent.com/toanduc0671/NhanDangAnh/main/image/week2/face_recognition.png)

------------------------------------------------------------

### Quay trở lại máy ubuntu, thay đổi ảnh và chạy *mqtt_image_pub.py* để public ảnh sang raspberrypi

![](https://raw.githubusercontent.com/toanduc0671/NhanDangAnh/main/image/week2/Biden_on_ubuntu.png)

Lần này trên pi (vẫn trên cửa sổ chương trình chạy từ đầu) sẽ trả về kết quả là **True** : <br />
![](https://raw.githubusercontent.com/toanduc0671/NhanDangAnh/main/image/week2/face_recognition2.png)

Sau đó lại tự động xoá file zip cùng với folder sau giải nén và đợi lần gửi dữ liệu tiếp theo. 





