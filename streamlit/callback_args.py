import streamlit as st

st.set_page_config(page_title="callback args", page_icon="🔢")

count = 0
if "count" not in st.session_state:
    st.session_state.count = 0

user_input = st.number_input("enter your number ")

def incremental(user_input):
    st.session_state.count += user_input
def decremental(user_input):
    st.session_state.count -=user_input

st.button("increment",on_click=incremental, args=(user_input,))
st.write(f"counter = {st.session_state.count}")

st.button("decrement",on_click=decremental, args=(user_input,))
