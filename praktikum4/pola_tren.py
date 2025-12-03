import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Bar Chart")
st.write("**Kelompok 15**")
st.markdown("""
    1. Abdu Azzam Alaris - 0110122073
    2. M. Ghiyatsul Humami - 0110220108
    3. Nurul Aeman - 0110222099
 """)

#data
data = {
    'Tahun': ['2019', '2020', '2021', '2022', '2023'],
    'Ilmu Komputer': [100, 110, 120, 130, 140],
    'Sistem Informasi': [120, 125, 135, 145, 160],
    'Teknik Informatika': [90, 95, 100, 105, 110],
    'Data Science': [70, 75, 80, 85, 90]
}

df = pd.DataFrame(data)

# Streamlit App
st.title("Visualisasi Tren Jumlah Mahasiswa Memilih Jurusan Komputer (5 Tahun Terakhir)")

# Menambahkan Filter Tahun
filter_tahun = st.multiselect("Pilih Tahun:", df['Tahun'], default=df['Tahun'])

# Menambahkan Filter Jurusan
jurusan_list = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
filter_jurusan = st.multiselect("Pilih Jurusan:", jurusan_list, default=jurusan_list)

#Filter Data Berdasarkan Input Pengguna 
filtered_data = df[df['Tahun'].isin(filter_tahun)][['Tahun'] + filter_jurusan]

# Menampilkan Data Tabel
st.subheader("Data Jumlah Mahasiswa")
st.dataframe(filtered_data)

# Membuat Bar Chart Dengan Filter
st.subheader("Bar Chart deangan Filter")
fig, ax = plt.subplots(figsize=(10, 6))

# Membuat Bar Chart Berdasarkan Data Yang Di Filter
x = range(len(filtered_data['Tahun']))
width = 0.2

for i, jur in enumerate(filter_jurusan):
    ax.bar([p + i * width for p in x], filtered_data[jur], width=width, label=jur)

# Menyesuaikan Sumbu dan Judul
ax.set_title("Jumlah Mahasiswa per Jurusan (Berdasarkan Filter)")
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Mahasiswa")
ax.set_xticks([p + width * len(filter_jurusan) / 2 - width / 2 for p in x])
ax.set_xticklabels(filtered_data['Tahun'])
ax.legend()

st.pyplot(fig)