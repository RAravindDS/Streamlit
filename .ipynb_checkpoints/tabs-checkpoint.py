import streamlit as st 

st.title("This is why I love streamlit!") 

titles = ['Text to question', 'Files to Question', 'YouTube Video To Question'] 

text, file, video = st.tabs(tab_titles) 

with text:
    st.header("Text to Question Generator") 
    t = st.text_area("Enter you text") 
    st.write(t) 
    
with file: 
    st.header("File to Question Generator")
    f = st.file_uploader('upload the files')
    st.write(f) 
    
with video: 
    st.header("YouTube video to Question Generator") 
    v = st.text_input("Enter Your Proper Link") 
    st.write(v) 
    


                     
