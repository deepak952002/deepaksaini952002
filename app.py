import streamlit as st
import joblib

#load the jobfile model
model_nb = joblib.load('spam-ham')

st.title('SPAM HAM CLASSIGIER')
ip = st.text_input('ENTER YOUR TEXT')

op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])
  
  
  
