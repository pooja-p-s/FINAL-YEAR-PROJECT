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

def train_test(data,labels,modelname): 
    #svm
    
    lsvc = LinearSVC(penalty='l2', loss='squared_hinge', 
                     dual=True, tol=0.0011, C=1.0, multi_class='ovr', 
                     fit_intercept=True, intercept_scaling=1, 
                     class_weight=None, verbose=0, random_state=None, 
                     max_iter=1000)
    #split 80-20
    xtrain,xtest,ytrain,ytest = train_test_split(data,labels,random_state=109,train_size=0.8) 
    st.write('Testing...')
    
    lsvc.fit(xtrain,ytrain)
    # save the model to disk
    filename = "/Users/poojaps/Desktop/project/models/" + modelname + ".sav"
    
    pickle.dump(lsvc, open(filename, 'wb'))
    #train
    ypred = lsvc.predict(xtest)
    cm = confusion_matrix(ytest, ypred)
    st.header("CONFUSION MATRIX") 
    st.write(cm)
    report = classification_report(ytest, ypred, output_dict=True )
    st.header("CLASSIFICATION REPORT") 
    print(classification_report(ytest, ypred))
    
    st.table((dict(list(report.items())[:7])))
    classifier_predictions = lsvc.predict(xtest)
    acc = "{:.2f}".format(accuracy_score(ytest, classifier_predictions)*100)
    st.write('**Accuracy** : ',acc,'%')
    return lsvc
    
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
    
st.title("FACIAL EMOTION RECOGNITION STUDY OF SPATIAL AND FREQUENCY DOMAIN MODELS")

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
    data=[]
    labels=[]
    st.write('Training...')
    if d=="Spatial Domain":
        if fd=="Local Binary Pattern (LBP)":
            option = 10
            st.write("Spatial Domain using LBP")
            data,labels = spa_lbp()
            modelname = "SDLBP"
        elif fd=="Three Patch LBP":
            option = 11
            st.write("Spatial Domain using TPLBP")
            data,labels = spa_tplbp()
            modelname = "SDTPLBP"
        elif fd=="Four Patch LBP":
            option = 12
            st.write("Spatial Domain using FPLBP")
            data,labels = spa_fplbp()
            modelname = "SDFPLBP"
        else:
            option = 13
            st.write("Spatial Domain using fusion of TPLBP & FPLBP")
            data,labels = spa_feature_fusion()
            modelname = "SDFUSION"
             
    else:
        if fd=="Local Binary Pattern (LBP)":
            option = 20
            st.write("Frequency Domain using LBP")
            data,labels = freq_lbp()
            modelname = "FDLBP"
        elif fd=="Three Patch LBP":
            option = 21
            st.write("Frequency Domain using TPLBP")
            data,labels = freq_tp()
            modelname = "FDTPLBP"
        elif fd=="Four Patch LBP":
            option = 22
            st.write("Frequency Domain using FPLBP")
            data,labels = freq_fp()
            modelname = "FDFPLBP"
        else:
            option = 23
            st.write("using fusion of TPLBP & FPLBP")
            d1,l1 = freq_tp()
            d2,l2 = freq_fp()
            st.write(len(d1),len(l1))
            st.write(len(d2),len(l2))
            data = data_fusion(d1,d2)
            labels = l1
            modelname = "FDFUSION"
            
    lsvc = train_test(data,labels,modelname)
    st.write("**Runtime for Training and Testing** : %s sec" % "{:.2f}".format((time.time() - start_time)))
