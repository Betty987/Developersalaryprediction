import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))
with st.sidebar: 
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()