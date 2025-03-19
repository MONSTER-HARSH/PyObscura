from cryptography.fernet import Fernet


def load_key():
    return open("secret.key", "rb").read()


def decrypt_and_run(encrypted_file):
    key = load_key()
    cipher = Fernet(key)

    with open(encrypted_file, "rb") as f:
        encrypted_data = f.read()

    decrypted_code = cipher.decrypt(encrypted_data).decode()

    
    exec(decrypted_code, globals())

if __name__ == "__main__":
    decrypt_and_run("encrypted_script.enc")
