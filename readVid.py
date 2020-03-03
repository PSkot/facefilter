import cv2
import time
from mtcnn import MTCNN
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, Circle

# Open video file
cap = cv2.VideoCapture(0)
detector = MTCNN()

if cap.isOpened() == False:
    print("Error opening video stream or file")
frame_rate = 10
prev = 0

while(cap.isOpened()):
    time_elapsed = time.time() - prev
    ret, frame = cap.read()

    if time_elapsed > 1./frame_rate:
        prev = time.time()

        if ret == True:
            faces = detector.detect_faces(frame)

            for face in faces:
                x, y, width, height = face['box']
                cv2.rectangle(frame, pt1 = (x, y), pt2 = (x+width, y+height), color = (0, 200, 0), thickness = 2)

            cv2.imshow('Frame', frame)
        # Press Q on keyboard to exit
            if cv2.waitKey(33) & 0xFF == ord('q'):
                break

        else:
            break

cap.release()
cv2.destroyAllWindows()
