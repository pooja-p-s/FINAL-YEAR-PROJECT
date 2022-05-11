from dataclasses import dataclass
from re import L
import cv2
import math
import psutil
import time
import itertools
import sklearn
import resource
from PIL import Image
import streamlit as st
from sklearn import svm
from sklearn.svm import LinearSVC,SVC
from sklearn.metrics import classification_report,confusion_matrix,plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve, precision_score, recall_score
from sklearn.model_selection import train_test_split
from libsvm import *
from libsvm.svmutil import *
from viola import *
from lbp import *
from dct import *
from common import *
from fplbp import *
from tplbp import *


option = 0

def train_test(data,labels): 
    #svm
    
    lsvc = LinearSVC(penalty='l2', loss='squared_hinge', 
                     dual=True, tol=0.0011, C=1.0, multi_class='ovr', 
                     fit_intercept=True, intercept_scaling=1, 
                     class_weight=None, verbose=0, random_state=None, 
                     max_iter=1000)
    #split 80-20
    xtrain,xtest,ytrain,ytest = train_test_split(data,labels,random_state=109,train_size=0.8) 
    
    lsvc.fit(xtrain,ytrain)

    #train
    ypred = lsvc.predict(xtest)
    cm = confusion_matrix(ytest, ypred)

    
    st.header("CONFUSION MATRIX")
    st.write(cm)
    st.write(classification_report(ytest, ypred))
    report = classification_report(ytest, ypred, output_dict=True )
    st.header("CLASSIFICATION REPORT")
    
    st.table(dict(list(report.items())[:7]))
    st.table(dict(list(report.items())[7:]))
    return lsvc
    
def freq_lbp():
    viola(datatset_folders)
    matlabfdlbp()
    return do_dct(fd_lbp)

def spa_lbp():
    viola(datatset_folders)
    return sdlbp(viola_folder)

def freq_tp():
    viola(datatset_folders)
    fdtplbp()
    return do_dct(tp_folders)
    
def freq_fp():
    viola(datatset_folders)
    fdfplbp()
    return do_dct(fp_folders) 

def spa_tplbp():
    viola(datatset_folders)
    sdtplbp()
    return sdlbp(viola_folder)
def spa_fplbp():
    viola(datatset_folders)
    sdtplbp()
    return sdlbp(viola_folder)
       
st.title("FACIAL EMOTION DETECTION MODELS -  STUDY")

uploaded_file = st.file_uploader("Choose an image file", type=[".png",".jpg",".jpeg"])

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
        
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
    if d=="Spatial Domain":
        st.write("Spatial Domain")
        if fd=="Local Binary Pattern (LBP)":
            option = 10
            st.write("LBP")
            data,labels = spa_lbp()
        elif fd=="Three Patch LBP":
            option = 11
            st.write("TPLBP")
            data,labels = spa_tplbp()
        elif fd=="Four Patch LBP":
            option = 12
            st.write("FPLBP")
            data,labels = spa_fplbp()
        else:
            option = 13
            st.write("TPLBP+FPLBP")
            
    else:
        st.write("Frequency Domain")
        if fd=="Local Binary Pattern (LBP)":
            option = 20
            st.write("LBP")
            data,labels = freq_lbp()
        elif fd=="Three Patch LBP":
            option = 21
            st.write("TPLBP")
            data,labels = freq_tp()
        elif fd=="Four Patch LBP":
            option = 22
            st.write("FPLBP")
            data,labels = freq_fp()
        else:
            option = 23
            st.write("TPLBP+FPLBP")
            d1,l1 = freq_tp()
            d2,l2 = freq_fp()
            st.write(len(d1),len(l1))
            st.write(len(d2),len(l2))
            #feature fusion
            for i in range(981):
                data.append(d1[i]+d2[i])
            labels = l1
    lsvc = train_test(data,labels)
    st.write("Runtime for Train & Test : %s seconds" % (time.time() - start_time))
    start_time = time.time()
       
    #vj
    find_viola(img)
    #lbp
    if option==20:
        #find_lbp()
        #dct		
        zz = find_dct()
    elif option==21:
        find_tplbp()
        #dct		
        zz = find_dct()
    elif option==22:
        find_fplbp()
        #dct		
        zz = find_dct()
    elif option==23:
        find_tplbp()
        z1 = find_dct()
        find_fplbp()
        z2 = find_dct()
        zz = z1+z2
    #elif option==10:
        #zz = find_sdlbp()
    
            

            
    #svm
    #xval =[]
    #xval.append(zz)
    #yvalpred = lsvc.predict(xval)
    #st.write("Predicted Emotion - ",yvalpred[0])   
    #res = lsvc._predict_proba_lr(xval)
    #for i in range(7):
        #st.write(emo[i],":",res[0][i]*100)
    #st.write("Runtime for uploaded image : %s seconds" % (time.time() - start_time))
    #mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    #st.write("Memory usage - ",mb/1000000,"MB")
    #gives a single float value
    #st.write(psutil.cpu_percent())