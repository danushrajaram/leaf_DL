from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
MODEL_PATH = "leaf_disease_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# Class labels
CLASS_NAMES = ["Healthy", "Powdery", "Rust"]

# Function to preprocess the image
def preprocess_image(image, target_size=(225, 225)):
    image = image.resize(target_size)
    img_array = img_to_array(image)
    img_array = img_array.astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# API endpoint for predictions
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    try:
        # Load and preprocess the image
        image = Image.open(file)
        processed_image = preprocess_image(image)

        # Make predictions
        predictions = model.predict(processed_image)
        predicted_class = CLASS_NAMES[np.argmax(predictions)]
        confidence = np.max(predictions)

        # Return the prediction results as JSON
        return jsonify({
            "prediction": predicted_class,
            "confidence": float(confidence)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
