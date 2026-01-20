## -- Example - 8 ::Multi-column layout & cards -- ##
## Purpose: Layout multiple charts/controls side-by-side.
import streamlit as st
import pandas as pd
import numpy as np

st.title("Multi-column Layout")
col1, col2 = st.columns(2)
data = pd.DataFrame(np.random.randn(50,3), columns=["A","B","C"])
with col1:
    st.header("Left: Line")
    st.line_chart(data)
with col2:
    st.header("Right: Bar")
    st.bar_chart(data.abs().sum().to_frame().T)
st.write("Columns let you build dashboards.")


## Explanation: st.columns splits page; place widgets independently in columns.
## Result: Two charts side-by-side, responsive layout.