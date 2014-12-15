
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


	im = setup(video_source)

	im = cleanup(im)

	rows, cols = im.shape

	regions_to_detect = []
	for i in range(10, cols-5, cols/10):
	 	for j in range(10, rows-5, rows/10):
	 		regions_to_detect.append([i,j])

	region_size = [3,3]

	region_list = regions(im, regions_to_detect, region_size)
	
	while True:
		region_list_past = region_list.copy()

		im, im_past = running_cleanup(video_source, im)

		region_list = regions(im, regions_to_detect, region_size)

		results_list = compute_regions(region_list, region_list_past)

		vector_list = compute_lk(results_list)

		#print vector_list[0][0][0]

		for i in range(0,len(vector_list)):
			#cv2.imshow(str(i) + 'ix', results_list[i][0])
			#cv2.imshow(str(i) + 'iy', results_list[i][1])
			#cv2.imshow(str(i) + 'it', results_list[i][2])
			#cv2.line(im,(0,regions_to_detect[i][0] + vector_list[i][0][0]),(511,511),(255,0,0),5)
			cv2.line(im, (regions_to_detect[i][0], regions_to_detect[i][1]), (regions_to_detect[i][0] + vector_list[i][0][0], regions_to_detect[i][1] + vector_list[i][1][0]),(255,0,0))


		aspect_multiplier = float(rows)/cols

		print aspect_multiplier

		im_resize = cv2.resize(im, (1200,int(1200 * aspect_multiplier)))#, fx=2, fy=2)

		cv2.imshow('image', im)
		cv2.imshow('image_large', im_resize)
		#cv2.imshow('image past', im_past)
		#cv2.imshow('ix', array_ix)
		#cv2.imshow('iy', array_iy)
		#cv2.imshow('it', array_it)
		cv2.waitKey(0)
		exit(0)
		key = cv2.waitKey(20)
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
	if im == None:
		print "end of video"
		exit(0)
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
		for j in xrange(0,cols-1):
			array_spacial = im[i][j],im[i][j+1],im[i+1][j],im[i+1][j+1]
			array_spacial_past = im_past[i][j],im_past[i][j+1],im_past[i+1][j],im_past[i+1][j+1]

			array_ix[i][j] = ((array_spacial[1] - array_spacial[0]) + (array_spacial[3] - array_spacial[2]) + (array_spacial_past[1] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[2]))/4
			array_iy[i][j] = ((array_spacial[2] - array_spacial[0]) + (array_spacial[3] - array_spacial[1]) + (array_spacial_past[2] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[1]))/4
			array_it[i][j] = ((array_spacial[0] - array_spacial_past[0])+(array_spacial[1] - array_spacial_past[1])+(array_spacial[2] - array_spacial_past[2])+(array_spacial[3] - array_spacial_past[3]))/4
	return array_ix, array_iy, array_it

#utilizes itemset to reduce computation power required
def find_values3(im, im_past):
	rows, cols = im.shape
	array_spacial = []
	array_spacial_past = []

	array_ix = np.zeros((rows-1,cols-1), np.uint8)
	array_iy = np.zeros((rows-1,cols-1), np.uint8)
	array_it = np.zeros((rows-1,cols-1), np.uint8)

	for i in xrange(0,rows-1):

		#line_it = []
		for j in xrange(0,cols-1):
			array_spacial = im.item(i,j),im.item(i,j+1),im.item(i+1,j),im.item(i+1,j+1)
			array_spacial_past = im_past.item(i,j),im_past.item(i,j+1),im_past.item(i+1,j),im_past.item(i+1,j+1)

			array_ix[i][j] = ((array_spacial[1] - array_spacial[0]) + (array_spacial[3] - array_spacial[2]) + (array_spacial_past[1] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[2]))/4
			array_iy[i][j] = ((array_spacial[2] - array_spacial[0]) + (array_spacial[3] - array_spacial[1]) + (array_spacial_past[2] - array_spacial_past[0]) + (array_spacial_past[3] - array_spacial_past[1]))/4
			array_it[i][j] = ((array_spacial[0] - array_spacial_past[0])+(array_spacial[1] - array_spacial_past[1])+(array_spacial[2] - array_spacial_past[2])+(array_spacial[3] - array_spacial_past[3]))/4

	return array_ix, array_iy, array_it

def regions(im, regions_to_detect, region_size):
	region_list = np.empty((len(regions_to_detect),region_size[0],region_size[1]),np.uint8)
	for i in range(0, len(regions_to_detect)):
		region_individual = im[regions_to_detect[i][1]:regions_to_detect[i][1] + region_size[1], regions_to_detect[i][0]:regions_to_detect[i][0] + region_size[0]] # format is y1:y2:x1:x2
		region_list[i] = region_individual

	return region_list

def compute_regions(region_list, region_list_past):
	results_list = np.empty((len(region_list),3,len(region_list[0])-1,len(region_list[0][0])-1),np.uint8)
	for i in range(0,len(region_list)):
		array_ix, array_iy, array_it = find_values3(region_list[i], region_list_past[i])
		results_list[i] = [array_ix, array_iy, array_it]

	return results_list

def compute_lk(results_list):
	vector_list = np.empty((len(results_list),2,1),np.uint8)
	for i in range(0,len(results_list)):
		ix = np.reshape(results_list[i][0], 4)
		iy = np.reshape(results_list[i][1], 4)
		it = np.reshape(results_list[i][2], 4)

		A = np.array([[(ix[0]**2 + ix[1]**2 + ix[2]**2 + ix[3]**2)/4, (ix[0]*iy[0] + ix[1]*iy[1] + ix[2]*iy[2] + ix[3]*iy[3])/4], [(ix[0]*iy[0] + ix[1]*iy[1] + ix[2]*iy[2] + ix[3]*iy[3])/4, (iy[0]**2 + iy[1]**2 + iy[2]**2 + iy[3]**2)/4]])
		b = np.array([[-1 * (ix[0]*it[0] + ix[1]*it[1] + ix[2]*it[2] + ix[3]*it[3])/4], [-1 * (iy[0]*it[0] + iy[1]*it[1] + iy[2]*it[2] + iy[3]*it[3])/4]])
		#calculate inverse of A
		try:
			#calculate product of inverse of A and b
			Ainv = np.linalg.inv(A)
			v = np.dot(Ainv, b)
		except:
			#if a singularity occurs this zeroes the vector, the print statement below is used for being alerted of singularities
			#print "singularity at coordinate pair " + str(i+1)
			v = np.array([[0],[0]])


		#clean out extreme to reduce noise.
		if v[0] > 250:
			v = np.array([[0],[0]])

		elif v[1] > 250:
			v = np.array([[0],[0]])

		vector_list[i] = v

	return vector_list

#def block_matrix_inverse(matrix):


main()