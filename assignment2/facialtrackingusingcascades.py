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
    face_cascade = cv2.CascadeClassifier('cascade_resources/haarcascade_frontalface_alt.xml')

    video_source = cv2.VideoCapture(0)

    ret = video_source.set(3,720) #set width
    ret = video_source.set(4,980) #set height

    while True:

        im = video_source.read()[1]
        
        # Convert to grayscale
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(im_gray, 1.3, 5)
        faces_center=[]
        for (x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
            #find center point
            faces_center.append(x+(w/2))
            faces_center.append(y+(w/2))
            cv2.circle(im,(faces_center[0],faces_center[1]),2,(255,0,0),2)
        
        #find image dimensions
        im_width, im_height = im_gray.shape[:2]

        #check if faces_center has anything in it
        # if faces_center:
        #     #follow face
        #     if im_width/2 > faces_center[0]:
        #         print "go left"

        #     if im_width/2 < faces_center[0]:
        #         print "go right"

        #     if im_height/2 > faces_center[0]:
        #         print "go up"

        #     if im_height/2 < faces_center[0]:
        #         print "go down"

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

def cascade_choice(choice = 1):
    if choice == 1048625:
        face_cascade = cv2.CascadeClassifier('cascade_resources/haarcascade_frontalface_alt.xml')
        print "frontal face haar"
    elif choice == 1048626:
        face_cascade = cv2.CascadeClassifier('cascade_resources/haarcascade_eye.xml')
        print "eye haar"
    elif choice == 1048627:
        face_cascade = cv2.CascadeClassifier('cascade_resources/haarcascade_smile.xml')
        print "smile haar"
    elif choice == 1048628:
        face_cascade = cv2.CascadeClassifier('cascade_resources/lbpcascade_frontalface.xml')
        print "frontal face lbp"
    elif choice == 1048629:
        face_cascade = cv2.CascadeClassifier('cascade_resources/lbpcascade_profileface.xml')
        print "profile face lbp"
    elif choice == 1048630:
        face_cascade = cv2.CascadeClassifier('cascade_resources/lbpcascade_silverware.xml')
        print "silverware lbp"
    elif choice == 1048631:
        face_cascade = cv2.CascadeClassifier('cascade_resources/hogcascade_pedestrians.xml')
        print "pedestrian hog"
    elif choice == 1048632:
        face_cascade = cv2.CascadeClassifier('cascade_resources/inria_caltech-17.01.2013.xml')
        print "inria caltech"
    elif choice == 1048633:
        face_cascade = cv2.CascadeClassifier('cascade_resources/soft-cascade-17.12.2012.xml')
        print "soft cascade"
    else:
        print "invalid cascade selection"
        face_cascade = cv2.CascadeClassifier('cascade_resources/haarcascade_frontalface_alt.xml')
    return face_cascade
main()