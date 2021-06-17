import os
import time
while True:
    check0 = os.path.isdir('/home/pi/Desktop/gg/')
    check1 = os.path.isfile('/home/pi/Desktop/receive.zip')
    time.sleep(0.5)
    if check0 == False:
        if check1 ==True:
            os.system("unzip receive.zip")