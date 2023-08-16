import os
import base64
import secrets
import hashlib
from cryptography.fernet import Fernet

def generate_aes_key():
    return secrets.token_urlsafe(32)

def hmac_derive_key(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=32)
  # Make the iteration number larger for higher security. The CPU hates me if I set to 1m.

def aes_encrypt(data, key):
    salt = os.urandom(16)
    aes_key = hmac_derive_key(key.encode(), salt)
    cipher = Fernet(base64.urlsafe_b64encode(aes_key).decode())
    encrypted_data = cipher.encrypt(data.encode())
    return base64.urlsafe_b64encode(salt + encrypted_data).decode()

def aes_decrypt(data, key):
    data = base64.urlsafe_b64decode(data.encode())
    salt = data[:16]
    aes_key = hmac_derive_key(key.encode(), salt)
    cipher = Fernet(base64.urlsafe_b64encode(aes_key).decode())
    decrypted_data = cipher.decrypt(data[16:])
    return decrypted_data.decode()

def encode(text, aes_key=None):
    try:
        if aes_key is None:
            aes_key = generate_aes_key()
        aes_encrypted = aes_encrypt(text, aes_key)
        return aes_key, aes_encrypted
    except Exception as e:
        raise ValueError("Error occurred during encoding: " + str(e))

def decode(data, key):
    try:
        aes_decrypted = aes_decrypt(data, key)
        return aes_decrypted
    except Exception as e:
        raise ValueError("Error occurred during decoding: " + str(e))
