#https://github.com/streamlit/streamlit/issues/511
#pip install --upgrade protobuf
#pip install streamlit

import streamlit as st
#import numpy as np
#import pandas as pd

import os
import openai

openai.organization = "org-mKJgDGXpv57x98vta4bKwrLH"
#openai.api_key = os.getenv("OPENAI_API_KEY")
key ='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'

openai.api_key = key

def queryGPT3(model = "text-davinci-003", query="What is the meaning of life?"):
    results = ""
    response = openai.Completion.create(
        #engine="text-davinci-002",
        engine = model,
        #prompt="Write an joke about belgian people",
        prompt = query,
        temperature=0.7,
        max_tokens=30,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print("Engine: ", model)
    results = response.choices[0].text
    return results



def select_models():
    st.sidebar.markdown("# OpenAI GPT 3 Models")
    option = st.sidebar.selectbox(
         'Select an OpenAI GPT 3 Model:',
         ["text-davinci-001","text-davinci-002","text-davinci-003"], index=0)
    st.sidebar.write('You selected:', option)
    return option



def main():
    """OpenAI GPT 3 App"""
    model = "text-davinci-003"
    st.title("Streamlit OpenAI GPT 3 App")
    st.text("Build with Streamlit and OpenAI GPT 3")
    
    activities = ["Streamlit OpenAI GPT 3","About"]
    choice = st.sidebar.selectbox("Select Activty",activities)
    if choice == 'Streamlit OpenAI GPT 3':
        model = select_models()

    elif choice == 'About':
        st.subheader("About Streamlit OpenAI GPT 3 App")
        st.markdown("Built with Streamlit by [LSBU](https://www.lsbu.ac.uk/)")
        st.text("Professor Perry Xiao")
        st.success("Copyright @ 2022 London South Bank University")

    query = st.text_input('Write your query here:', 'What is the meaning of life?')
    if st.button('Query OpenAI GPT 3'):
        #st.write('Why hello there')
        answer = queryGPT3(model,query)
        st.write(answer)
    else:
        #st.write('Goodbye')
        pass 

if __name__ == '__main__':
    main()	
