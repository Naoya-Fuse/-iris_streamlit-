import streamlit as st
import numpy as np
import pandas as pd

# Pillow
from PIL import Image

# 画像の読み込み
img = Image.open('iris.jpg')
st.image(img,caption = 'Iris' , use_column_width = True)

# チェックボックス
if st.checkbox('Show Image'):
    img = Image.open('iris.jpg')
    st.image(img,caption = 'Iris' , use_column_width = True)

    