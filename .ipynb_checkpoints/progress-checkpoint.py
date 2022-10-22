import streamlit as st 
import pandas as pd
import time 
import numpy as np 
import matplotlib.pyplot as plt 

plt.style.use('ggplot') 
data = pd.read_csv('bro.csv').dropna() 

# Multiple Tabls  
rad = st.sidebar.radio("Navigation", ['HOME', "About us"])

if rad == 'HOME': 
    ## side bar widgest 
    col = st.sidebar.multiselect("Select Columns", data.columns)
    fig, ax = plt.subplots()
    ax.plot(data['year'], data[col]) 
    st.pyplot(fig) 
    
if rad == 'About us': 
    st.write('We are simply awesome')
    

## Status Messages 
st.error("Error") 
st.success("show success") 
st.info("Information") 
st.exception(RuntimeError("This is an runtime error")) 
st.warning("his is warning message")


## Progress bar: 
progress = st.progress(0)  # initialize with 0 
for i in range(100): 
    time.sleep(0.1)
    progress.progress(i + 1)

## Ballon animation: 
st.balloons()