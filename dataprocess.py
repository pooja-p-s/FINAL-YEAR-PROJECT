import streamlit as st
import matlab.engine
import sys
import os
import cv2
from common import *

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if any([filename.endswith(x) for x in ['.jpeg', '.jpg','.png','.tiff']]):
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
    return images


def each_emo(filename):
    final_data =[]
    with open(filename, 'r') as file:
        all_file = file.read().strip()  #remove extra newlines (if any)
        all_file_list = all_file.split('\n')  #make list of lines
        final_data = [[float(each_num) for each_num in line.split()] for line in all_file_list]  # make list of list 
    return final_data


def create_data(hist):
    data = []
    for i in range(0,7):
        data = data + each_emo(hist[i])
    return data

def data_fusion(d1,d2):
    final_data=[]
    for i in range(len(d1)):
        final_data.append(d1[i]+d2[i])
    return final_data

def spatial_data(folders,type):   
    labels = []
    order = 0
    
    if type==1:
        data = create_data(hist_sd_lbp)
    elif type==2:
        data =  create_data(hist_sd_tplbp)
    elif type==3:
        data =  create_data(hist_sd_fplbp)
    
    for folder in folders:
        images = load_images_from_folder(folder)
        for img in images:
            labels.append(emo[order])
        order = order+1
    return data,labels    
    

    
