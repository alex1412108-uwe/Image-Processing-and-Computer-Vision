
import cv2
import numpy as np
import time
import math
from matplotlib import pyplot as plt

def main():
	video_feed = 'resources/3.avi'
	#video_feed = 'testvideos/seed_tape_model_semiloose2.mkv'

	video_source=cv2.VideoCapture(video_feed)
	#video_source = cv2.VideoCapture(0)
	#ret = video_source.set(3,1920) #set width
	#ret = video_source.set(4,1080) #set height

	im = setup(video_source)

	im = cleanup(im)

	while True:
		im, im_past = running_cleanup(video_source, im)

		array_ix, array_iy, array_it = find_values3(im, im_past)

		#plt.imshow(array_ix, cmap = 'gray', interpolation = 'bicubic')
		#plt.xticks([]), plt.yticks([])
		#plt.show()

		# plt.subplot(2,2,1),plt.imshow(im,cmap = 'gray')
		# plt.title('image'), plt.xticks([]), plt.yticks([])

		# plt.subplot(2,2,2),plt.imshow(im_past,cmap = 'gray')
		# plt.title('past'), plt.xticks([]), plt.yticks([])

		# plt.subplot(2,2,3),plt.imshow(array_ix,cmap = 'gray')
		# plt.title('ix'), plt.xticks([]), plt.yticks([])

		# plt.subplot(2,2,4),plt.imshow(array_iy,cmap = 'gray')
		# plt.title('iy'), plt.xticks([]), plt.yticks([])

		# plt.show()

		cv2.imshow('image', im)
		cv2.imshow('image past', im_past)
		cv2.imshow('ix', array_ix)
		cv2.imshow('iy', array_iy)
		cv2.imshow('it', array_it)
		t = 0
		# while t<1:
		key = cv2.waitKey(10)
		if key > 0:
			if key==1048603: #escape key
				exit(0)
		# 		if key==1048608: #space key
		# 			t = 2

def setup(video_source):
	im = video_source.read()[1]
	return im

def cleanup(im):
	im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	return im_gray

def running_cleanup(video_source, im):
	im_past_gray = im.copy()
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
	rows, cols = im.shape
	array_spacial = []
	array_spacial_past = []

	array_ix = np.zeros((rows,cols), np.uint8)
	array_iy = np.zeros((rows,cols), np.uint8)
	array_it = np.zeros((rows,cols), np.uint8)

	for i in xrange(0,rows-1):

		#line_it = []
		for j in range(0,cols-1):
			array_spacial = im[i][j],im[i][j+1],im[i+1][j],im[i+1][j+1]
			array_spacial_past = im_past[i][j],im_past[i][j+1],im_past[i+1][j],im_past[i+1][j+1]

			array_ix[i][j] = ((array_spacial[1] - array_spacial[0]) + (array_spacial[3] - array_spacial[2]) + (array_spacial_past[1] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[2]))/4
			array_iy[i][j] = ((array_spacial[2] - array_spacial[0]) + (array_spacial[3] - array_spacial[1]) + (array_spacial_past[2] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[1]))/4
			array_it[i][j] = ((array_spacial[0] - array_spacial_past[0])+(array_spacial[1] - array_spacial_past[1])+(array_spacial[2] - array_spacial_past[2])+(array_spacial[3] - array_spacial_past[3]))/4
	return array_ix, array_iy, array_it

def find_values3(im, im_past):
	rows, cols = im.shape
	array_spacial = []
	array_spacial_past = []

	array_ix = np.zeros((rows,cols), np.uint8)
	array_iy = np.zeros((rows,cols), np.uint8)
	array_it = np.zeros((rows,cols), np.uint8)

	for i in xrange(0,rows-1):

		#line_it = []
		for j in range(0,cols-1):
			array_spacial = im.item(i,j),im.item(i,j+1),im.item(i+1,j),im.item(i+1,j+1)
			array_spacial_past = im_past.item(i,j),im_past.item(i,j+1),im_past.item(i+1,j),im_past.item(i+1,j+1)

			array_ix[i][j] = ((array_spacial[1] - array_spacial[0]) + (array_spacial[3] - array_spacial[2]) + (array_spacial_past[1] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[2]))/4
			array_iy[i][j] = ((array_spacial[2] - array_spacial[0]) + (array_spacial[3] - array_spacial[1]) + (array_spacial_past[2] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[1]))/4
			array_it[i][j] = ((array_spacial[0] - array_spacial_past[0])+(array_spacial[1] - array_spacial_past[1])+(array_spacial[2] - array_spacial_past[2])+(array_spacial[3] - array_spacial_past[3]))/4
	return array_ix, array_iy, array_it

main()