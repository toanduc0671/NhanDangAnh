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
    if results==True:
        os.system("rm receive.zip")
        os.system("rm -r gg/")

#     time.sleep(5)
#     if check0==True & check1 ==True:
#         os.system("rm receive.zip")
#         os.system("rm -r gg/")