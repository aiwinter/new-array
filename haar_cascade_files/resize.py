import urllib.request
import cv2
import numpy as np
import os
import glob

def resize():
    pic_num = 1            
    folder = "pos/"
    for (i,image_file) in enumerate(glob.iglob('cola_smith/*.jpg')):
        try:
            print(i)
            img = cv2.imread(image_file,cv2.IMREAD_GRAYSCALE)
            #img = cv2.imread(image_file,cv2)
            height, width = img.shape[:2]
            if (width > height):
                max_height = 50
                max_width = 50
                scaling_factor = max_width / float(width)
                resized_image  = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
                height, width = img.shape[:2]
                cv2.imwrite(folder+str(pic_num)+".jpg",resized_image)
                pic_num += 1
            
        except Exception as e:
            print(str(e))  

resize()