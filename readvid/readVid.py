import cv2

# Open video file

filename = 'c:/path/to/file.mp4'

cap = cv2.VideoCapture(filename)
i=0
while(cpa.isOpened()):
    ret, frame = cap.read():
    if ret == False:
        break
    cv2.imwrite('kang'+str(i)'.jpg',frame)
    i += 1

cap.release()
cv.destroyAllWindows()
