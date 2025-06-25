# Keylogger-With-Encrypted-Data-Exfiltration-
A Proof-of-Concept Keylogger that encrypts logs and simulates exfiltration

## Project Overview:

This is a Proof-of-Concept (PoC) encrypted keylogger built using Python. It captures user keystrokes, encrypts them using AES (Fernet), and simulates the secure exfiltration of logs to a local Flask-based server.

The project is designed strictly for ethical testing and educational purposes only.

---

## Requirements:

- [pynput](https://pypi.org/project/pynput/) for capturing keystrokes
- [cryptography](https://pypi.org/project/cryptography/) for AES encryption (Fernet)
- [Flask](https://flask.palletsprojects.com/en/stable/) to simulate a remote server
- [requests](https://pypi.org/project/requests/) to simulate a remote server

---

## Folder Structure:

project/
- .gitignore
- README.md
- keylogger/
  - keylogger.py # Captures keystrokes to log.txt
  - encryptor.py # Encrypts logs into log.enc
  - upload_client.py # Sends encrypted file to server
  - log.txt # Generated Plain keystroke log
  - log.enc # Generated Encrypted log
  - key.key # Generated Fernet encryption key
- server/
  - server.py # Flask server to receive logs
- uploads/ # (Generated) Folder for received logs

---

## How It Works:

1. **Keylogger** (`keylogger.py`) captures keyboard input and writes it to `log.txt`.
2. **Encryptor** (`encryptor.py`) uses a randomly generated Fernet AES key to encrypt `log.txt` into `log.enc`.
3. **Flask Server** (`server.py`) listens on `http://localhost:5000/upload` to receive encrypted files.
4. **Uploader** (`upload_client.py`) simulates sending the `log.enc` to the server via an HTTP POST request.
5. Logs are saved securely in the `uploads/` folder on the server side.

---

## How To Run This Project On Windows/Linux:

### 1. Install Python Dependancies

- Make sure Python 3 is installed. Then run:
  pip install pynput cryptography flask requests

### 2. Run the Keylogger

- Captures keystrokes and saves them in log.txt
- Run with this command:
  python keylogger/keylogger.py
- Press a few keys, then stop with "Ctrl + C"

### 3. Encrypt the Logs

- Encrypt the logs with Fernet AES
- Run with this command:
  python keylogger/encryptor.py
- This will generate:
  - log.enc (encrypted data)
  - key.key (your secret key)

### 4. Start the Flask Server

- Simulate a remote endpoint for exfiltration
- Run using this command:
  python server/server.py
- it runs on https://localhost:5000/upload

### 5. Send Encrypted Log to Server

- Simulate exfiltration to the server
- Run with this command
  python keylogger/upload_client.py
- Encrypted file will be stored in the uploads/ folder on the server.

### 6. Add these to .gitignore

__pycache__/
*.pyc
*.enc
*.log
log.txt
key.key
uploads/

---

## Disclaimer

This project is intended strictly for educational and ethical testing purposes only. This project was created as an assignment for an internship at Elevate Labs. Do not deploy or distribute this software on any device or network you do not own or have explicit permission to test.

## Author

Sumit Milind Prabhu
Computer Engineering Student @ COEP Technological University, Pune
