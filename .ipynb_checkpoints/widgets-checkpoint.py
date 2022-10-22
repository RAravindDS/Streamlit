import streamlit as st 

# Button 
st.title('Button') 
st.button('Click here')


# some function 
if st.button('Click Here'): 
    st.write("like this video")
    
    
## Text Input 
text = st.text_input("Give your text") 
st.write(text)

### 1.1 Multiple area of text input 
st.subheader("This is large box text")
address = st.text_area("Enter your address") 
st.write(address)

## Radio Buttion 
a = st.radio("Question Type:", ['MCQ', 'FILL', 'BOTH'], index = 0)  # index = 0, means it select 0th index value defaultly 
st.write(f'You have selected: {a}')

## Files upload 
b = st.file_uploader("Upload the files") 
st.

## Select Box: 
a = st.selectbox("Question Type:", ['MCQ', 'FILL', 'BOTH'], index = 0)

## Select Multiple Options: 
a = st.multiselect("Question Type:", ['MCQ', 'FILL', 'BOTH'])





## st.date_input()
## st.time_input() 

## Adding checkbox 
# st.checkbox("You accept the T&C", value = False) 

## some functionality 
if st.checkbox("You accept the T&C", value = False): 
    st.write("Thank you")


## Slider 
st.slider("age", min_value = 20, max_value = 60)

## Number Input 
st.number_input("numbers")  # all the functionality same as 