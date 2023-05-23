import pickle
import string
import streamlit as st
import webbrowser
global Lrdetect_Model

Lrdetect_Model=open('testmodel.pckl','rb')
Lrdetect_Model=pickle.load(Lrdetect_Model)

st.title("Emotion detection")
input_test=st.text_input("input text", '')
button_clicked=st.button("get emotion")
if(button_clicked):
	st.text(Lrdetect_Model.predict([input_test]))