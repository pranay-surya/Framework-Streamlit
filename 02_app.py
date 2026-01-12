# Example - 2 :: File Uploader and Display CSV file 

import pandas as pd 
import streamlit as st
st.title("CSV File Uploader ")

uploaded = st.file_uploader("Upload a csv file ", type=["csv"])
if uploaded :
    data = pd.read_csv(uploaded)
    st.write("Preview of Dataset ")
    st.write("First 3 Rows ")
    st.dataframe(data.head(3))
    st.write("Last 3 Rows ",data.tail(3))
    st.write("Shape of Dataset :: ",data.shape)
    st.write("Number of Rows :: ",data.shape[0])
    st.write("Number of Columns :: ",data.shape[1])
    st.write("Null values in Dataset ",data.isnull().sum())
    st.write("Data type of each column ",data.dtypes)


else:
    st.info("Please Upload a CSV file to see Details ")    

