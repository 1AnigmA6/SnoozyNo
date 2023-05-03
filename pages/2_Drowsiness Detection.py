import streamlit as st
import cv2
import os
import tensorflow as tf
from keras.models import load_model
import numpy as np
from pygame import mixer
import time

def selectsound():
    mixer.init()
    sound = 0
    option = st.selectbox("Select your alarm choice: ", ("none", "alarm", "warning", "classic", "street public"))
    if option == "none":
        st.error("Select a alarm sound")
    elif option == "alarm":
        sound = mixer.Sound("D:\\BACKUP\\Assignments\\Final year pro\\Drowsiness detection\\Drowsiness detection\\alarms\\alarm.wav")
        sound.play(maxtime=2000)
    elif option == "warning":
        sound = mixer.Sound("D:\\BACKUP\\Assignments\\Final year pro\\Drowsiness detection\\Drowsiness detection\\alarms\\warning.wav")
        sound.play(maxtime=2000)
    elif option == "classic":
        sound = mixer.Sound("D:\\BACKUP\\Assignments\\Final year pro\\Drowsiness detection\\Drowsiness detection\\alarms\\mixkitclassic.wav")
        sound.play(maxtime=2000)
    elif option == "street public":
        sound = mixer.Sound("D:\\BACKUP\\Assignments\\Final year pro\\Drowsiness detection\\Drowsiness detection\\alarms\\streetpublic.wav")
        sound.play(maxtime=2000)

    return sound


def detection(file):
    #these are the cascade files that are used in extraction of the features that have been captured
    face = cv2.CascadeClassifier('D:\BACKUP\Assignments\Final year pro\Drowsiness detection\Drowsiness detection\haar cascade files\haarcascade_frontalface_alt.xml')
    leye = cv2.CascadeClassifier('D:\BACKUP\Assignments\Final year pro\Drowsiness detection\Drowsiness detection\haar cascade files\haarcascade_lefteye_2splits.xml')
    reye = cv2.CascadeClassifier('D:\BACKUP\Assignments\Final year pro\Drowsiness detection\Drowsiness detection\haar cascade files\haarcascade_righteye_2splits.xml')
    lbl=['Close','Open']

    model = load_model('D:\BACKUP\Assignments\Final year pro\Drowsiness detection\Drowsiness detection\models\model1.h5')
    path = os.getcwd()
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    sound = file

    def webcam(sound):
        mixer.init()
        cap = cv2.VideoCapture(0)
        Frame_Window = st.image([])
        count=0
        score=0 
        thicc=2
        rpred=[99]
        lpred=[99]
        while True:
            ref, frame = cap.read()
            height,width = frame.shape[:2]

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))
            left_eye = leye.detectMultiScale(gray)
            right_eye =  reye.detectMultiScale(gray)

            cv2.rectangle(frame, (0,height-50) , (200,height) , (0,0,0) , thickness=cv2.FILLED )

            #Classifies the face and extract the face image feature
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y) , (x+w,y+h) , (100,100,100) , 1 )
            
            #Extracts the right eye for classification
            for (x,y,w,h) in right_eye:
                r_eye=frame[y:y+h,x:x+w]
                count=count+1
                r_eye = cv2.cvtColor(r_eye,cv2.COLOR_BGR2GRAY)
                r_eye = cv2.resize(r_eye,(24,24))
                r_eye= r_eye/255
                r_eye=  r_eye.reshape(24,24,-1)
                r_eye = np.expand_dims(r_eye,axis=0)
                rpred = np.argmax(model.predict(r_eye), axis=-1)
                if(rpred[0]==1):
                    lbl='Open' 
                if(rpred[0]==0):
                    lbl='Closed'
                break

            #Extracts the left eye for classification
            for (x,y,w,h) in left_eye:
                l_eye=frame[y:y+h,x:x+w]
                count=count+1
                l_eye = cv2.cvtColor(l_eye,cv2.COLOR_BGR2GRAY)  
                l_eye = cv2.resize(l_eye,(24,24))
                l_eye= l_eye/255
                l_eye=l_eye.reshape(24,24,-1)
                l_eye = np.expand_dims(l_eye,axis=0)
                lpred = np.argmax(model.predict(l_eye), axis=-1)
                if(lpred[0]==1):
                    lbl='Open'   
                if(lpred[0]==0):
                    lbl='Closed'
                break

            if(rpred[0]==0 and lpred[0]==0):
                score=score+1
                cv2.putText(frame,"Closed",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
            # if(rpred[0]==1 or lpred[0]==1):
            else:
                score=score-1
                cv2.putText(frame,"Open",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
                
            if(score<0):
                score=0   
            cv2.putText(frame,'Score:'+str(score),(100,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
            if(score>15):
                #person is feeling sleepy so we beep the alarm
                cv2.imwrite(os.path.join(path,'image.jpg'),frame)
                try:
                    sound.play()    
                except:  # isplaying = False
                    pass
                if(thicc<16):
                    thicc= thicc+2
                else:
                    thicc=thicc-2
                    if(thicc<2):
                        thicc=2
                cv2.rectangle(frame,(0,0),(width,height),(0,0,255),thicc)


            #Displaying the image frames
            Frame_Window.image(frame)


    if st.button("Close"):
        cap.release()
        cv2.destroyAllWindows()

    if st.button("Start Detection"):
        webcam(sound)
        

file = selectsound()
if file != 0:
    detection(file)
else:
    print("Error: Sound not selected")
