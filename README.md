# Deepfake Image Detection Using MobileNetV2

## Overview

This repository implements a deepfake image detection system using MobileNetV2 as a pre-trained model and a Flask-based web application for the user interface. The system allows users to upload an image and receive a response indicating whether the image is real or fake.

## Features

- **MobileNetV2 Pre-trained Model**: Utilizes MobileNetV2 to detect deepfakes efficiently.
- **Custom Dataset Training**: Allows for fine-tuning on deepfake datasets.
- **Flask Web Application**: A simple UI where users can upload an image and receive detection results.
- **Real-Time Detection**: Instantly displays whether the uploaded image is real or fake.

## Architecture

- **Model**: The core of the detection system is built using MobileNetV2, a lightweight and efficient convolutional neural network.
- **Web Interface**: The UI is built using Flask, enabling users to interact with the model through a browser.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Ankurgupta2927/Deepfake-Image-Detection.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Deepfake-Image-Detection
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run Flask app.

```bash
    python app.py
```
