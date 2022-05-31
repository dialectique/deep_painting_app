#Import Libraries
import streamlit as st
import re
import base64

#Sets title and the body
def head():

    st.markdown(f'<h1 style="text-align:center;color:black;margin-bottom:-30px;margin-top: -10px">{"Welcome To The Deep Painting App"}</h1>',
                unsafe_allow_html=True)

def body():
    st.markdown(f'<h2 style="text-align:center;color:black;margin-bottom:-25px;margin-top: 7px; font-size:21px;font-weight:bolder">{"Upload your image to predict the artistic movement "}</h2>',
                unsafe_allow_html=True)

def example():
    st.markdown(f'<h2 style="text-align:center;color:black;margin-bottom:-25px;margin-top: 7px; font-size:23px;font-weight:bolder">{"Image examples from six different artistic movements"}</h2>',
                unsafe_allow_html=True)

def about():
    st.markdown('This is a web app that can be used to perform deep learning based image classification. The app is developed by **Gilles**, **Kevser**, **Deepanjali**, and **Bryan**.')
    st.markdown('The app is based on the **[DeepPainting]** model')

#Transforms " 'highRenaiss' to 'High Renaiss' "
def equal_text(text):
    res = [re.sub(r"(\w)([A-Z])", r"\1 \2", text)]
    return res[0].title()

#Sets background
@st.cache(allow_output_mutation=True)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = """
        <style>
        .stApp {
        background-image: url("data:image/jpg;base64,%s");
        background-size: cover;
        }
        </style>
    """ % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
