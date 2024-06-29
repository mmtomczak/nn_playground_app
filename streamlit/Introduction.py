import streamlit as st

st.set_page_config(
    page_title="Neural Network App",
    layout="wide"
)

with st.sidebar:
    st.title("Upload the data")
    st.file_uploader(
        label="File upoad",
        type="csv",
        label_visibility="hidden"
    )
    
with st.container():
    st.title("Interacive Neural Network App")
    st.markdown(
        """  
        Goal of this application is to introduce a basic understanding on how to create Neural Network models and how they work.  
        Application is utilizing the TensorFlow package for creating neural networks.

        """
    )