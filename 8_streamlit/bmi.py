import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="📟"
)

st.title("BMI Calculator: Calculate your BMI")
weight = st.number_input("Type your weight in kg ")

h_measure = st.radio("Select height format", ["cm","feet","meters"])

if h_measure == "cm":
    height = st.number_input("Type your height in cm")

    try:
        bmi = (weight/((height/100)**2))
    except:
        st.write("")
elif h_measure=="feet": 
    height = st.number_input("Type your height in feet")
    try:
        bmi = (weight/(((height/3.28))**2))
    except:
        st.write("")

else:
    height = st.number_input("Type your height in meters")
    try:
       bmi = (weight/(height**2))
    except:
        st.write("")


if(st.button("calculate")):
    st.write(f"your BMI index is {bmi}")
    if bmi <= 16:
        st.error(f"Your Bmi is: {bmi} which is severe")
    elif bmi > 16 and bmi < 18.5:
        st.warning(f"Your BMI is: {bmi} which is Mild")
    elif bmi > 18.5 and bmi < 25:
        st.success(f"Your bmi is: {bmi} which is Normal")
    else:
        st.error(f"Your BMI is {bmi} which is Overweight")    
