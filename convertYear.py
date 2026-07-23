import streamlit as st
st.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

bh_year-st.number_input("กรอกปี พ.ศ.:", value=1)
ce_year=bh_year-543
st.header ("ปี ค.ศ. คือ : f{ce_year}")
