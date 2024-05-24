from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'UPLOAD_FOLDER'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')####

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return f'File {filename} uploaded successfully. <a href="/view/{filename}" style="color: #3333FF;">View</a> or <a href="/download/{filename}">Download</a>'
    return '<body style="background-color: #FF9999;"><p style="color: red; text-align: center; font-weight: bold; font-size: 50px;">No file selected</p></body>'

@app.route('/view/<filename>')
def view_file(filename):
    return render_template('view.html', filename=filename)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

