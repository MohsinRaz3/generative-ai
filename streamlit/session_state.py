import streamlit as st
 
if "count" not in st.session_state:
    st.session_state.count = 0

if(st.button("increment")):
    st.session_state.count +=1
    st.write(f"incremented count: {st.session_state.count}")

if (st.button("decrement")):
    st.session_state.count -=1
    st.write(f"decremented count: {st.session_state.count}")