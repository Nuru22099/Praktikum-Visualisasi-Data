import streamlit as st
import numpy as np

st.title("Containers")
st.write("Praktikum 2 - Visualisasi Data")

#st.markdown digunakan untuk menampilkan teks dengan format
st.markdown("**Kelompok 15**")
st.markdown("""
                        
1. Abdu Azzam Alaris - 0110122073
2. M. Ghiyatsul Humami - 0110220108
3. Nurul Aeman - 0110222099
            """)

with st.container():
    st.write("Elemen Inside Container")
    st.line_chart(np.random.randn(40,4))
    st.write("Elemen Outside Container")