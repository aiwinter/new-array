import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

# Callback Function for Trackbar (but do not any work)
def nothing(*arg):
    pass

# Code here
def SimpleTrackbar(Image, WindowName):
 # Generate trackbar Window Name
 TrackbarName = WindowName + "Trackbar"
 TrackbarNameBlur = WindowName + 'TrackbarBlur'
 # Make Window and Trackbar
 cv2.namedWindow(WindowName)
 cv2.createTrackbar(TrackbarName, WindowName, 0, 255, nothing)
 cv2.createTrackbar(TrackbarNameBlur, WindowName, 1, 55, nothing)
 hh = 'Hue High'
 hl = 'Hue Low'
 sh = 'Saturation High'
 sl = 'Saturation Low'
 vh = 'Value High'
 vl = 'Value Low'
 cv2.createTrackbar(hl, WindowName, 0, 179, nothing)
 cv2.createTrackbar(hh, WindowName, 0, 179, nothing)
 cv2.createTrackbar(sl, WindowName, 0, 255, nothing)
 cv2.createTrackbar(sh, WindowName, 0, 255, nothing)
 cv2.createTrackbar(vl, WindowName, 0, 255, nothing)
 cv2.createTrackbar(vh, WindowName, 0, 255, nothing)

 height, width = Image.shape[:2]
 max_height = 300
 max_width = 300

 # only shrink if img is bigger than required
 if max_height < height or max_width < width:
    # get scaling factor
    scaling_factor = max_height / float(height)
    if max_width/float(width) < scaling_factor:
        scaling_factor = max_width / float(width)
    # resize image
    img = cv2.resize(Image, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)


 key = cv2.waitKey()
 # Allocate destination image
 Threshold = np.zeros(img.shape, np.uint8)

 # Loop for get trackbar pos and process it
 while True:
  # Get position in trackbar
  TrackbarPos = cv2.getTrackbarPos(TrackbarName, WindowName)
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  TrackbarPosBlur = cv2.getTrackbarPos(TrackbarNameBlur, WindowName)
  hul = cv2.getTrackbarPos(hl, WindowName)
  huh = cv2.getTrackbarPos(hh, WindowName)
  sal = cv2.getTrackbarPos(sl, WindowName)
  sah = cv2.getTrackbarPos(sh, WindowName)
  val = cv2.getTrackbarPos(vl, WindowName)
  vah = cv2.getTrackbarPos(vh, WindowName)
  #make array for final values
  HSVLOW=np.array([hul,sal,val])
  HSVHIGH=np.array([huh,sah,vah])
  #create a mask for that range
  mask = cv2.inRange(hsv,HSVLOW, HSVHIGH)
  # Apply threshold
  if TrackbarPosBlur % 2 == 1:
    cv2.GaussianBlur(img, (TrackbarPosBlur, TrackbarPosBlur), 0 , Threshold)
  cv2.threshold(img, TrackbarPos, 255, cv2.THRESH_BINARY, Threshold)
  # Show in window
  res = cv2.bitwise_and(img, img, mask = mask)
  #cv2.imshow(WindowName, res)
  cv2.imshow(WindowName, Threshold)

  # If you press "ESC", it will return value
  ch = cv2.waitKey(5)
  if ch == 27:
      break

 cv2.destroyAllWindows()
 return Threshold

WindowName = 'Thresh1'
Image = cv2.imread('../images/a.jpg')

SimpleTrackbar(Image, WindowName)