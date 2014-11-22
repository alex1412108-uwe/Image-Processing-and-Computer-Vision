import cv2
import numpy as np
np.set_printoptions(threshold=np.nan)
from matplotlib import pyplot as plt

filename = 'coins2_sobel.png'
filenamearray = filename.split('.')

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,img_thresh = cv2.threshold(img,200,255,cv2.THRESH_BINARY)


cv2.imshow(filenamearray[0] + '_sobel_horizontal', img_thresh)
#cv2.imshow(filenamearray[0] + '_sobel_vertical', img_final2)
#cv2.imshow(filenamearray[0] + '_sobel', img_final3)
cv2.waitKey(0)
cv2.destroyAllWindows()

#finalfilename = filenamearray[0] + '_sobel' + '.' + filenamearray[1]
#cv2.imwrite(finalfilename, img_final3)