#Import Libraries
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from utils import head, set_bg, equal_text, body, example, about, explanation_of_movements, transform_output
from deep_painting_app.explore_data import random_painting, pick_up_one_painting_per_class
import requests
import random
import math
import numpy as np
import plotly.express as px

path = 'raw_data/examples'
#Opens and displays the image
def get_opened_image(image):
    return Image.open(image)

#Title
head()

#Sets background image
#set_bg('data/black_background.jpg')


#Shows examples of images for each class
example()

if 'main_random_images' not in st.session_state:
    st.session_state['main_random_images'] = pick_up_one_painting_per_class(path)
    print("Init")

figure, axs = plt.subplots(1, 6, figsize=(20,20))
i = 0
for cl in  st.session_state['main_random_images']:
    axs[i].imshow(st.session_state['main_random_images'][cl]/255)
    axs[i].set_title(equal_text(cl))
    axs[i].set_axis_off()
    i += 1
st.pyplot(figure)

#Short explanations for movements
explanation_of_movements()

#Body
body()

#Uploads the image file
image_file = st.file_uploader('Upload an image', type = ['png', 'jpg',
                                                         'jpeg', 'pdf'])

deep_painting_url = 'https://deeppainting3-ynhfw4pdza-an.a.run.app/predict/image'

if image_file:
    st.markdown(f'<h2 style="font-size:22px;color:black;margin-bottom:-35px">{"Results"}</h2>',
                unsafe_allow_html=True)
    r = requests.post(url = deep_painting_url,files={'file':image_file})
    predicted_movement = r.json()['movement']
    predicted_probabilty = r.json()['confidence']

    st.markdown(f'<h2 style="font-size:22px;color:black;margin-bottom:-35px">{f"The Deep Painting App classifies this image as {predicted_movement} ."}</h2>',
                unsafe_allow_html=True)
    api_df = transform_output(r.json())
    fig = px.bar(api_df, x='Confidence', y='Movement',orientation='h', color = 'Movement')
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig)

    image = get_opened_image(image_file)
    with st.expander("Selected Image", expanded = True):
        st.image(image, use_column_width = True)


#THE GUESSING GAME
if 'sidebar_random_image' not in st.session_state:
    st.session_state['sidebar_random_image'] = random_painting(path)
    print("Init")

def form2_callback():
    st.session_state['sidebar_random_image'] = random_painting(path)
    print("callback")

with st.sidebar:
    with st.expander('About'): #About section
        about()

    st.title('Guess the Movement')
    fig, ax = plt.subplots()
    ax.imshow(st.session_state['sidebar_random_image'][0]/255)
    ax.set_axis_off()
    st.pyplot(fig)

    label = st.session_state['sidebar_random_image'][1]
    label = equal_text(label)


    with st.form(key ='Form1'):
        movement = st.radio("What do you think?",
                    ('High Renaissance', 'Impressionism', 'Northern Renaissance',
                     'Post Impressionism', 'Rococo', 'Ukiyo-e'))

        submitted = st.form_submit_button(label = 'Submit')

    if submitted:
        if movement == label:
            st.write('Well done!')
        else:
            st.write(f'Ooops! It was {label} .')

        btn = st.button("Next", on_click= form2_callback)
