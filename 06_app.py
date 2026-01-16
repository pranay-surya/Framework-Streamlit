## -- Example - 6 :: Caching expensive computations (st.cache_data) -- ##
import streamlit as st
import time
import pandas as pd
import numpy as np

st.title("Caching Example")
@st.cache_data
def expensive_calc(n):
    time.sleep(2)
    return pd.DataFrame(np.random.randn(n,3), columns=list("ABC"))

n = st.slider("Rows", 100, 5000, 500)
df = expensive_calc(n)
st.write(df.head())
st.write("Note: expand rows to see caching effect (first run slower).")


## Explanation: @st.cache_data caches function outputs. Use for data loading/transformations.
## Result: Faster repeated interactions after first run.