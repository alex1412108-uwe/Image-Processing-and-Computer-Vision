import time
import argparse
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from matplotlib import pyplot as plt

#---------------------------------------------------------------------------------------------------        
#if __name__ == "__main__":
def main():
    #video_source = cv2.VideoCapture(0)

    #select cascade library
    detect_cascade = cv2.CascadeClassifier('cascade_resources/dartcascade.xml')

    folder_input = 'testsamples2'
    folder_output = 'results/thresholddetect'

    for filename in listdir(folder_input):

        #array to store details of the image
        filenamearray = filename.split('.')

        #gets image
        im = cv2.imread(folder_input + '/' + filename) 
        
        # Convert to grayscale
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        #im_equal = cv2.equalizeHist (im_gray)
        #ret, im_thresh = cv2.threshold(im_gray,150,255,cv2.THRESH_BINARY)
        #ret, im_thresh = cv2.threshold(im_thresh,100,255,cv2.THRESH_BINARY_INV)

        #sobel and then circle
        laplacian = cv2.Laplacian(im_gray,cv2.CV_64F)
        

        #detects the location of the object and saves it into a list
        detect = detect_cascade.detectMultiScale(im_gray, 1.1, 1, cv2.cv.CV_HAAR_SCALE_IMAGE, (50, 50), (500,500) )

        #pulls the location data out of the detection array and draws squares and circles
        for (x,y,w,h) in detect:
            detect_center=[]
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,255),2)
            #find center point
            detect_center.append(x+(w/2))
            detect_center.append(y+(w/2))
            cv2.circle(im,(detect_center[0],detect_center[1]),w/2,(0,255,255),2)

        #calculates an appropriate name
        finalfilename = filenamearray[0] + '_basic_detect' + '.' + filenamearray[1]
        # saves the image
        cv2.imwrite( folder_output + '/' + finalfilename, im )
        #cv2.imshow( "Image", np.uint8(laplacian))
        print laplacian
        converted = np.zeros_like(laplacian)
        numbermax = 0
        numbermin = 0
        for i in range(0,len(laplacian)):
            for j in range(0,len(laplacian[0])):
                if laplacian[i][j] > numbermax:
                    numbermax = laplacian[i][j]
                if laplacian[i][j] < numbermin:
                    numbermin = laplacian[i][j]
                converted[i][j] = convert_range(laplacian[i][j])
        print numbermax, numbermin
        print np.uint8(laplacian)

        cv2.imshow( "thresh", converted )
        #plt.subplot(1,1,1),plt.imshow(laplacian,cmap = 'gray')
        #plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
        #plt.show()
        key = cv2.waitKey(0)

    #displays one of the saved images
    #im_temp = cv2.imread(folder_output + '/' + 'dart0_basic_detect.jpg')
    #cv2.imshow( "Image", im_temp )
    #key = cv2.waitKey(0)

def convert_range(old_value, old_max = 1024, old_min = -1024, new_max = 255, new_min = 0):
    OldRange = (old_max - old_min)
    if OldRange == 0:
        NewValue = new_min
    else:
        NewRange = (new_max - new_min)  
        NewValue = (((old_value - old_min) * NewRange) / OldRange) + new_min
    return NewValue

main()