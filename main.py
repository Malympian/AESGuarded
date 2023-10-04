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
    try:
        nonce = ciphertext[:16]
        tag = ciphertext[-16:]
        ciphertext = ciphertext[16:-16]
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode('utf-8')
    except (ValueError, KeyError):
        return None  # Return None if decryption fails

def main():
    while True:  # Continue looping until the user chooses to exit
        print("Choose an option:")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

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
            if decoded_message is not None:
                print(f"Decoded message: {decoded_message}")
            else:
                print("Decryption failed. Invalid AES key or encoded message.")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break  # Exit the loop and end the program

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
