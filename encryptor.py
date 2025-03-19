from cryptography.fernet import Fernet
import sys


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("secret.key", "rb").read()


def encrypt_file(input_file, output_file):
    key = load_key()
    cipher = Fernet(key)

    with open(input_file, "rb") as f:
        plaintext = f.read()

    encrypted = cipher.encrypt(plaintext)

    with open(output_file, "wb") as f:
        f.write(encrypted)

    print(f"Encrypted {input_file} -> {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python encryptor.py <script.py>")
        sys.exit(1)

    generate_key()
    encrypt_file(sys.argv[1], "encrypted_script.enc")
