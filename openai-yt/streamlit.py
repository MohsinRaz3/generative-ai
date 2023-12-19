import streamlit as st
import pandas as pd
import numpy as np

# write and input text values
st.write("# hellow streamlit")
x = st.text_input("## Whats your fav language?")   

#display variable values and button
st.write(f"my fav language is { x}")
st.button(f"Click me for: {x}")

#display csv file in streamlit
data = pd.read_csv("niche.csv")
st.write(data)

#display graph with random data
chart_value = pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])

st.line_chart(chart_value)
st.bar_chart(chart_value)