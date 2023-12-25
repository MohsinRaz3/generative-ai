import streamlit as st

st.set_page_config(
    page_icon="🎰",
    page_title="Counter Callback"
)

count = 1
if "count" not in st.session_state:
    st.session_state.count = 1

def incremental():
    st.session_state.count +=2
def decremental():
    st.session_state.count -=2

if(st.button("increment",on_click=incremental)):
    st.write(st.session_state.count)
if(st.button("decrement",on_click=decremental)):
    st.write(st.session_state.count)