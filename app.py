import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image

# Load the pre-trained model
MODEL_PATH = "leaf_disease_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# Class labels
CLASS_NAMES = ["Healthy", "Powdery", "Rust"]

# Function to preprocess the uploaded image
def preprocess_image(image, target_size=(225, 225)):
    image = image.resize(target_size)
    img_array = img_to_array(image)
    img_array = img_array.astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Streamlit app
st.markdown("<h1 style='text-align: center;'>🌿 Leaf Disease Prediction 🌿</h1>", unsafe_allow_html=True)
st.subheader("Deep learning project by [Your Name]")

# Description
st.write("Upload an image of a leaf, and the model will predict whether it is **Healthy**, affected by **Powdery Mildew**, or has **Rust** disease.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)  # Updated parameter

    # Add a Predict button
    if st.button("Predict"):
        # Preprocess the image
        processed_image = preprocess_image(image)

        # Make predictions
        predictions = model.predict(processed_image)
        predicted_class = CLASS_NAMES[np.argmax(predictions)]
        confidence = np.max(predictions)

        # Display prediction results
        st.markdown(f"<h2 style='color: green;'>Prediction: {predicted_class} 🍃</h2>", unsafe_allow_html=True)
        st.write(f"Confidence: {confidence:.2%}")
