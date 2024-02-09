from flask import Flask, render_template, request, jsonify 
import numpy as numpy
from PIL import Image
import io
import pickle

app = Flask(__name__)

# Placeholder for model
def predict_image(iamge_data):
    #Convert image data to numpy array image
    image = Image.open(io.BytesIO(iamge_data)).convert("RGB")
    # Resize model if needed
    # image - image.resize((width, height))
    # Convert image to numpy array
    image_array = np.array(image)
    # Make predictions using the model
    prediction = "dummy prediction"
    return prediction

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_image', methods=['POST'])
def prediction_image():
    if request.method == 'POST':
        try:
            # Get image file from request
            file = request.files['file']
            # Read iamge file as bytes 
            image_data = file.read()
            prediction_result = predict_image(image_data)
            return jsonify({'prediction': prediction_result}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
