import streamlit as st 
import pandas as pd 
import numpy as np 
import time 

# visualize the dataframe in multiple ways
a = pd.read_csv('bro.csv') 

st.title("Data Frame")
st.dataframe(a.head(), width = 500, height = 500) 

# st.json(dictionary)
# st.table(a) 
st.subheader("1. This is write funciton") 
st.write(a.head()) 

# st.table(a) 

""" Caching a mechanism if you want to run the heavy file, it will take some time. 
    But If you active cache in your code, every time it will save the cache and run it fastly!"""

@st.cache 
def summa(): 
    time.sleep(5) 
    return time.time()


if st.checkbox("1"): 
    st.write(summa()) 
    
if st.checkbox("2"): 
    st.write(summa()) 
   # """ It will run faster """
