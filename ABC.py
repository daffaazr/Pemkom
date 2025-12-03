import streamlit as st
import numpy as np


st.sidebar.title('Kelompok 4')
st.sidebar.image('2wCEAAkGBxMTEhUTExMWFhUXGBoWFxgXGBoYFxoYGBoXFxgYGBgYHSggGholHhgVITEiJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGxAQGi0lHx8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0rLS0tLS0tLf', width = 120)
page =  st.sidebar.selectbox('Pilih Halaman',['Crt','Crtt','Crrttt'])

st.markdown("""
<style>
body {
    background-color: #f7f9fc;
}
</style>
""", unsafe_allow_html=True)

card = """
<div style="
    background-color:white;
    padding:20px;
    border-radius:18px;
    box-shadow:0 4px 10px rgba(0,0,0,0.15);
    margin-bottom:20px;
">
    <h3 style="color:#333;">📘 Informasi</h3>
    <p style="font-size:16px;">Ini contoh card cantik di Streamlit.</p>
</div>
"""

st.markdown(card, unsafe_allow_html=True)

st.set_page_config()
st.header('Pengujian Hipotesis')
Tab1, Tab2, Tab3 = st.tabs(['ABC','BCD','DEF'])
