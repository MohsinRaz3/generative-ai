import streamlit as st
st.set_page_config(page_title="Avatar the last air bender",page_icon="🏹")

st.title("Avatar the last Air bender")
col1,col2,col3 = st.columns(3)
with col1:
    st.header("Aang")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTezZSo2Pvavad-SUMJNxUJHKoW5pO7Oh1RXg&usqp=CAU")


with col2:
    st.header("Sokka")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqTwVx5pbNY6tr7QIldNR75-x5uBaPK92p-Q&usqp=CAU")


with col3:
    st.header("Katara")
    st.image("https://a1cf74336522e87f135f-2f21ace9a6cf0052456644b80fa06d4f.ssl.cf2.rackcdn.com/images/characters/large/2800/Katara.Avatar-The-Last-Airbender.webp")



col4,col5,col6 = st.columns(3)
with col4:
    st.header("Momo")
    st.image("https://i.ebayimg.com/images/g/cdgAAOSwyxRhLOpr/s-l1600.png")


with col5:
    st.header("Aapa")
    st.image("https://steamuserimages-a.akamaihd.net/ugc/1807639172330902507/07D5BDF54068E697B05EB6B4ED295852DD94B4EC/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true")


with col6:
    st.header("Toph")
    st.image("https://facts.net/wp-content/uploads/2023/09/20-facts-about-toph-beifong-avatar-the-last-airbender-1694069244.jpg")