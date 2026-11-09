# 🔐 AES Web Application

A Flask-based web application that demonstrates client-side and server-side **AES symmetric encryption and decryption** using **CryptoJS** on the frontend and **PyCryptodome** on the backend.

## ✨ Features

- **Client-Side AES Encryption/Decryption:** Encrypts and decrypts messages directly in the browser using `CryptoJS.AES`.
- **Server-Side Verification & Storage:** Sends encrypted payloads to the `/api/save` Flask endpoint, which decrypts the payload (supporting both OpenSSL salted AES-256-CBC and raw AES-128-ECB) with full UTF-8 support and logs verified messages.
- **Responsive Interface:** Clean web UI styled with custom CSS.

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask, PyCryptodome
- **Frontend:** HTML5, CSS3, Vanilla JavaScript, CryptoJS

## 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Firatdondar/AES_WEB_APP.git
   cd AES_WEB_APP
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   Navigate to `http://127.0.0.1:5001`
