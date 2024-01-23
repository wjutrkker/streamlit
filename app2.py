import streamlit as st
from streamlit_timeline import timeline


# use full page width
st.set_page_config(page_title="Test Multiple Timelines", layout="wide")


def genericCamera(timeLineName):
    with open(f'{timeLineName}.json', "r") as f:
        data = f.read()
    timeline(data, height=600)       

# Add a title and intro text
st.title('Image Review Page')
st.text('This is a page to allow review of Image data')

# Sidebar setup
st.sidebar.title('Radio Buttons')

st.sidebar.title('Navigation')
options = st.sidebar.radio('radio', ['First', 'Second', 'Third'])


cls= st.sidebar.radio('radios', ['1','2', '3', ])
detection = st.sidebar.radio('sidebar', ['1', '2'])
numDet = st.number_input("number input:", value=25)

if options != None:
    genericCamera(options)
    