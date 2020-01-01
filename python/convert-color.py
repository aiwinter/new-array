import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('a.png')
height, width = img.shape[:2]
max_height = 1024
max_width = 1024
scaling_factor = max_width / float(width)
img = cv2.resize(img, None, fx=scaling_factor,
                 fy=scaling_factor, interpolation=cv2.INTER_AREA)
height, width = img.shape[:2]
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)
# s.fill(255)
# v.fill(255)
print(height, width)
hsv_image = cv2.merge([h, s, v])
out = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
edges = cv2.Canny(hsv_image, height, width)

#shiftedH = h.clone()
cv2.imshow('edges', edges)
#cv2.imshow('hsv_image', hsv_image)
#cv2.imshow('out', out)
#cv2.imshow('h', h)
#cv2.imshow('s', s)
#cv2.imshow('v', v)

cv2.waitKey()

# plt.imshow(h),plt.colorbar(),plt.show()
