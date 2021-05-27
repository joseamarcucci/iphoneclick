import streamlit as st







buff, col = st.beta_columns([2,2])

country = buff.text_input('Ingrese mail USAL')
if country != "":
