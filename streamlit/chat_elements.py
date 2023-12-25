import streamlit as st

user_input = st.chat_input("say something")

if "data" not in st.session_state:
    st.session_state.data : list = []

if user_input:
    st.session_state.data.append(user_input)
    st.write(st.session_state.data)

##############################################
    
assistant_msg = st.chat_message("assistant")
assistant_msg.write("hey good day my friend")

user_msg = st.chat_message("user")
user_msg.write("How is it goin'")