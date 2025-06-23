import os
from cryptography.fernet import Fernet

KEY_PATH = "keylogger/key.key"
LOG_PATH = "keylogger/log.txt"
ENC_PATH = "keylogger/log.enc"

def generate_key(path=KEY_PATH):
    """Generate a Fernet symmetric key and save it to file."""
    key = Fernet.generate_key()
    with open(path, "wb") as key_file:
        key_file.write(key)
    print(f"[+] Key generated and saved to {path}")

def encrypt_log(log_path=LOG_PATH, enc_path=ENC_PATH, key_path=KEY_PATH):
    """Encrypt log.txt and save it as log.enc using Fernet key."""
    if not os.path.exists(log_path):
        print("[!] Log file not found.")
        return

    with open(key_path, "rb") as kf:
        key = kf.read()
    fernet = Fernet(key)

    with open(log_path, "rb") as log_file:
        data = log_file.read()

    encrypted = fernet.encrypt(data)

    with open(enc_path, "wb") as enc_file:
        enc_file.write(encrypted)

    print(f"[+] Log encrypted and saved to {enc_path}")

def decrypt_log(enc_path=ENC_PATH, key_path=KEY_PATH):
    """(Optional) Decrypt the encrypted log for debugging/testing."""
    if not os.path.exists(enc_path):
        print("[!] Encrypted file not found.")
        return

    with open(key_path, "rb") as kf:
        key = kf.read()
    fernet = Fernet(key)

    with open(enc_path, "rb") as ef:
        encrypted_data = ef.read()

    decrypted = fernet.decrypt(encrypted_data)
    print("\n--- Decrypted Log Preview ---\n")
    print(decrypted.decode())

if __name__ == "__main__":
    if not os.path.exists(KEY_PATH):
        generate_key()
    else:
        print("[*] Key already exists. Skipping generation.")
    encrypt_log()

    # Uncomment to preview decrypted log:
    # decrypt_log()