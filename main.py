import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import cv2

uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpeg'])
if uploaded_file is not None:
    image_original = np.asarray(Image.open(uploaded_file))
    image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)
    # image_gray = cv2.resize(image_gray)
    st.image(image_gray)
    
    

