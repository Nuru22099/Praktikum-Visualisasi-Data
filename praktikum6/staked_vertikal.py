import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Header
st.title("Praktikum 6 Visualisasi Data")
st.write("Kelompok 15")
st.markdown("""
    1. Abdu Azzam Alaris - 0110122073
    2. M. Ghiyatsul Humami - 0110220108
    3. Nurul Aeman - 0110222099
 """)

# Dataset
stores = ['Store A', 'Store B', 'Store C']
male = [150, 200, 180]
female = [120, 230, 170]

# Data Transaksi Penjualan
stores = ['Store A', 'Store B', 'Store C']
product_a = [200, 250, 300]
product_b = [150, 300, 200]

# Data Quarter
q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 160]

# 1. Grafik Staked Vertikal Bar Chart
st.subheader("1. Staked Vertikal Bar Chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male, label='Male', color='green')
ax.bar(x, female, bottom=male, label='Female', color='red')

ax.set_title('Population by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

# 2. Grafik Staked Vertikal Bar Chart
st.subheader("2. Staked Vertikal Bar Chart dengan Matplotlib")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a, label='Product A', color='black')
ax.bar(x, product_b, bottom=product_a, label='Product B', color='pink')

ax.set_title('Sales by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

# 3. Grafik Kustomisasi Staked Vertikal Bar Chart
st.subheader("3. Kustomisasi Staked Vertikal Bar Chart")

for i in range(len(x)):
    plt.text(x[i], product_a[i]/2, str(product_a[i]), ha='center', color='orange')
    plt.text(x[i], product_a[i] + product_b[i]/2, str(product_b[i]), ha='center', color='black')
st.pyplot(fig)

# 4. Grafik Multiple Staked Vertikal Bar Chart
st.subheader("4. Multiple Staked Vertikal Bar Chart")

fig, ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))

# Quarter 1
ax.bar(x-width/2, q1_male, label='Q1 Male', color='pink', width=width)
ax.bar(x-width/2, q1_female, bottom=q1_male, label='Q1 Female', color='black', width=width)

# Quarter 2
ax.bar(x-width/2, q2_male, label='Q2 Male', color='orange', width=width)
ax.bar(x-width/2, q2_female, bottom=q2_male, label='Q1 Female', color='black', width=width)

ax.set_title('Population by Gender and Store (Multiple Quarter)')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)