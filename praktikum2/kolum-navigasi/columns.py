import streamlit as st
import pandas as pd
import numpy as np

st.title("Columns")
st.write("Praktikum 2 - Visualisasi Data")


#st.markdown digunakan untuk menampilkan teks dengan format
st.markdown("**Kelompok 15**")
st.markdown("""
            
1. Abdu Azzam Alaris - 0110122073
2. M. Ghiyatsul Humami - 0110220108
3. Nurul Aeman - 0110222099
            """)

col1, col2= st.columns(2)

col1.write("ini adalah kolom pertama")
col1.image("../../praktikum1/Aset/Mawar.jpg")

col2.write("ini adalah kolom kedua")
col2.image("../../praktikum1/Aset/Tulip.jpg")