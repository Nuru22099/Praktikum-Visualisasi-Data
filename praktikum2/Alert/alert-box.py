import streamlit as st

st.title("Alert Box")
st.write("Praktikum 2 - Visualisasi Data")

#st.markdown digunakan untuk menampilkan teks dengan format
st.markdown("Kelompok 15")
st.markdown("""            
1. Abdu Azzam Alaris - 0110122073
2. M. Ghiyatsul Humami - 0110220108
3. Nurul Aeman - 0110222099
            """)
st.success("Succsessful")
st.warning("Warning")
st.info("Info")
st.error("Error")
st.exception("It is an exception")