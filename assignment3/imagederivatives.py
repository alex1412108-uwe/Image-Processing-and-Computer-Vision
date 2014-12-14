
import cv2
import numpy as np
import time
import math
from matplotlib import pyplot as plt

def main():
	video_feed = 'resources/2.mov'
	#video_feed = 'testvideos/seed_tape_model_semiloose2.mkv'

	video_source=cv2.VideoCapture(video_feed)
	#video_source = cv2.VideoCapture(0)
	#ret = video_source.set(3,1920) #set width
	#ret = video_source.set(4,1080) #set height

	im, im_past = setup(video_source)

	im, im_past = cleanup(im)

	while True:
		im, im_past = running_cleanup(video_source, im)

		array_ix, array_iy, array_it = find_values(im, im_past)

		#plt.imshow(array_ix, cmap = 'gray', interpolation = 'bicubic')
		#plt.xticks([]), plt.yticks([])
		#plt.show()

		plt.subplot(2,2,1),plt.imshow(im,cmap = 'gray')
		plt.title('image'), plt.xticks([]), plt.yticks([])

		plt.subplot(2,2,2),plt.imshow(im_past,cmap = 'gray')
		plt.title('past'), plt.xticks([]), plt.yticks([])

		plt.subplot(2,2,3),plt.imshow(array_ix,cmap = 'gray')
		plt.title('ix'), plt.xticks([]), plt.yticks([])

		plt.subplot(2,2,4),plt.imshow(array_iy,cmap = 'gray')
		plt.title('iy'), plt.xticks([]), plt.yticks([])

		plt.show()

		cv2.waitKey(0)

def setup(video_source):
	im = video_source.read()[1]
	im_past = list(im)
	return im, im_past

def cleanup(im):
	im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	im_past_gray = list(im_gray)
	return im_gray, im_past_gray

def running_cleanup(video_source, im):
	im_past_gray = list(im)
	im = video_source.read()[1]
	im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
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
		line_it = []
		for j in range(0,len(im[0])-1):
			array_spacial = im[i][j],im[i][j+1],im[i+1][j],im[i+1][j+1]
			array_spacial_past = im_past[i][j],im_past[i][j+1],im_past[i+1][j],im_past[i+1][j+1]

			line_ix.append(((array_spacial[1] - array_spacial[0]) + (array_spacial[3] - array_spacial[2]) + (array_spacial_past[1] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[2]))/4)
			line_iy.append(((array_spacial[2] - array_spacial[0]) + (array_spacial[3] - array_spacial[1]) + (array_spacial_past[2] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[1]))/4)
			line_it.append(((array_spacial[0] - array_spacial_past[0])+(array_spacial[1] - array_spacial_past[1])+(array_spacial[2] - array_spacial_past[2])+(array_spacial[3] - array_spacial_past[3]))/4)

		array_ix.append(line_ix)
		array_iy.append(line_iy)
		array_it.append(line_it)

	return array_ix, array_iy, array_it

def find_values2(im, im_past):
	array_spacial = []
	array_spacial_past = []

	array_ix = list(im)
	array_iy = list(im)
	array_it = 0#list(im)
	cv2.imshow("im", im)
	cv2.waitKey(0)
	for i in range(0,len(im)-1):

		#line_it = []
		for j in range(0,len(im[0])-1):
			array_spacial = im_past[i][j],im[i][j+1],im[i+1][j],im[i+1][j+1]
			array_spacial_past = im_past[i][j],im_past[i][j+1],im_past[i+1][j],im_past[i+1][j+1]

			array_ix[i][j] = ((array_spacial[1] - array_spacial[0]) + (array_spacial[3] - array_spacial[2]) + (array_spacial_past[1] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[2]))/4
			array_iy[i][j] = ((array_spacial[2] - array_spacial[0]) + (array_spacial[3] - array_spacial[1]) + (array_spacial_past[2] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[1]))/4
			#line_it.append((sum(array_spacial - array_spacial_past))/4)
	cv2.imshow("im", im)
	cv2.waitKey(0)
	return array_ix, array_iy, array_it

main()