import cv2
import imutils
import time

cam = cv2.VideoCapture(0)
time.sleep(1)
firstFrame = None
area = 500

while True:
    _,img = cam.read()
    text = "Normal"

    cv2.imshow("my_cam",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()