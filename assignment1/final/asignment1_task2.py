import cv2
import numpy as np
np.set_printoptions(threshold=np.nan)
from matplotlib import pyplot as plt
import math

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
img_horizontal = cv2.filter2D(img_grey,cv2.CV_64F,kernel)
img_vertical= cv2.filter2D(img_grey,cv2.CV_64F,kernel2)
img_magnitude = abs(img_horizontal) + abs(img_vertical)
img_mag,img_angle = cv2.cartToPolar(img_horizontal,img_vertical)

#sets up the window for displaying the images and cmaps

plt.subplot(3,3,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('original'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,4),plt.imshow(img_grey,cmap = 'gray')
plt.title('greyscale'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,3),plt.imshow(img_magnitude,cmap = 'gray')
plt.title('magnitude'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,6),plt.imshow(img_angle,cmap = 'gray')
plt.title('angle'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,2),plt.imshow(img_horizontal,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,5),plt.imshow(img_vertical,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])


#plt.subplot(3,3,7),plt.hist(img_angle, 50, normed=1, facecolor='g', alpha=0.75)

#print img_angle

#displays the result
#plt.show()

#cv2.suptitle('test')

#generates a name for the files to be saved
finalfilename = filenamearray[0] + '_sobel_magnitude' + '.' + filenamearray[1]
finalfilename2 = filenamearray[0] + '_sobel_angle' + '.' + 'txt'

#saves the file
plt.imshow(img_magnitude,cmap = 'gray'),plt.xticks([]), plt.yticks([])
#plt.show()
plt.savefig(finalfilename)

radius_minimum = 100 
radius_maximum = 500
R=10



img_2 = cv2.imread("coins3_sobel_magnitude.png") 
grey = cv2.imread("coins3_sobel_magnitude.png",0) #0 for grayscale

#print img_2
num = 0
ret, thresh = cv2.threshold(grey,90,1,cv2.THRESH_BINARY)
Hough_accumulation = thresh
print len(thresh)
print len(thresh[1])
#print thresh[1][1]
#print Hough_accumulation
for i in range(0,len(thresh)-300):
	for j in range(0,len(thresh[i])-400):
		#if thresh[i][j] == 1:
			#for R in xrange(radius_minimum,radius_maximum):
				
			#if (img_angle[i][j] != [255 255 255]):
				#print img_angle[i][j]
		
		Hough_accumulation [i][j] = math.cos(img_angle[i][j])*R + math.sin(img_angle[i][j])*R
			#num+=1	
			#Hough_accumulation [i][j] = 


		




#cv2.imshow("thresh",Hough_accumulation)

cv2.waitKey(0)


