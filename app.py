import streamlit as st
import json

data1 = json.load(open('./text-summarization_comparision_list_17_01_2024_batch_1.json','r'))
data2 = json.load(open('./text-summarization_comparision_list_17_01_2024_batch_2.json','r'))
data3 = json.load(open('./text-summarization_comparision_list_17_01_2024_batch_3.json','r'))
data = {
    '1. Without examples':data3, 
    '2. With examples (short examples)':data2, 
    '3. With examples (long examples)':data1
    }
st.set_page_config(layout="wide")

selections = ['1. Without examples', '2. With examples (short examples)', '3. With examples (long examples)']
b = st.selectbox('Prompting template', selections)
a = st.number_input('Sample Index', max_value=20, min_value=1) -1

col1, col2, col3 = st.columns([4,2,2])

with col1:
    st.header('Input')
    st.text_area(label= 'Long summary',value=data[b][a]['input'], height=2000)

with col2:
    st.header('Output (old)')
    st.text_area(label= 'Short summary',value=data[b][a]['old_summary']['short'], height=150)
    st.text_area(label= 'Long summary',value=data[b][a]['old_summary']['long'][2:].replace('-', '\n'), height=800)

with col3:
    st.header('Output (new)')
    st.text_area(label= 'Short summary',value=data[b][a]['new_summary']['short'], height=150)
    st.text_area(label= 'Long summary',value=data[b][a]['new_summary']['long'], height=800)

