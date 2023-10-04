import os
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def generate_aes_key():
    return get_random_bytes(32)  # 256-bit AES key

def encrypt(message, key):
    cipher = AES.new(key, AES.MODE_GCM)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    return nonce + ciphertext + tag

def decrypt(ciphertext, key):
    nonce = ciphertext[:16]
    tag = ciphertext[-16:]
    ciphertext = ciphertext[16:-16]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('utf-8')

def main():
    print("Choose an option:")
    print("1. Encode")
    print("2. Decode")
    choice = input("Enter your choice: ")

    if choice == '1':
        message = input("Enter the message to encode: ")
        aes_key = generate_aes_key()
        encoded_message = encrypt(message, aes_key)
        encoded_message = base64.b64encode(encoded_message).decode('utf-8')
        print(f"Encoded message: {encoded_message}")
        print(f"AES Key: {base64.b64encode(aes_key).decode('utf-8')}")

    elif choice == '2':
        encoded_message = input("Enter the encoded message: ")
        aes_key = input("Enter the AES key (base64 encoded) used for encoding: ")
        aes_key = base64.b64decode(aes_key)
        encoded_message = base64.b64decode(encoded_message)
        decoded_message = decrypt(encoded_message, aes_key)
        print(f"Decoded message: {decoded_message}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
