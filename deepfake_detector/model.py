import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

# Load the Keras model
model = load_model('deepfake_detection_model.h5')

# Function to preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Resize to 224x224
    img_array = image.img_to_array(img)  # Convert to array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize the image
    return img_array

# Function to predict whether an image is real or fake
def predict_image(image_path):
    # Preprocess the image
    img_array = preprocess_image(image_path)

    # Make a prediction
    prediction = model.predict(img_array)

    # Convert the prediction to binary (0 for real, 1 for fake)
    predicted_class = np.where(prediction > 0.5, 1, 0)

    # Return result
    return 'fake' if predicted_class == 1 else 'real'
