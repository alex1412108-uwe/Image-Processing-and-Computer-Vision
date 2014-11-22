#! /usr/bin/python

# This example shows the simplest way of getting an image from the robot's camera. The image
# is an OpenCV image so we also show how to perform edge detection on the image

#some code is based on: http://blog.derivatived.com/posts/OpenCV-Tutorial-on-Face-Tracking-Raspberry-PI-Camera/

import time
import argparse
import cv2
#import py_websockets_bot
import numpy as np

#---------------------------------------------------------------------------------------------------        
#if __name__ == "__main__":
def main():
    #video_source = cv2.VideoCapture(0)

    #select cascade library
    face_cascade = cv2.CascadeClassifier('cascade_resources/haarcascade_dartcascade.xml')


    #name of image
    filename = 'coins1.png'
    #array to store details of the image
    filenamearray = filename.split('.')

    im = cv2.imread(filename) #gets image and greyscales it
    
    # Convert to grayscale
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    detect = face_cascade.detectMultiScale(im_gray, 1.3, 5)
    detect_center=[]
    for (x,y,w,h) in detect:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        #find center point
        detect_center.append(x+(w/2))
        detect_center.append(y+(w/2))
        cv2.circle(im,(detect_center[0],detect_center[1]),2,(255,0,0),2)
    
    #find image dimensions
    im_width, im_height = im_gray.shape[:2]

    # Display the image
    cv2.imshow( "Image", im )

    #check if user presses a key
    key = cv2.waitKey(10)
    if key > 0:
        #print key
        #if key == 1113937:
            #bot.set_motor_speeds(-80.0,80.0)
        face_cascade = cascade_choice(key)
        #bot.set_motor_speeds(-80.0,80.0) #spin left
        if key == 1048603:
            # Disconnect from the robot
            bot.disconnect()
            exit(0)

main()