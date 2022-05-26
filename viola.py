import streamlit as st
import cv2
from common import *
from dataprocess import *
def cropface(img,cropx,cropy):
    y,x = img.shape
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)    
    return img[starty:starty+cropy,startx:startx+cropx]

def viola(folders):
    order = 0
    for folder in folders:
        d=0
        images = load_images_from_folder(folder)
        for img in images:
            # Convert into grayscale
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Load the cascade
            face_cascade = cv2.CascadeClassifier('/Users/poojaps/Desktop/project/haarcascade_frontalface_alt.xml')
            # Detect faces
            faces = face_cascade.detectMultiScale(img, 1.1, 4)
            # Draw rectangle around the faces and crop the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                faces = img[y:y + h, x:x + w]
                #for dim<41
                if(faces.shape[0]<41 or faces.shape[1]<41):
                    faces = cv2.resize(faces, (41,41), interpolation = cv2.INTER_AREA)  
                #for dim>41         
                faces=cropface(faces,41,41)
                #save cropped face                
                filename = '/Users/poojaps/Desktop/project/afterviola/' + emo[order] + '/face' + emo[order]+ str(d) + '.png'			
                cv2.imwrite(filename, faces)
            d=d+1
        order = order+1
        
        
def find_viola(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #print(img.shape[0],img.shape[1])
    face_cascade = cv2.CascadeClassifier('/Users/poojaps/Desktop/project/haarcascade_frontalface_alt.xml')
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        faces = img[y:y + h, x:x + w]
        #print(faces.shape[0],faces.shape[1])
        faces = cv2.resize(faces, (41,41), interpolation = cv2.INTER_AREA)
        #print(faces.shape[0],faces.shape[1])
        cv2.imwrite('/Users/poojaps/Desktop/project/sampleviola.png', faces) 
      
    return faces