#https://github.com/streamlit/streamlit/issues/511
#pip install --upgrade protobuf
#pip install streamlit

import streamlit as st
import numpy as np
import pandas as pd

import os


mode = 1

def select_models():
    st.sidebar.markdown("# OpenAI GPT 3 Models")
    option = st.sidebar.selectbox(
         'Select an OpenAI GPT 3 Model:',
         ["text-davinci-001","text-davinci-002","text-davinci-003"], index=0)
    st.sidebar.write('You selected:', option)
    if option == "text-davinci-001":
        mode = 1
    elif option == "text-davinci-002":
        mode = 2
    elif option == "text-davinci-003":
        mode = 3
    return mode



def main():
    """Image Classification App"""
    query = st.text_input('Write your query here:', 'What is the meaning of life?')

    st.title("Streamlit OpenAI GPT 3 App")
    st.text("Build with Streamlit and OpenAI GPT 3")
    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')
    
    activities = ["Streamlit OpenAI GPT 3","About"]
    choice = st.sidebar.selectbox("Select Activty",activities)
    if choice == 'Streamlit OpenAI GPT 3':
        mode = select_models()

    elif choice == 'About':
        st.subheader("About Streamlit OpenAI GPT 3 App")
        st.markdown("Built with Streamlit by [LSBU](https://www.lsbu.ac.uk/)")
        st.text("Professor Perry Xiao")
        st.success("Copyright @ 2022 London South Bank University")
if __name__ == '__main__':
    main()	
