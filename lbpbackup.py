import cv2
import numpy as np
from common import *
from skimage import feature
import streamlit as st

lbph_bin = [-1,0, 1, 2, 3, 4, 6, 7, 8, 12, 14, 15, 16, 24, 28, 30, 31, 32, 48, 56, 60, 62, 63, 64, 96, 112, 120, 124, 126, 127, 128, 129, 131, 135, 143, 159, 191, 192, 193, 195, 199, 207, 223, 224, 225, 227, 231, 239, 240, 241, 243, 247, 248, 249, 251, 252, 253, 254,255]
bins_number = 59


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
                    
            filename = '/Users/poojaps/Desktop/project/afterlbp/' + emo[order] + '/face' + emo[order]+ str(d) + '.png'			            
            cv2.imwrite(filename, img_lbp)
            d=d+1
        order = order+1
    
def find_lbp():
    img = cv2.imread('/Users/poojaps/Desktop/project/sampleviola.png')
    #st.image(img)
    height= img.shape[0]
    width = img.shape[1]
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_lbp = np.zeros((height, width), np.uint8)
    for i in range(0, height):
        for j in range(0, width):
            img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)
    filename   = '/Users/poojaps/Desktop/project/samplelbp.png'			
    cv2.imwrite(filename, img_lbp)

def sdlbp(folders):
    d=0   
    #eps = 1e-7
    count=0
    order = 0
    histogram_list = []
    labels = []
    tempt = 0
    for folder in folders:
        d=0
        images = load_images_from_folder(folder)
        for img in images:
            height, width, _ = img.shape
            # Convert RGB image into grayscale
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Create a numpy array with the same height and width of RGB image
            img_lbp = np.zeros((height, width), np.uint8)
            reg_hist = [0] * bins_number
            for i in range(0, height):
                for j in range(0, width):
                    img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)
                    tempt = img_lbp[i, j]
                    if lbph_bin.count(tempt) > 0:
                        reg_hist[lbph_bin.index(tempt)] = reg_hist[lbph_bin.index(tempt)] + 1
                    else:
                        reg_hist[0] = reg_hist[0] + 1 
                        
            histogram_list.append(reg_hist)
            
            #(hist, _) = np.histogram(img_lbp.ravel(), bins = 257)
            #hist = hist.astype("float")
            #hist /= (hist.sum() + eps)
            #histogram_list.append(hist)
            labels.append(emo[order])       
            print(count)   
            count=count+1   
            filename = '/Users/poojaps/Desktop/project/afterlbp/' + emo[order] + '/face' + emo[order]+ str(d) + '.png'	
            #st.write(img_lbp)		            
            cv2.imwrite(filename, img_lbp)
            d=d+1      
        order = order+1
    st.write(histogram_list)
    return histogram_list, labels
    

def find_sdlbp():    
    img = cv2.imread('/Users/poojaps/Desktop/project/sampleviola.png')
    #st.image(img)
    height= img.shape[0]
    width = img.shape[1]
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_lbp = np.zeros((height, width), np.uint8)
    for i in range(0, height):
        for j in range(0, width):
            img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)
    filename   = '/Users/poojaps/Desktop/project/samplelbp.png'			
    cv2.imwrite(filename, img_lbp)
    h,f = np.histogram(img_lbp, bins=256, range=None, normed=None, weights=None, density=None)
    return h