import cv2
import numpy as np
np.set_printoptions(threshold=np.nan)
from matplotlib import pyplot as plt

img = cv2.imread('coins1.png')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#kernel = np.ones((5,5),np.float32)/25
kernel = np.matrix([[1,0],[0,-1]])
kernel2 = 0
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
while True:

  dst = cv2.filter2D(img,cv2.CV_64F,kernel)
  if hasattr(kernel2, "__len__"):
    dst2 = cv2.filter2D(img,cv2.CV_64F,kernel2)

  #print dst.shape[0]
      


  cv2.imshow('coins1', np.uint8(np.absolute(dst)))
  if hasattr(kernel2, "__len__"):
    cv2.imshow('coins1.1', np.uint8(np.absolute(dst2)))

  key = cv2.waitKey(10)
  if key > 0:
    print key
    if key==1048603: #escape key
      #for i in range(0, len(dst)):
        #for j in range(0, dst.shape[0]):
          #print j
      exit(0)
    if key==1048625: #1
      print 'roberts operator part 1'
      kernel = np.matrix([[1,0],[0,-1]])
      kernel2 = 0
    if key==1048626: #2
      print 'roberts operator part 2'
      kernel = np.matrix([[0,1],[-1,0]])
      kernel2 = 0
    if key==1048627: #3
      print 'roberts operator combined'
      kernel = np.matrix([[1,0],[0,-1]])
      kernel2 = np.matrix([[0,1],[-1,0]])
    if key==1048628: #4
      print 'sobel horizontal'
      kernel = np.matrix([[-1,0,1],[-2,0,2],[-1,0,1]])
      kernel2 = 0
    if key==1048629: #5
      print 'sobel vertical'
      kernel = np.matrix([[1,2,1],[0,0,0],[-1,-2,-1]])
      kernel2 = 0
    if key==1048630: #6
      print 'sobel combined'
      kernel = np.matrix([[-1,0,1],[-2,0,2],[-1,0,1]])
      kernel2 = np.matrix([[1,2,1],[0,0,0],[-1,-2,-1]])
    if key==1048631: #7
      print 'blurry'
      kernel = np.ones((5,5),np.float32)/25
      kernel2 = 0
    if key==1048632: #8
      kernel = np.matrix([0])
      kernel2 = 0
    if key==1048633: #9
      kernel = np.matrix([0])
      kernel2 = 0