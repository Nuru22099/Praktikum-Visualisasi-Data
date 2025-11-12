import streamlit as st
from PIL import Image

st.title("Grid")
st.write("Praktikum 2 - Visualisasi Data")

#st.markdown digunakan untuk menampilkan teks dengan format
st.markdown("**Kelompok 15**")
st.markdown("""            
1. Abdu Azzam Alaris - 0110122073
2. M. Ghiyatsul Humami - 0110220108
3. Nurul Aeman - 0110222099
            """)
img = Image.open("../../praktikum1/Aset/Serigala.jpg")
st.title("Grid")
for a in range(4):
    cols = st.columns((1, 1, 1, 1,))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)