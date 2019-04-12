import numpy as np
import cv2
from matplotlib import pyplot as plt
face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')

cv_image = cv2.imread('check.jpg')

gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# faces = face_cascade.detectMultiScale(
#  		cv_image,
#  		scaleFactor=1.1,
#  		minNeighbors=3,
#  		minSize=(30, 30),
#  		# flags=cv2.cv.CV_HAAR_SCALE_IMAGE
#  		)
#faces = face_cascade.detectMultiScale(gray)


x2=0
y2=0

for (x,y,w,h) in faces:
	x2 = x + w
	y2 = y + h
	face_roi = cv_image[y:y2, x:x2]
	cv2.imshow('Face Only', face_roi)
	cv2.waitKey()
	cv2.destroyAllWindows()
    # print type(cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2))
    # roi_gray = gray[y:y+h, x:x+w]
    # roi_color = img[y:y+h, x:x+w]
    # eyes = eye_cascade.detectMultiScale(roi_gray)
    # for (ex,ey,ew,eh) in eyes:
    #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# cv2.imshow('img',img)
# cv2.waitKey(0)