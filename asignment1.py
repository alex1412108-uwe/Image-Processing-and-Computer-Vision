import cv2
import numpy as np
np.set_printoptions(threshold=np.nan)
from matplotlib import pyplot as plt

#name of image
filename = 'coins2.png'
#array to store details of the image
filenamearray = filename.split('.')

img = cv2.imread(filename,0) #gets image and greyscales it
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #can be used to greyscale image if the original is grabbed above

#kernels for sobel
#horizontal
kernel = np.matrix([[-1,0,1],[-2,0,2],[-1,0,1]])
#vertical
kernel2 = np.matrix([[1,2,1],[0,0,0],[-1,-2,-1]])

#applies kernels to the image
#uses a 64 bit color space to avoid loosing negatives
img_final1 = cv2.filter2D(img,cv2.CV_64F,kernel)
img_final2 = cv2.filter2D(img,cv2.CV_64F,kernel2)
img_final3 = img_final1 **2 + img_final2 **2

#sets up the window for displaying the images and cmaps
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2),plt.imshow(img_final3,cmap = 'gray')
plt.title('magnitude'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3),plt.imshow(img_final1,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4),plt.imshow(img_final2,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

#displays the result
plt.show()
#cv2.suptitle('test')

#saves using the details of the image
finalfilename = filenamearray[0] + '_sobel' + '.' + filenamearray[1]
cv2.imwrite(finalfilename, img_final3)



#cv2.imshow(filenamearray[0] + '_sobel_horizontal', img_final1)
#cv2.imshow(filenamearray[0] + '_sobel_vertical', img_final2)
#cv2.imshow(filenamearray[0] + '_sobel', img_final3)
#cv2.waitKey(0)
#cv2.destroyAllWindows()