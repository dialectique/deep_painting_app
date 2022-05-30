#Import Libraries
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
set_bg('data/background.jpg')

#Uploads the image file
image_file = st.file_uploader('Upload an image', type = ['png', 'jpg',
                                                         'jpeg', 'pdf'])
# #Camera Input
# picture = st.camera_input("Take a picture")
# if picture and st.button('Load'):
#     pic = get_opened_image(picture)
#     with st.expander("Selected Image", expanded = True):
#         st.image(pic, use_column_width = True)

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
with st.sidebar:
    st.title('Guess the Movement')
    path = 'data/orgImg'
    random_image = random_painting(path, img_height=180, img_width=180)
    fig, ax = plt.subplots()
    ax.imshow(random_image[0]/255)
    ax.set_axis_off()
    st.pyplot(fig)

    # movement = st.radio("What do you think?",
    #                 ('High Renaiss', 'Impress', 'Northern Renaiss',
    #                  'Post Impress', 'Rococo', 'Ukiyo'))

    # movement = st.selectbox("What do you think?",
    #                 ('High Renaiss', 'Impress', 'Northern Renaiss',
    #                  'Post Impress', 'Rococo', 'Ukiyo'))

    with st.form(key ='Form1'):
        movement = st.radio("What do you think?",
                    ('Empty', 'High Renaiss', 'Impress', 'Northern Renaiss',
                     'Post Impress', 'Rococo', 'Ukiyo'), on_change=None)

        submitted = st.form_submit_button(label = 'Submit')

    label = random_image[1]
    label = equal_text(label)

    if movement == label:
        st.write('Well done!')
    else:
        st.write(f'Ooops! It was {label} .')

    # placeholder = st.empty()
    # with placeholder.container():
    #     btn = st.button("Next")

    # if btn:
    #     placeholder.empty()
