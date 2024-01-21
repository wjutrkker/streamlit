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

# st.sidebar.title('Navigation')
cameraArray = [key for key in arrayOfCams.keys() if arrayOfCams[key][0]!="N/A"]
print(cameraArray)
# options = st.sidebar.radio('Cameras', ['RY_rack', 'Top_Silo_PTZ', 'BackAdmin'])
options = st.sidebar.radio('Cameras',cameraArray)


cls= st.sidebar.radio('Detection Class', ['any','person', 'car', ])
detection = st.sidebar.radio('Dections or Tracks', ['detections', 'tracks'])
numDet = st.number_input("Number of Detections To Display:", value=25)

if options != None:
    genericCamera(options)
    