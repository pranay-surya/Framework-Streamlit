# Example -1 :: basic Texts , Input & Slider 
 
import streamlit as st
st.title("Hello Streamlit")
st.header("Widgets Gallery")
st.write("Answer the Question :: ")
name = st.text_input("Enter your name","Achal")
age = st.slider("Age",0,100,30)
color = st.selectbox("Favorite color",['Red','Green','Blue'])
st.write("Hello {} your age is {} favorite color is {}".format(name,age,color))