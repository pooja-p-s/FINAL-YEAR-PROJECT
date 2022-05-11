import cv2
import numpy as np
from common import *
from skimage import feature
import streamlit as st
import matlab.engine
import sys

def each_emo(filename):
    with open(filename, 'r') as file:
        all_file = file.read().strip()  #remove extra newlines (if any)
        all_file_list = all_file.split('\n')  #make list of lines
        final_data = [[float(each_num) for each_num in line.split()] for line in all_file_list]  # make list of list 
    return final_data


def create_data():
    data = list()
    for i in range(0,7):
        data = data + each_emo(sd_lbp[i])
    return data

def sdlbp(folders):
    labels = []
    order = 0
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callSDLBP(nargout=0)
    eng.quit()
    data =  create_data()
    for folder in folders:
        images = load_images_from_folder(folder)
        for img in images:
            labels.append(emo[order])
        order = order+1
    return data,labels


def matlabfdlbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callFDLBP(nargout=0)
    eng.quit()
    
def matlabsdlbp():
    positionOfPath = 1
    sys.path.insert( positionOfPath, '/Users/poojaps/Documents/MATLAB' )
    eng = matlab.engine.start_matlab()
    eng.callSDLBP(nargout=0)
    eng.quit()