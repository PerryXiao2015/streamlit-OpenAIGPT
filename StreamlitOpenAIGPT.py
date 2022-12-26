#https://github.com/streamlit/streamlit/issues/511
#pip install --upgrade protobuf
#pip install streamlit

import streamlit as st
#import numpy as np
#import pandas as pd

import os
import openai

import pyttsx3
engine = pyttsx3.init()
import speech_recognition as sr
print(sr.__version__)

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

def show_query_text(model):
    query = st.text_input('Write your query here:', 'What is the meaning of life?')
    if st.button('Query OpenAI GPT 3'):
        #st.write('Why hello there')
        answer = queryGPT3(model,query)
        st.write(answer)
    else:
        #st.write('Goodbye')
        pass 

def show_query_audio(model):
    if st.button('Ask OpenAI GPT 3'):
        #st.write('Why hello there')
        #answer = queryGPT3(model,query)
        #st.write(answer)
        text = "Welcome to London"
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(source)
            audio_data = r.record(source, duration = 5)
            print("Recognizing...")
            text = r.recognize_google(audio_data)
            st.write(text)
        engine.say(text)
        engine.runAndWait()

    else:
        #st.write('Goodbye')
        pass 


def main():
    """OpenAI GPT 3 App"""
    model = "text-davinci-003"
    st.title("Streamlit OpenAI GPT 3 App")
    st.text("Build with Streamlit and OpenAI GPT 3")
    
    activities = ["Text GPT3 Query","Audio GPT3 Query","About"]
    choice = st.sidebar.selectbox("Select Activty",activities)
    if choice == 'Text GPT3 Query':
        model = select_models()
        show_query_text(model)
    elif choice == 'Audio GPT3 Query':
        model = select_models()
        show_query_audio(model)

    elif choice == 'About':
        st.subheader("About Streamlit OpenAI GPT 3 App")
        st.markdown("Built with Streamlit by [LSBU](https://www.lsbu.ac.uk/)")
        st.text("Professor Perry Xiao")
        st.success("Copyright @ 2022 London South Bank University")


if __name__ == '__main__':
    main()	
