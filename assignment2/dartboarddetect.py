import time
import argparse
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

#---------------------------------------------------------------------------------------------------        
#if __name__ == "__main__":
def main():
    #video_source = cv2.VideoCapture(0)

    #select cascade library
    detect_cascade = cv2.CascadeClassifier('cascade_resources/dartcascade.xml')

    folder_input = 'testsamples'
    folder_output = 'results/basicdetect'

    for filename in listdir(folder_input):

        #array to store details of the image
        filenamearray = filename.split('.')

        im = cv2.imread(folder_input + '/' + filename) #gets image
        
        # Convert to grayscale
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        detect = detect_cascade.detectMultiScale(im_gray, 1.1, 1, cv2.cv.CV_HAAR_SCALE_IMAGE, (50, 50), (500,500) )
        detect_center=[]
        for (x,y,w,h) in detect:
            cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
            #find center point
            detect_center.append(x+(w/2))
            detect_center.append(y+(w/2))
            cv2.circle(im,(detect_center[0],detect_center[1]),2,(255,0,0),2)

        finalfilename = filenamearray[0] + '_basic_detect' + '.' + filenamearray[1]
        # Display the image
        cv2.imwrite( folder_output + '/' + finalfilename, im )
        #key = cv2.waitKey(0)

main()