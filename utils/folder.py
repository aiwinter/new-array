import glob
import cv2
from store_images import store_raw_images

for (i,image_file) in enumerate(glob.iglob('84 photos/*.jpg')):
        process(image_file, i)  