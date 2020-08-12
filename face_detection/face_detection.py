import sys
import cv2

fc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

vc = cv2.VideoCapture(0)

while True:
    ret, frame = vc.read()
    k = cv2.waitKey(1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = fc.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Face Detection', frame)

video_capture.release()
cv2.destroyAllWindows()