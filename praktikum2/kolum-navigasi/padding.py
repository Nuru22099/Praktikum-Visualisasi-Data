import streamlit as st
from PIL import Image

st.title("Padding")
st.write("Praktikum 2 - Visualisasi Data")

#st.markdown digunakan untuk menampilkan teks dengan format
st.markdown("**Kelompok 15**")
st.markdown("""            
1. Abdu Azzam Alaris - 0110122073
2. M. Ghiyatsul Humami - 0110220108
3. Nurul Aeman - 0110222099
            """)
img = Image.open("../../praktikum1/Aset/Mawar.jpg")
col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)