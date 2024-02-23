from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os

# initialising the flask app
app = Flask(__name__)

# The path for uploading the file
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def uploadfile():
    if request.method == 'POST':
        f = request.files.get('file')  # Use request.files.get to avoid UnboundLocalError
        if f:
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('upload.html', file_uploaded=True, file_name=filename)
    return render_template('upload.html', file_uploaded=False)

@app.route('/display', methods=['GET'])
def display_file():
    file_name = request.args.get('filename')
    return send_from_directory(app.config['UPLOAD_FOLDER'], file_name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)