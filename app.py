from flask import Flask, request, jsonify, render_template
from Crypto.Cipher import AES
import base64

app = Flask(__name__)

BLOCK_SIZE = 16

# Padding function
def pad(text):
    padding = BLOCK_SIZE - len(text) % BLOCK_SIZE
    return text + chr(padding) * padding

# Unpadding function
def unpad(text):
    return text[:-ord(text[-1])]

# Encryption function
def encrypt_message(message, key):
    key = key.ljust(16)[:16].encode()
    message = pad(message).encode()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(message)
    return base64.b64encode(encrypted).decode()

# Decryption function
def decrypt_message(encrypted_message, key):
    key = key.ljust(16)[:16].encode()
    encrypted_data = base64.b64decode(encrypted_message)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(encrypted_data)
    return unpad(decrypted.decode())

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# API: Save and decrypt message
@app.route("/api/save", methods=["POST"])
def save_message():
    data = request.get_json()
    encrypted = data.get("encryptedMessage")
    key = data.get("key")

    if not encrypted or not key:
        return jsonify({"error": "Message or key is missing!"}), 400

    try:
        decrypted = decrypt_message(encrypted, key)
    except Exception as e:
        return jsonify({"error": f"Decryption failed! Error: {str(e)}"}), 400

    try:
        with open("saved_messages.txt", "a", encoding="utf-8") as f:
            f.write(decrypted + "\n")
    except Exception as e:
        return jsonify({"error": f"Failed to save message! Error: {str(e)}"}), 500

    return jsonify({"message": "Message saved!", "decrypted": decrypted})

# Run the application
if __name__ == "__main__":
    app.run(debug=True, port=5001)
