from flask import Flask, request
import os
import datetime

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = os.path.join(UPLOAD_FOLDER, f"log_{timestamp}.enc")
    with open(save_path, "wb") as f:
        f.write(request.data)
    print(f"[+] Saved encrypted log to {save_path}")
    return "Upload successful", 200

if __name__ == "__main__":
    print("[*] Starting server at http://localhost:5000")
    app.run(host="0.0.0.0", port=5000)