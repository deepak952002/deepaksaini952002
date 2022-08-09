import streamlit as st
import joblib

#load the jobfile model
model_nb = joblib.load('spam-ham')

st.title('SPAM HAM CLASSIGIER')
IP = ST.TEXT_INPUT('ENTER YOUR TEXT')

OP = MODEL_NB.PREDICT([ip])
if st.button('PREDICT'):
  st.title(op[0])

  
  
  
     
     
