## -- Example - 4 — DataFrame filtering with widgets -- ##
import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris

st.title("Data Filter - Iris Dataset")
iris = load_iris(as_frame=True)
data = iris.frame
species = st.multiselect("Species",options= data["target"].unique(),default= data["target"].unique())
min_petal = st.slider("Min petal length", float(data["petal length (cm)"].min()), float(data["petal length (cm)"].max()), 0.0)
filtered = data[(data["target"].isin(species)) & (data["petal length (cm)"] >= min_petal)]
st.dataframe(filtered)
st.write("Rows:", len(filtered))