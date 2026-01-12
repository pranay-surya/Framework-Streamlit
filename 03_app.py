# Example - 3 :: Potting on Streamlit 
import streamlit as st 
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import altair as alt


st.header('Line Chart Demo')
st.write("This uses Streamlit's built-in interactive chart.")
data = pd.DataFrame(np.random.randn(50,3), columns=['A','B','C'])
st.line_chart(data)
 

 

# Bar Chart: Select by Category
st.header('Bar Chart - Sales by Product')
st.write("Bar Chart shows sales per product.")
data1 = pd.DataFrame({
        "Product":['A','B','C','D'],
        "Sales":[120,300,180,90]
        })
data1 = data1.set_index('Product')
st.bar_chart(data1)
 

# Area Chart : Temperature over time
st.header('Area Chart - Temperature over Day')
st.write("Area chart works well for filling under the curve.")
days = pd.date_range("2025-01-01",periods = 30)
temps = np.cumsum(np.random.randn(30)) + 20
df = pd.DataFrame({"temp": temps},index=days)
st.area_chart(df)
 

# Area Chart : Temperature over time
st.header('Matplotlib Integration')
x = np.linspace(0, 10, 200)
y = np.sin(x)
fig,ax = plt.subplots()
ax.plot(x,y, lw=2)
ax.set_xlabel('X')
ax.set_ylabel('sin(x)')
st.pyplot(fig) 



# Map visualization with lat/lon 
st.header("Map: Random Locations")
st.write("Streamlit uses deck.gl under the hood for maps.")
n = 100
df1 = pd.DataFrame({
    "lat": 37.76 + np.random.randn(n) * 0.02,
    "lon": -122.4 + np.random.randn(n) * 0.02
})
st.map(df1)
 

# Altair chart (declarative) — scatter with tooltips -- ##
st.header("Altair Scatter Plot")
df2 = pd.DataFrame({
    "x1": np.random.randn(200),
    "y1": np.random.randn(200),
    "size": np.abs(np.random.randn(200))*30
})
chart = alt.Chart(df2).mark_circle().encode(
    x="x1", y="y1", size="size", tooltip=["x1","y1","size"]
).interactive()
st.altair_chart(chart, use_container_width=True) 