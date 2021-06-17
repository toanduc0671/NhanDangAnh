# Báo cáo tuần 2
## gửi dữ liệu nén dạng zip từ ubuntu sang raspios và nhận diện khuôn mặt bằng ảnh

Thay vì gửi và nhận ảnh giữa 2 máy như trước thì trong bài báo cáo lần này em thực hiện gửi file dạng .zip từ máy Ubuntu rồi nhận và tự động giải nén đồng thời nhận diện khuôn mặt trên raspberry pi <br />

## Dưới đây là các bước demo:
### Test trường hợp nhận dạng fail:
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

![]()




![](https://raw.githubusercontent.com/toanduc0671/NhanDangAnh/main/image/week2/Biden_on_pi.png)



