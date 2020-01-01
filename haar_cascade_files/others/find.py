import numpy as np
import cv2

# Config and Image
painting = cv2.CascadeClassifier('smaller/cascade.xml')
img = cv2.imread('cola_smith/1498846210capt0000.jpg')

# Resize
height, width = img.shape[:2]
max_height = 1024
max_width = 1024
scaling_factor = max_width / float(width)
img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
height, width = img.shape[:2]

# More Config
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
paintings = painting.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in paintings:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()