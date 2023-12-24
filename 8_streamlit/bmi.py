import streamlit as st

st.title("BMI Calculator: Calculate your BMI")
weight = st.number_input("Type your weight in kg ")
height = st.number_input("Type your height in cm/inches")

h_measure = st.radio("Select height format", ["cm","inches"])
if h_measure == "cm":
    st.write(h_measure)
else:
    st.write(h_measure)
    