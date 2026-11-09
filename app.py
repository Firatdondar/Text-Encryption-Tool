from flask import Flask, request, jsonify, render_template
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib

app = Flask(__name__)

BLOCK_SIZE = 16


def evp_bytes_to_key(password: bytes, salt: bytes, key_len: int = 32, iv_len: int = 16):
    """Derives AES key and IV compatible with CryptoJS OpenSSL format."""
    dtot = b""
    d = b""
    while len(dtot) < (key_len + iv_len):
        d = hashlib.md5(d + password + salt).digest()
        dtot += d
    return dtot[:key_len], dtot[key_len:key_len + iv_len]


# Encryption function
def encrypt_message(message: str, key: str) -> str:
    key_bytes = key.encode("utf-8").ljust(BLOCK_SIZE, b"\0")[:BLOCK_SIZE]
    padded_bytes = pad(message.encode("utf-8"), BLOCK_SIZE)
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    encrypted = cipher.encrypt(padded_bytes)
    return base64.b64encode(encrypted).decode("utf-8")


# Decryption function (supports both CryptoJS Salted CBC and raw AES-ECB)
def decrypt_message(encrypted_message: str, key: str) -> str:
    encrypted_data = base64.b64decode(encrypted_message)

    if encrypted_data.startswith(b"Salted__"):
        salt = encrypted_data[8:16]
        ciphertext = encrypted_data[16:]
        aes_key, iv = evp_bytes_to_key(key.encode("utf-8"), salt, 32, 16)
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), BLOCK_SIZE)
        return decrypted.decode("utf-8")

    key_bytes = key.encode("utf-8").ljust(BLOCK_SIZE, b"\0")[:BLOCK_SIZE]
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(encrypted_data), BLOCK_SIZE)
    return decrypted.decode("utf-8")


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# API: Save and decrypt message
@app.route("/api/save", methods=["POST"])
def save_message():
    data = request.get_json() or {}
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
