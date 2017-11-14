import cv2
import numpy as np

im = cv2.imread('../images/a.jpg')
# Convert BGR to HSV
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)
# Bitwise-AND mask and original image
res = cv2.bitwise_and(im,im, mask= mask)
cv2.imshow('im',im)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
k = cv2.waitKey(5) & 0xFF
if k == 27:

    cv2.destroyAllWindows()