import streamlit as st
import numpy as np


st.sidebar.title('KONTOL')
page =  st.sidebar.selectbox('Pilih Halaman',['Crt','Crtt','Crrttt'])
st.set_page_config()
st.header('Pengujian Hipotesis')
Tab1, Tab2, Tab3 = st.tabs(['ABC','BCD','DEF'])
