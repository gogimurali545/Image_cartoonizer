import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import base64
from io import BytesIO
import os

uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpeg'])
if uploaded_file is not None:
    image_original = np.asarray(Image.open(uploaded_file))
    var =str(image_original.shape)
    # st.text(var)
    image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)
    # image_gray = cv2.resize(image_gray, (960, 540))
    st.image(image_gray)
    # var1 = str(image_gray.shape)
    # st.text(var1)
    image_gray = Image.fromarray(image_gray)
    buf = BytesIO()
    image_gray.save(buf, format='JPEG')
    # img = plt.imshow(image_gray)
    
    st.download_button(label="Download gray image", data=buf.getvalue(), mime="image/png")

    
    

