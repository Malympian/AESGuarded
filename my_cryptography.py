# my_cryptography.py

# Install the cryptography library if you haven't already
# (You don't need to include this line in your code)
# pip install cryptography

# Import necessary modules from the cryptography library
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from cryptography.hazmat.primitives import serialization

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

def aes_encrypt(data, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted_data

def aes_decrypt(data, key):
    iv = data[:16]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(data[16:]) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data

def get_shift(char):
    return (ord(char.lower()) - ord('a'))

def shift_letter(char, key_char, reverse=False):
    if char.isalpha():
        shift = get_shift(key_char)
        if reverse:
            shift = -shift
        ord_value = ord(char.lower()) + shift
        if char.isupper():
            if ord_value > ord('z'):
                ord_value -= 26
            elif ord_value < ord('a'):
                ord_value += 26
            return chr(ord_value).upper()
        else:
            if ord_value > ord('z'):
                ord_value -= 26
            elif ord_value < ord('a'):
                ord_value += 26
            return chr(ord_value)
    else:
        return char

def vigenere_encrypt(text, keyword):
    encrypted = ""
    keyword = keyword.lower()
    keyword_index = 0

    for char in text:
        encrypted += shift_letter(char, keyword[keyword_index])
        if char.isalpha():
            keyword_index = (keyword_index + 1) % len(keyword)

    return encrypted

def vigenere_decrypt(text, keyword):
    decrypted = ""
    keyword = keyword.lower()
    keyword_index = 0

    for char in text:
        shifted = shift_letter(char, keyword[keyword_index], reverse=True)
        decrypted += shifted
        if char.isalpha():
            keyword_index = (keyword_index + 1) % len(keyword)

    return decrypted

def reverse_text(text):
    return "".join(reversed(text))

def encode(text):
    try:
        reversed_text = reverse_text(text)
        vigenere_encrypted = vigenere_encrypt(reversed_text, KEYWORD)
        aes_key = os.urandom(16)
        aes_encrypted = aes_encrypt(vigenere_encrypted.encode(), aes_key)
        aes_encoded_data = aes_key + aes_encrypted
        return base64.b64encode(aes_encoded_data).decode()
    except Exception as e:
        raise ValueError("Encryption error: " + str(e))

def decode(text):
    try:
        aes_encoded_data = base64.b64decode(text.encode())
        aes_key = aes_encoded_data[:16]
        aes_encrypted = aes_encoded_data[16:]
        vigenere_encrypted = aes_decrypt(aes_encrypted, aes_key)
        reversed_text = vigenere_decrypt(vigenere_encrypted.decode(), KEYWORD)
        return reverse_text(reversed_text)
    except Exception as e:
        raise ValueError("Decryption error: " + str(e))

# Fetch the KEYWORD from the environment variable (Repl.it Secret)
import os
KEYWORD = os.getenv("KEYWORD")
