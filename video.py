import streamlit as st 



st.header("Just showing video") 
st.video("https://drive.google.com/file/d/1BGHlaxBNQdfxiAIwE4gyPCGiE7V47q0y/preview") 


my_file = "https://drive.google.com/file/d/1BGHlaxBNQdfxiAIwE4gyPCGiE7V47q0y/preview"
video_file = open(my_file, "rb").read()

st.subheader("byte Video") 
st.video(video_file)