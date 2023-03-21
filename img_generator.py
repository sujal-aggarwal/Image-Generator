import openai
import urllib.request
from PIL import Image
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()


openai.api_key=os.getenv("API_KEY")

#Function to generate image
def generate_img(img_description):
    img_response=openai.Image.create(
        prompt=img_description,
        n=1,
        size="512x512"
    )
    img_url=img_response['data'][0]['url']
    urllib.request.urlretrieve(img_url,'img.png')
    img=Image.open("img.png")
    return img

# Page Title
st.title(' Image Generation ')

#Text box
img_description=st.text_input('Image Description')

#Text button
if st.button('Generate Image'):
    generated_image=generate_img(img_description)
    st.image(generated_image)
