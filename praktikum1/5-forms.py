import streamlit as st

st.title("Text Box")
st.markdown("**Kelompok 15**")
st.markdown("""
1. Abdu Azzam Alaris - 0110122073
2. M. Ghiyatsul Humami - 0110220108
3. Nurul Aeman - 0110222099
            """)

("---------------------------------------------------------------------")

#creating text box
name = st.text_input("Enter Your Name")

st.write("Your Name is", name)

#creating text box with 10 as character limit
name = st.text_input("Enter Your Name", max_chars=10)
password = st.text_input("Enter Your Password", type='password')

("----------------------------------")

import streamlit as st

#creating text area
input_text = st.text_area("Enter your Review")

#printing entered text
st.write("""You entered: \n""", input_text)

("-----------------------------------")

import streamlit as st
#create number input
st.number_input("Enter Your Number")

import streamlit as st
#create number input
num = st.number_input("Enter Your Number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. Value is 10")
st.write("Default Value is 5, \n Step Size value is 2")
st.write("Total value after adding number entered with step value is:", num)

("----------------------------")
import streamlit as st
st.title("Time")
#defining time function
st.time_input("Select Your Time")

("-----------------------------")
import streamlit as st
st.title("Date")

#defining date function
st.date_input("Select Date")

("-------------------------")
import streamlit as st
import datetime
st. title("Date")

#defining time function
st.date_input("Select your date", value=datetime.date(1989, 12, 25)),
min_value = datetime.date(1987, 1, 1),
max_value = datetime.date(2005, 12, 1)

("------------------------------")
st.title("Select Color")
color_code= st.color_picker("Select your color")
st.header(color_code)

("----------------------------")
import streamlit as st
import pandas as pd
st.title("CSV Data")
data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")
if details:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type":data_file.type,
                        "file_size":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else :
        st.write("No CSV File is Uploaded")

("---------------------------")

import streamlit as st
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')

#defining submit button
submit_button = my_form.form_submit_button(label='submit')

st. write(a)