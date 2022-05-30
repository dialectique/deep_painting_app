#Import Libraries
from re import sub
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import os
from utils import head, set_bg, equal_text
from deep_painting_app.explore_data import random_painting


#Opens and displays the image
def get_opened_image(image):
    return Image.open(image)

#Title and the body
head()

#Sets background image
set_bg('data/black_background.jpg')

#Uploads the image file
image_file = st.file_uploader('Upload an image', type = ['png', 'jpg',
                                                         'jpeg', 'pdf'])

#Displays the image
if image_file and st.button('Load'):
    image = get_opened_image(image_file)
    with st.expander("Selected Image", expanded = True):
        st.image(image, use_column_width = True)

# #Displays the results
# pred = perform_prediction(image_file) #function name can be different
# st.subheader('Prediction')
# st.markdown(f'This image belongs to **{pred}** class with .. probability')

#THE GUESSING GAME
path = 'data/orgImg'

if 'random_image' not in st.session_state:
    st.session_state['random_image'] = random_painting(path)
    print("Init")

def form2_callback():
    st.session_state['random_image'] = random_painting(path)
    print("callback")

with st.sidebar:
    st.title('Guess the Movement')
    fig, ax = plt.subplots()
    ax.imshow(st.session_state['random_image'][0]/255)
    ax.set_axis_off()
    st.pyplot(fig)

    label = st.session_state['random_image'][1]
    label = equal_text(label)


    with st.form(key ='Form1'):
        movement = st.radio("What do you think?",
                    ('High Renaiss', 'Impress', 'Northern Renaiss',
                     'Post Impress', 'Rococo', 'Ukiyo'))

        submitted = st.form_submit_button(label = 'Submit')

    if submitted:
        if movement == label:
            st.write('Well done!')
        else:
            st.write(f'Ooops! It was {label} .')

        #with st.form(key = 'Form2'):
        btn = st.button("Next", on_click= form2_callback)
