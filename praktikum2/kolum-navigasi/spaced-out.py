import streamlit as st
from PIL import Image

st.title("Space Out")
st.write("Praktikum 2 - Visualisasi Data")

#st.markdown digunakan untuk menampilkan teks dengan format
st.markdown("**Kelompok 15**")
st.markdown("""          
1. Abdu Azzam Alaris - 0110122073
2. M. Ghiyatsul Humami - 0110220108
3. Nurul Aeman - 0110222099
            """)
img = Image.open("../../praktikum1/Aset/Apel.jpg")
for _ in range(2):
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)