import cv2
import streamlit as st
from scipy.fftpack import dct, idct
from common import *

def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')
    
# Zig-zag pattern
def zigzagfunc(imF):
	matrix = imF
	rows = imF.shape[0]
	columns = imF.shape[1]

	solution=[[] for i in range(rows+columns-1)]

	for i in range(rows):
		for j in range(columns):
			sum=i+j
			if(sum%2 == 0):
				#add at beginning
				solution[sum].insert(0,matrix[i][j])
			else:
				#add at end of the list
				solution[sum].append(matrix[i][j])
						
	zigzag = []
	for i in solution:
		for j in i:
			zigzag.append(j)
   
	return zigzag

def do_dct(folders):
    d=0
    order = 0
    pos=0
    data = []
    labels = []

    for folder in folders:
        d=0
        images = load_images_from_folder(folder)
        for img in images:
            #convert to greyscale
            img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #convert to DCT
            imdct = dct2(img_gr)
            #save dct 
            filename = '/Users/poojaps/Desktop/project/fd/afterdct/' + emo[order] + '/face' + emo[order]+ str(d) + '.png'			
            cv2.imwrite(filename, imdct)
            #zigzag value
            zz = zigzagfunc(imdct)
            #append zigzag to feature vector list
            data.append(zz)
            #st.write(zz)
            labels.append(emo[order])
            d=d+1
        order = order+1
    return data,labels

def find_dct():
    img = cv2.imread('/Users/poojaps/Desktop/project/samplelbp.png')
    img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imdct = dct2(img_gr)
    filename = '/Users/poojaps/Desktop/project/sampledct.png'			
    cv2.imwrite(filename, imdct)
    zz = zigzagfunc(imdct)
    return zz
