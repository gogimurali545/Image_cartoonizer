import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import cv2
import base64
from io import BytesIO
import os

uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpeg'])
if uploaded_file is not None:
    image_original = np.asarray(Image.open(uploaded_file))
    # var =str(image_original.shape)
    # st.text(var)
    # image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)
    # image_gray = cv2.resize(image_gray, (960, 540))
    # st.image(image_gray)
    # var1 = str(image_gray.shape)
    # st.text(var1)
    def cartoonify(image):
        grayScaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ReSized2 = cv2.resize(grayScaleImage, (960, 540))

        return ReSized2

    final_image = cartoonify(image_original)
    final_image = Image.fromarray(final_image)
    buf = BytesIO()
    # final_image.save(buf, format='JPEG')
    # img = plt.imshow(final_image)
    
    st.download_button(label="Download gray image", data=buf.getvalue(), mime="image/png")

    
    

