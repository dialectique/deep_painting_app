#Import Libraries
import streamlit as st
import re
import base64


#Sets title and the body
def head():

    st.markdown(f'<h1 style="color:#471F05;text-align:center;color:brown;margin-bottom:-49px;margin-top: 19px">{"Deep Painting App"}</h1>',
                unsafe_allow_html=True)

    st.markdown(f'<h2 style="text-align:center;color:#4E6073;margin-bottom:-60px;margin-top: -1.5px; font-size:22px;font-weight:bolder">{" Welcome to the Deep Painting App!"}</h2>',
                unsafe_allow_html=True)
    st.markdown(f'<h2 style="text-align:center;color:#4E6073;margin-bottom:-25px;margin-top: 7px; font-size:21px; font-weight:bolder">{"If you want to learn which class your image belongs to, <br> please upload your image. "}</h2>',
                unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

#Sets background
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

#Transforms " 'highRenaiss' to 'High Renaiss' "
def equal_text(text):
    res = [re.sub(r"(\w)([A-Z])", r"\1 \2", text)]
    return res[0].title()
