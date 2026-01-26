## -- Example - 9 :: Simple ML - Iris classifier with inputs + probability (improved) -- ##
# Purpose: Full example using scikit-learn, accept inputs, predict & show probability chart.
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.title("Iris Classifier (with probabilities)")
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Sidebar inputs
st.sidebar.header("Input features")
def user_input():
    vals = {name: st.sidebar.slider(name, float(X[name].min()), float(X[name].max()), float(X[name].mean())) for name in X.columns}
    return pd.DataFrame(vals, index=[0])
input_df = user_input()

# Train model (toy example — train on full data)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
pred = model.predict(input_df)[0]
proba = model.predict_proba(input_df)[0]
st.subheader("Input")
st.write(input_df)
st.subheader("Prediction")
st.write(iris.target_names[pred])
st.subheader("Prediction Probabilities")
st.bar_chart(pd.DataFrame(proba.reshape(1,-1), columns=iris.target_names))


## Explanation: Classic ML pipeline in-app. Shows prediction and probabilities as a bar chart.
## Result: Sidebar controls, prediction, and probability visualization.