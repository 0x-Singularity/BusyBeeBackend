from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
import numpy as np
from PIL import Image
import io
import pickle

app = Flask(__name__, template_folder='templates')

model = InceptionV3(weights="imagenet", include_top=True)

# Function to preprocess input image
def preprocess_image(image_data):
    img = Image.open(io.BytesIO(image_data))
    img = img.resize((299, 299))  # Resize image to match input size of InceptionV3
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Preprocess image for InceptionV3
    return img_array

# Function to perform image classification
def classify_image(image_data):
    img_array = preprocess_image(image_data)
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]  # Get top 3 predicted classes
    return decoded_predictions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_image', methods=['POST'])
def predict_image():
    if request.method == 'POST':
        try:
            # Get image file from request
            file = request.files['file']
            # Read image file as bytes
            image_data = file.read()
            # Perform image classification
            predictions = classify_image(image_data)
            # Return predictions as JSON response
            return jsonify(predictions=[(label, str(np.round(score * 100, 2)) + '%') for (_, label, score) in predictions]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
