import numpy as np
import cv2
from matplotlib import pyplot as plt
im = cv2.imread('../a.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
plt.imshow(imgray),plt.colorbar(),plt.show() 