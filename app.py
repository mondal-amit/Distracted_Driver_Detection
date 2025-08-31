import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

st.title("🚗 Distracted Driver Detection")

st.write("Upload an image of a driver and the model will classify the behavior.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Load model (dummy placeholder)
    st.write("Model loading... (Replace with your trained model)")
    # model = tf.keras.models.load_model('../models/distracted_driver_model.keras')

    st.write("Prediction: [Dummy Output] Replace with model.predict()")
