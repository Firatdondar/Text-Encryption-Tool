# 🔐 Text Encryption Tool (AES-256-CBC & PKCS7)

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-000000?logo=flask&logoColor=white)
![PyCryptodome](https://img.shields.io/badge/PyCryptodome-AES--256-critical)
![JavaScript](https://img.shields.io/badge/CryptoJS-4.1.1-F7DF1E?logo=javascript&logoColor=black)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A full-stack cryptographic web application built with **Flask**, **PyCryptodome**, and **CryptoJS** that performs interactive **client-side AES encryption/decryption** and **server-side cryptographic verification**.

---

## ✨ Key Features

- **In-Browser AES-256 Encryption & Decryption:** Encrypts plaintext messages and decrypts Base64 ciphertexts directly in the browser using `CryptoJS.AES` with user-supplied secret passphrases.
- **Cross-Platform OpenSSL Key Derivation (`EVP_BytesToKey`):** The Python backend (`app.py`) implements OpenSSL `Salted__` MD5 key/IV derivation (`AES-256-CBC`) alongside raw `AES-128-ECB` fallback and strict byte-level **PKCS#7 unpadding**, ensuring 100% compatibility with multi-byte UTF-8 characters.
- **Server-Side Cryptographic Verification (`/api/save`):** Verifies encrypted payloads on the Flask server before logging authenticated messages.
- **Modern Dark-Mode UI:** Responsive two-column cryptographic studio with one-click clipboard copy and live verification badges.

---

## 🗂️ Project Structure

```text
Text-Encryption-Tool/
├── static/
│   └── css/
│       └── style.css        # Modern dark-mode cryptographic studio styles
├── templates/
│   └── index.html           # Interactive encryption/decryption web interface
├── app.py                   # Flask server & AES-256-CBC / AES-ECB verification engine
├── requirements.txt         # Python dependencies (Flask, pycryptodome)
├── LICENSE                  # MIT License
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Firatdondar/Text-Encryption-Tool.git
cd Text-Encryption-Tool
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Server
```bash
python app.py
```
Open `http://127.0.0.1:5001` in your browser.

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
