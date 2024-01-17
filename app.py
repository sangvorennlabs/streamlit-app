import streamlit as st
import json

data = json.load(open('./text-summarization_comparision_list_17_01_2024.json','r'))
st.set_page_config(layout="wide")
a = st.number_input('Sample Index', max_value=10, min_value=1) -1

col1, col2, col3 = st.columns([4,2,2])

with col1:
    st.header('Input')
    st.text_area(label= 'Long summary',value=data[a]['input'], height=2000)

with col2:
    st.header('Output (old)')
    st.text_area(label= 'Short summary',value=data[a]['old_summary']['short'], height=150)
    st.text_area(label= 'Long summary',value=data[a]['old_summary']['long'], height=800)

with col3:
    st.header('Output (new)')
    st.text_area(label= 'Short summary',value=data[a]['new_summary']['short'], height=150)
    st.text_area(label= 'Long summary',value=data[a]['new_summary']['long'], height=800)

