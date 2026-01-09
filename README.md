# SecureVault

SecureVault is a secure, zero-knowledge file sharing application built using Python Flask and the `cryptography` library. It implements AES encryption to protect files at rest, ensuring that the server never stores decryption keys.

## Project Overview

This application simulates a high-security environment where data privacy is paramount. Unlike traditional cloud storage, SecureVault employs a **Zero-Knowledge Architecture**:
* **Per-File Encryption:** Every file is encrypted with a unique, randomly generated key.
* **No Server-Side Key Storage:** The decryption key is generated upon upload and displayed only once to the user. It is not saved in the database or filesystem.
* **Data Integrity:** The system uses Fernet (AES-128 in CBC mode with HMAC) to ensure files are not tampered with during storage.

## Key Features

* **Secure Uploads:** Files are automatically encrypted before being saved to the server disk.
* **Zero-Knowledge Privacy:** The server administrator cannot access user files without the user-provided key.
* **Manual Decryption:** Downloads require the user to input the specific encryption key generated during the upload process.
* **Ephemeral Key Generation:** Keys exist in memory only for the duration of the request and are discarded immediately after.

## Technical Stack

* **Language:** Python 3.x
* **Framework:** Flask
* **Encryption:** `cryptography` library (Fernet implementation of AES)
* **Frontend:** HTML5, CSS3

## Installation and Setup

### 1. Clone the Repository

git clone [https://github.com/YOUR_USERNAME/SecureVault.git](https://github.com/YOUR_USERNAME/SecureVault.git)
cd SecureVault 
### 2. Set Up Virtual Environment (Recommended)


# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

### 3. Install Dependencies

pip install Flask cryptography

### 4. Run the Application

python app.py
The application will start on http://127.0.0.1:5000.

Usage Guide
Upload File: Navigate to the home page and select a file to upload.

Save Key: Upon successful upload, the system will generate a unique decryption key. Copy this key immediately; it is shown only once.

Download & Decrypt: To retrieve a file, click the "Decrypt" button next to the filename and paste your saved key.
