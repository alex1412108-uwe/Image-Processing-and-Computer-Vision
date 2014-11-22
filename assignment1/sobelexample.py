import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('coins2.png',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
#sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
#sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

kernel = np.matrix([[-1,0,1],[-2,0,2],[-1,0,1]])
kernel2 = np.matrix([[1,2,1],[0,0,0],[-1,-2,-1]])
dst = cv2.filter2D(img,cv2.CV_64F,kernel)
dst2 = cv2.filter2D(img,cv2.CV_64F,kernel2)

#cv2.imshow('test',sobely)
cv2.waitKey(0)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(dst,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(dst2,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

