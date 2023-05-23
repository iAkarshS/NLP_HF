import pickle
import string
import streamlit as st
import webbrowser
global Lrdetect_Model
global filename

from datetime import datetime


Lrdetect_Model=open('testmodel.pckl','rb')
Lrdetect_Model=pickle.load(Lrdetect_Model)

st.title("Emotion detection")
input_test=st.text_input("input text", '')
t=1
button_clicked=st.button("get emotion")
if(button_clicked):
    st.text(Lrdetect_Model.predict([input_test]))
    with open("log.txt","a") as out_file:
        if t==1:
            now = datetime.now()
            os=str(now)+","+input_test+","+str(Lrdetect_Model.predict([input_test]))+"\n"
            out_file.write(os)
            t=0
