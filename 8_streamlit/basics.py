import streamlit as st

#write titles or headers
st.title("hello title")
st.header("hello header")
st.subheader("hello subheader")

#write text
st.text("hellow text")
st.write("hellow write")

#markdown
'_this_ is ***markdown***'
st.markdown("This is _markdown_")

#code snippet
st.code('while True:\n if x == 2:\n print("They are equal")')

#select from checkbox
if st.checkbox("hide/show"):
    st.write("checked")
else:
    st.write("unchecked")


# select value from radio button
status = st.radio(" select gender", ("male","female","other"))
if status =="male":
    st.success(f"{status}")
elif status == "female":
    st.warning("only male can apply")
else:
    st.toast("contact us")

#select DOB from clander
dob = st.date_input("Your birthday")
st.write(dob)

#form-fill for login
with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')


#slider
level = st.slider("Select the level", 1, 5)
st.write(level)

#input text

name = st.text_input("enter your name")
name

st.button("click me for some reason")

if st.button("about"):
    st.text("welcome to genai about") 

st.radio("select one number", (1,2,3))