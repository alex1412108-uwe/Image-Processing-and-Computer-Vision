import cv2
import numpy as np
np.set_printoptions(threshold=np.nan)
from matplotlib import pyplot as plt

#name of image
filename = 'coins2.png'
#array to store details of the image
filenamearray = filename.split('.')

img = cv2.imread(filename) #gets image and greyscales it
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #can be used to greyscale image if the original is grabbed above

#kernels for sobel
#horizontal
kernel = np.matrix([[-1,0,1],[-2,0,2],[-1,0,1]])
#vertical
kernel2 = np.matrix([[1,2,1],[0,0,0],[-1,-2,-1]])

#applies kernels to the image
#uses a 64 bit color space to avoid loosing negatives
img_final1 = cv2.filter2D(img_grey,cv2.CV_64F,kernel)
img_final2 = cv2.filter2D(img_grey,cv2.CV_64F,kernel2)
img_final3 = abs(img_final1) + abs(img_final2)

#sets up the window for displaying the images and cmaps

plt.subplot(3,3,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('original'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,4),plt.imshow(img_grey,cmap = 'gray')
plt.title('greyscale'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,3),plt.imshow(img_final3,cmap = 'gray')
plt.title('magnitude'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,6),plt.imshow(img_final3)
plt.title('colortest'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,2),plt.imshow(img_final1,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,5),plt.imshow(img_final2,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

#displays the result
plt.show()

#cv2.suptitle('test')

#generates a name for the files to be saved
finalfilename = filenamearray[0] + '_sobel_magnitude' + '.' + filenamearray[1]

#saves the file
plt.imshow(img_final3,cmap = 'gray')
plt.savefig(finalfilename)