import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../a.png')

height, width = img.shape[:2]
max_height = 2048
max_width = 2048

scaling_factor = max_width / float(width)
img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

height, width = img.shape[:2]

print height, width

mask = np.zeros(img.shape[:2],np.uint8)
 
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (1024/2, 250, width/2, height)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img),plt.colorbar(),plt.show()
