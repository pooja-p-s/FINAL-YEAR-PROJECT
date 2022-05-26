from dataclasses import dataclass
from re import L
import cv2 as cv2
import math
import pickle
import pandas
import psutil
import time
import itertools
import sklearn
import resource
from PIL import Image
import streamlit as st
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report,confusion_matrix,plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve, precision_score, recall_score
from sklearn.model_selection import train_test_split
from libsvm import *
from libsvm.svmutil import *
from viola import *
from lbp import *
from dct import *
from common import *
from matlbp import *
from dataprocess import  *
from tplbp import *
from capture import *
option = 0

    
def freq_lbp():
    viola(datatset_folders)
    fdlbp()
    return do_dct(fd_lbp)

def freq_tp():
    viola(datatset_folders)
    fdtplbp()
    return do_dct(tp_folders)
    
def freq_fp():
    viola(datatset_folders)
    fdfplbp()
    return do_dct(fp_folders) 

def spa_lbp():
    viola(datatset_folders)
    sdlbp()
    return spatial_data(viola_folder,1)

def spa_tplbp():
    viola(datatset_folders)
    sdtplbp()
    return spatial_data(viola_folder,2)

def spa_fplbp():
    viola(datatset_folders)
    sdfplbp()
    return spatial_data(viola_folder,3)

def spa_feature_fusion():
    d1,l1 = spa_tplbp()  
    d2,l2 = spa_fplbp() 
    st.write(len(d1),len(l1))
    st.write(len(d2),len(l2)) 
    data =  data_fusion(d1,d2)
    return data,l1
    
st.title("LIVE TEST - FACIAL EMOTION RECOGNITION ON SPATIAL AND FREQUENCY DOMAIN MODELS")

#Captured Image Processing

uploaded_file = st.camera_input("Capture a photo")
    
with st.form("choose_model"):
    domain = ["Spatial Domain","Frequency Domain"] 
    d = st.radio("Domain",domain)

    fd_list=["Local Binary Pattern (LBP)",
            "Three Patch LBP",
            "Four Patch LBP",
            "TPLBP+FPLBP"]
    fd = st.radio("Feature Descriptor",fd_list)

    submitted = st.form_submit_button("Submit")
    
if submitted:
    start_time = time.time()
    if d=="Spatial Domain":
        if fd=="Local Binary Pattern (LBP)":
            option = 10
            st.write("Spatial Domain  LBP")
            modelname = "SDLBP"
        elif fd=="Three Patch LBP":
            option = 11
            st.write("Spatial Domain using TPLBP")
            modelname = "SDTPLBP"
        elif fd=="Four Patch LBP":
            option = 12
            st.write("Spatial Domain using FPLBP")
            modelname = "SDFPLBP"
        else:
            option = 13
            st.write("Spatial Domain using fusion of TPLBP & FPLBP")
            modelname = "SDFUSION"           
    else:
        if fd=="Local Binary Pattern (LBP)":
            option = 20
            st.write("Frequency Domain using LBP")
            modelname = "FDLBP"
        elif fd=="Three Patch LBP":
            option = 21
            st.write("Frequency Domain using TPLBP")
            modelname = "FDTPLBP"
        elif fd=="Four Patch LBP":
            option = 22
            st.write("Frequency Domain using FPLBP")
            modelname = "FDFPLBP"
        else:
            option = 23
            st.write("Frequency Domain using fusion of TPLBP & FPLBP")
            modelname = "FDFUSION"
              
    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)     
       
        st.write('Processing Captured Image...')
        start_time = time.time()
        find_viola(img)
        st.write('After Viola :')
        st.image("/users/poojaps/desktop/project/sampleviola.png",width=200)
        if option==10:
            find_sdlbp()
            st.write('After LBP :')
            st.image("/users/poojaps/desktop/project/samplelbp.png",width=200)
            xval = each_emo(sampleimghist)
        elif option==11:
            find_sdtplbp() 
            st.write('After TPLBP :') 
            st.image("/users/poojaps/desktop/project/samplelbptp.png",width=200)
            xval = each_emo(sampleimghisttp)
        elif option==12:
            find_sdfplbp()
            st.write('After FPLBP :')
            st.image("/users/poojaps/desktop/project/samplelbpfp.png",width=200)
            xval = each_emo(sampleimghistfp)
        elif option==13:
            find_fdtplbp()
            st.write('After TPLBP :')
            st.image("/users/poojaps/desktop/project/samplelbptp.png",width=200)
            z1 = each_emo(sampleimghisttp)
            find_fdfplbp()
            st.write('After FPLBP :')
            st.image("/users/poojaps/desktop/project/samplelbpfp.png",width=200)
            z2 = each_emo(sampleimghistfp)
            xval = data_fusion(z1,z2)
            
        elif option==20:
            find_fdlbp()
            st.write('After LBP :')
            st.image("/users/poojaps/desktop/project/samplelbp.png",width=200)
            xval = find_dct() 
            st.write('After DCT :')
            st.image("/users/poojaps/desktop/project/sampledct.png",width=200)     
        elif option==21:
            find_fdtplbp()  
            st.write('After TPLBP :')
            st.image("/users/poojaps/desktop/project/samplelbptp.png",width=200)                 
            xval = find_dct()
            st.write('After DCT :')
            st.image("/users/poojaps/desktop/project/sampledct.png",width=200) 
        elif option==22:
            find_fdfplbp() 
            st.write('After FPLBP :')
            st.image("/users/poojaps/desktop/project/samplelbpfp.png",width=200)                  
            xval = find_dct()
            st.write('After DCT :')
            st.image("/users/poojaps/desktop/project/sampledct.png",width=200) 
        elif option==23:
            find_fdtplbp()
            st.write('After TPLBP :')
            st.image("/users/poojaps/desktop/project/samplelbptp.png",width=200)
            z1 = find_dct()
            st.write('After DCT of TPLBP:')
            st.image("/users/poojaps/desktop/project/sampledct.png",width=200) 
            find_fdfplbp()
            st.write('After FPLBP :')
            st.image("/users/poojaps/desktop/project/samplelbpfp.png",width=200)
            z2 = find_dct()
            st.write('After DCT of FPLBP :')
            st.image("/users/poojaps/desktop/project/sampledct.png",width=200) 
            xval  = data_fusion(z1,z2)
        
        lsvc = pickle.load(open("/Users/poojaps/Desktop/project/models/"+ modelname +".sav", 'rb'))
        yvalpred = lsvc.predict(xval)
        end_time = time.time()
        st.write("**Predicted Emotion** : ",yvalpred[0])   
        res = lsvc._predict_proba_lr(xval)
        for i in range(7):
            st.write(emo[i],":","{:.2f}".format(res[0][i]*100),"%")
        st.write("**Runtime for Predicting** : %s sec" % "{:.2f}".format((end_time - start_time)))

            