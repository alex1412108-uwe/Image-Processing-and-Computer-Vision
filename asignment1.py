import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('coins1.png')

#kernel = np.ones((5,5),np.float32)/25
kernel = np.matrix([[1,0],[0,-1]])

print kernel
dst = cv2.filter2D(img,-1,kernel)

#plt.subplot(121),plt.imshow(img),plt.title('Original')
#plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
#plt.xticks([]), plt.yticks([])
#plt.show()


while True:
  cv2.imshow('coins1', img)
  key = cv2.waitKey(10)
  if key > 0:
    print key
    if key==1048603: #escape key
      exit(0)