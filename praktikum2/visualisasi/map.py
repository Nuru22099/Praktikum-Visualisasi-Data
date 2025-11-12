import streamlit as st
import pandas as pd
import numpy as np

st.title("Map")
st.write("Praktikum 2 - Visualisasi Data")


#st.markdown digunakan untuk menampilkan teks dengan format
st.markdown("**Kelompok 15**")
st.markdown("""
            
1. Abdu Azzam Alaris - 0110122073
2. M. Ghiyatsul Humami - 0110220108
3. Nurul Aeman - 0110222099
            """)
df= pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)