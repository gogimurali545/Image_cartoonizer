import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import cv2
import base64
from io import BytesIO
import os

st.set_page_config(page_title="Pirates of Python", page_icon="https://cdn-icons-png.flaticon.com/128/71/71270.png")

st.title("Image Cartoonizer")

def cartoonify(image):
    gray_Image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_Gray_Image = cv2.medianBlur(gray_Image, 5)
    edge_Image = cv2.adaptiveThreshold(blur_Gray_Image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)
    color_Image = cv2.bilateralFilter(image, 9, 300, 300)
    cartoonified_Image = cv2.bitwise_and(color_Image, color_Image, mask=edge_Image)
    return gray_Image, blur_Gray_Image, edge_Image, color_Image, cartoonified_Image

def buffer_data(image):
    image_from_array = Image.fromarray(image)
    buf = BytesIO()
    image_from_array.save(buf, format='JPEG')
    return image_from_array, buf.getvalue()

uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
    image_original = np.asarray(Image.open(uploaded_file))
    

    [image_2, image_3, image_4, image_5, Cartoonified_Image] = cartoonify(image_original)

    col1, col2 = st.columns(2)


    original_image, original_data = buffer_data(image_original)
    image_2, image_2_data = buffer_data(image_2)
    image_3, image_3_data = buffer_data(image_3)
    image_4, image_4_data = buffer_data(image_4)
    image_5, image_5_data = buffer_data(image_5)
    cartoonified_image , cartoonified_data = buffer_data(Cartoonified_Image)
    
    col1.header('Original Image')
    col1.image(original_image)
    col1.download_button(label="Download Original Image", data=original_data, mime="image/png")

    col2.header('Gray Image')
    col2.image(image_2)
    col2.download_button(label="Download Gray Image", data=image_2_data, mime="image/png")

    col1.header('Blur Gray Image')
    col1.image(image_3)
    col1.download_button(label="Download Median Blur Gray Image", data=image_3_data, mime="image/png")

    col2.header('Edge Image')
    col2.image(image_4)
    col2.download_button(label="Download Edge Image", data=image_4_data, mime="image/png")

    col1.header('Colored Blur Image')
    col1.image(image_5)
    col1.download_button(label="Download Colored  Blur Image", data=image_5_data, mime="image/png")

    col2.header('Cartoonified Image')
    col2.image(cartoonified_image)
    col2.download_button(label="Download Cartoonified Image", data=cartoonified_data, mime="image/png")

    st.header('Project Done by: ')
    st.write('Muralidhar Reddy 216')
    st.write('Seetharam Dasari 481')
    st.write('Suraj Alamoni 558')
