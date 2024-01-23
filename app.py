import streamlit as st
from streamlit_timeline import timeline

# use full page width
st.set_page_config(page_title="Test Basic Timelines", layout="wide")

# def genericCamera(timeLineName):
with open(f'/app/timeline.json', "r") as f:
    data = f.read()
timeline(data, height=600)       

# Add a title and intro text
st.title('Image Review Page')
st.text('This is a page to allow review of Image data')



    