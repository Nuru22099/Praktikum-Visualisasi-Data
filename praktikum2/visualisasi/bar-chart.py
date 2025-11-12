import streamlit as st
import pandas as pd
import numpy as np

st.title("Bar Chart")
st.write("Praktikum 2 - Visualisasi Data")


#st.markdown digunakan untuk menampilkan teks dengan format
st.markdown("**Kelompok 15**")
st.markdown("""
1. Abdu Azzam Alaris - 0110122073
2. M. Ghiyatsul Humami - 0110220108
3. Nurul Aeman - 0110222099
            """)

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)
st.bar_chart(df)