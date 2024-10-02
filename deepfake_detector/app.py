from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from model import predict_image

app = Flask(__name__)

# Folder for uploaded images
app.config['UPLOAD_FOLDER'] = 'uploads/'
# Allowed extensions for image files
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg','webp'}

# Function to check if the uploaded file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle image upload and prediction
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Predict if the image is real or fake
        result = predict_image(filepath)
        
        return render_template('result.html', result=result)
    
    return redirect(request.url)

if __name__ == '__main__':
    # Create uploads directory if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    # Run the app on port 5001
    app.run(debug=True, port=5001)
