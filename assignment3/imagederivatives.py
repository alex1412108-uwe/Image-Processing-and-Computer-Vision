
import cv2
import numpy as np
import time
import math

def main():
	video_feed = 'resources/2.mov'
	#video_feed = 'testvideos/seed_tape_model_semiloose2.mkv'

	video_source=cv2.VideoCapture(video_feed)
	#video_source = cv2.VideoCapture(0)
	#ret = video_source.set(3,1920) #set width
	#ret = video_source.set(4,1080) #set height

	im, im_past = setup(video_source)

	im, im_past = cleanup(im)

	array_ix, array_iy, array_it = find_values(im, im_past)


def setup(video_source):
	im = video_source.read()[1]
	im_past = list(im)
	return im, im_past

def cleanup(im):
	im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	im_past_gray = list(im_gray)
	return im_gray, im_past_gray

def find_values(im, im_past):
	array_spacial = []
	array_spacial_past = []

	array_ix = []
	array_iy = []
	array_it = []

	for i in range(0,len(im)-1):
		line_ix = []
		line_iy = []
		#line_it = []
		for j in range(0,len(im[0])-1):
			array_spacial = im_past[i][j],im[i][j+1],im[i+1][j],im[i+1][j+1]
			array_spacial_past = im_past[i][j],im_past[i][j+1],im_past[i+1][j],im_past[i+1][j+1]

			line_ix.append(((array_spacial[1] - array_spacial[0]) + (array_spacial[3] - array_spacial[2]) + (array_spacial_past[1] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[2]))/4)
			line_iy.append(((array_spacial[2] - array_spacial[0]) + (array_spacial[3] - array_spacial[1]) + (array_spacial_past[2] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[1]))/4)
			#line_it.append((sum(array_spacial - array_spacial_past))/4)

		array_ix.append(line_ix)
		array_iy.append(line_iy)
		#array_it.append(line_it)

	return array_ix, array_iy, array_it

main()