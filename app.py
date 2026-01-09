from flask import Flask, request, send_file, render_template, redirect, url_for
from cryptography.fernet import Fernet
import os
import io

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        
        key = Fernet.generate_key()
        cipher = Fernet(key)

        
        original_data = file.read()
        encrypted_data = cipher.encrypt(original_data)
        
        
        filepath = os.path.join(UPLOAD_FOLDER, file.filename + ".enc")
        with open(filepath, "wb") as f:
            f.write(encrypted_data)
        
       
        return render_template('success.html', key=key.decode(), filename=file.filename)


@app.route('/unlock/<filename>')
def unlock_page(filename):
    return render_template('unlock.html', filename=filename)


@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    filename = request.form['filename']
    user_key = request.form['key'] 
    
    try:
       
        cipher = Fernet(user_key.encode())
        
       
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        with open(filepath, "rb") as f:
            encrypted_data = f.read()
            
        
        decrypted_data = cipher.decrypt(encrypted_data)
        
       
        return send_file(
            io.BytesIO(decrypted_data),
            as_attachment=True,
            download_name=filename.replace(".enc", "")
        )
    except Exception as e:
        return f"<h1>Decryption Failed!</h1><p>Incorrect Key or Corrupt File.</p><p>Error: {e}</p>"

if __name__ == '__main__':
    app.run(debug=True)