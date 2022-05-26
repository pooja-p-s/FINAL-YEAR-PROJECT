import cv2
import numpy as np
from common import *
from skimage import feature
import streamlit as st
import matlab.engine
import sys
from dataprocess import *

def get_pixel(img, center, x, y):
    	
	new_value = 0
	
	try:
		# local neighbourhood pixel value >=  center pixel values : set it to 1
		if img[x][y] >= center:
			new_value = 1
			
	except:
		#neighbourhood value of a center pixel value - null values - present at boundaries.
		pass
	
	return new_value

#  LBP
def lbp_calculated_pixel(img, x, y):

	center = img[x][y]

	val_ar = []
	
	# top_left
	val_ar.append(get_pixel(img, center, x-1, y-1))
	
	# top
	val_ar.append(get_pixel(img, center, x-1, y))
	
	# top_right
	val_ar.append(get_pixel(img, center, x-1, y + 1))
	
	# right
	val_ar.append(get_pixel(img, center, x, y + 1))
	
	# bottom_right
	val_ar.append(get_pixel(img, center, x + 1, y + 1))
	
	# bottom
	val_ar.append(get_pixel(img, center, x + 1, y))
	
	# bottom_left
	val_ar.append(get_pixel(img, center, x + 1, y-1))
	
	# left
	val_ar.append(get_pixel(img, center, x, y-1))
	
	# convert binary values to decimal
	power_val = [1, 2, 4, 8, 16, 32, 64, 128]

	val = 0
	
	for i in range(len(val_ar)):
		val += val_ar[i] * power_val[i]
		
	return val

def lbp(folders):
    d=0   
    order = 0
    for folder in folders:
        d=0
        images = load_images_from_folder(folder)
        for img in images:
            height, width, _ = img.shape
            # Convert RGB image into grayscale
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Create a numpy array with the same height and width of RGB image
            img_lbp = np.zeros((height, width), np.uint8)

            for i in range(0, height):
                for j in range(0, width):
                    img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)
                    
            filename = '/Users/poojaps/Desktop/project/fd/afterlbp/' + emo[order] + '/face' + emo[order]+ str(d) + '.png'			            
            cv2.imwrite(filename, img_lbp)
            d=d+1
        order = order+1
 
def fdlbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callFDLBP(nargout=0)
    eng.quit()
   
def sdlbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callSDLBP(nargout=0)
    eng.quit()
            
def find_lbp():
    img = cv2.imread('/Users/poojaps/Desktop/project/sampleviola.png')
    
    height, width, _ = img.shape
    	
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_lbp = np.zeros((height, width), np.uint8)

    for i in range(0, height):
        for j in range(0, width):
            img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)
                    
    filename = '/Users/poojaps/Desktop/project/samplelbp.png'			            
    cv2.imwrite(filename, img_lbp)		    