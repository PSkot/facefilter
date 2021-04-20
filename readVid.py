import cv2
import time
import numpy as np
from mtcnn import MTCNN
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, Circle

# Open video file
cap = cv2.VideoCapture(0)
mask = cv2.imread('mask.png')
mask = cv2.resize(mask, (mask.shape[0]//12, mask.shape[1]//50))
detector = MTCNN()
alpha_s = mask[:, :, 2] / 255.0
alpha_l = 1.0 - alpha_s
if cap.isOpened() == False:
    print("Error opening video stream or file")

frame_rate = 20
prev = 0

while(cap.isOpened()):
    time_elapsed = time.time() - prev
    ret, frame = cap.read()
    added = frame.copy()
    if time_elapsed > 1./frame_rate:
        prev = time.time()

        if ret == True:
            faces = detector.detect_faces(frame)


            for face in faces:
                x, y, width, height = face['box']

                y_offset = y + 20
                x_offset = x - 25
                y1, y2 = y_offset, y_offset + mask.shape[0]
                x1, x2 = x_offset, x_offset + mask.shape[1]

                #cv2.rectangle(frame, pt1 = (x, y), pt2 = (x+width, y+height), color = (0, 200, 0), thickness = 2)

            try:
                for c in range(0,3):
                    added[y1:y2, x1:x2,c] = (alpha_s * mask[:, :, c] + alpha_l * frame[y1:y2, x1:x2, c])
                cv2.imshow('Frame', added)

            except NameError:
                cv2.imshow('Frame', frame)
        # Press Q on keyboard to exit
            if cv2.waitKey(33) & 0xFF == ord('q'):
                break

        else:
            break

cap.release()
cv2.destroyAllWindows()
