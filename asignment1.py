import cv2
import numpy as np
np.set_printoptions(threshold=np.nan)
from matplotlib import pyplot as plt

filename = 'coins2.png'
filenamearray = filename.split('.')

img = cv2.imread(filename)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.matrix([[-1,0,1],[-2,0,2],[-1,0,1]])
kernel2 = np.matrix([[1,2,1],[0,0,0],[-1,-2,-1]])


img_final1 = cv2.filter2D(img,-1,kernel) #+ cv2.filter2D(img,-1,-kernel)
img_final2 = cv2.filter2D(img,-1,kernel2) #+ cv2.filter2D(img,-1,-kernel2)
img_final3 = img_final1 **2 + img_final2 **2

cv2.imshow(filenamearray[0] + '_sobel_horizontal', img_final1)
cv2.imshow(filenamearray[0] + '_sobel_vertical', img_final2)
cv2.imshow(filenamearray[0] + '_sobel', img_final3)
cv2.waitKey(0)
cv2.destroyAllWindows()

finalfilename = filenamearray[0] + '_sobel' + '.' + filenamearray[1]
cv2.imwrite(finalfilename, img_final3)