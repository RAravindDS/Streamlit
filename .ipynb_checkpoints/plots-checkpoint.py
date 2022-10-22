import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
st.set_option('deprecation.showPyplotGlobalUse', False)

from IPython import display 
display.set_matplotlib_formats('svg')

a = pd.read_csv("bro.csv").dropna()

## line chart 
st.subheader("This is line chart for Temperate")
st.line_chart(a["TEMP"])

## area chart 
st.subheader("This is a area chart") 
st.area_chart(a['TEMP'], width = 500, height = 500)

## bar chart 
st.subheader("This is a bar chart") 
st.bar_chart(a['TEMP']) 


### MATPLOT LIB 
st.subheader("This is a scatter plot") 
plt.scatter(a['TEMP'], a['O3']) 
st.pyplot(use_container_width = True)  # It will take whole column

## Better way fig, ax = plt.subplots(); ax.plot(); st.pyplot(fig)
## It can support plotly, graphviz and more.... 

## Display image 
st.image("download.png")  # width and height 

## Audio 
# st.audio('path') 

## Video 
# st.video('path') ## you can specify youtube video link aslo. or any online video link. 