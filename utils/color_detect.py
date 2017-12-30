import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt
 
img = cv2.imread('../a.png')

height, width = img.shape[:2]
max_height = 1024
max_width = 1024

scaling_factor = max_width / float(width)
img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

height, width = img.shape[:2]

print height, width

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([0, 0, 0])
upper_range = np.array([0, 255, 255])

mask = cv2.inRange(hsv, lower_range, upper_range)

#cv2.imshow('image', img)
#cv2.imshow('mask', mask)
plt.imshow(mask),plt.colorbar(),plt.show()
 
while(True):
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
 
cv2.destroyAllWindows()
