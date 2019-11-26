import cv2
import os
import subprocess
import threading
import numpy as np

def camRecognize():

    face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

    #cap = cv2.VideoCapture("rtsp://192.168.0.172:888/cgi-bin/CGIProxy.fcgi?cmd=getMainVideoStreamType&usr=root&pwd=r1a2y3!")
    cap = cv2.VideoCapture("http://192.168.0.91:5001/mjpg/video.mjpg")

    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h,) in faces:
            print(x,y,w,h)

            openStream.start()
            exit()
            #color = (255, 0, 0)
            #stroke = 2
            #end_cord_x = x + w
            #end_cord_y = y + h
            #cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color, stroke)

            #openStream.start()

        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destoryAllWindows()
camRecognize = threading.Thread(target=camRecognize)

def openStream():
    os.system('start "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://192.168.0.91:5001/mjpg/video.mjpg')
openStream = threading.Thread(target=openStream)


camRecognize.start()