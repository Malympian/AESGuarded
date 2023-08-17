import os
from my_cryptography import generate_aes_key, encode, decode

ENCODED_MESSAGES_FILE = "encoded_messages.txt"

def save_encoded_message(encoded_message):
    with open(ENCODED_MESSAGES_FILE, "a") as f:
        f.write(f"{encoded_message}\n")

def load_encoded_messages():
    encoded_messages = []
    try:
        with open(ENCODED_MESSAGES_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    encoded_messages.append(line)
    except FileNotFoundError:
        pass
    return encoded_messages

def main():
    aes_key = generate_aes_key()  # Generate a new AES key each time the program runs
    encoded_messages = load_encoded_messages()

    while True:
        action = input("Encode, decode, custom encode, custom decode, or exit? If you choose encode or decode strong randomly-generated AES keys (but not easy to remember) will be used. (e/d/ce/cd/exit): ")

        if action == 'e':
            input_text = input("Enter text to encode: ")
            try:
                _, encoded_text = encode(input_text, aes_key)
                save_encoded_message(encoded_text)
                print("Encoded:", encoded_text)
                print("__________________________________________________________")
                print("Your AES_KEY was", aes_key)
                print("Save the key for future reference or then you won't be able to decode the message. (you can use cd in the future.)")
                print("__________________________________________________________")
            except Exception as e:
                print("Error occurred during encoding:", e)

        elif action == 'd':
            encoded_text = input("Enter the encoded message you want to decode: ")
            try:
                decoded_text = decode(encoded_text, aes_key)
                print("Decoded:", decoded_text)
            except Exception as e:
                print("Error occurred during decoding:", e)

        elif action == 'ce':
            custom_aes_key = input("Enter the AES key for custom encoding: ")
            input_text = input("Enter text to custom encode: ")
            try:
                _, encoded_text = encode(input_text, custom_aes_key)
                print("Custom Encoded:", encoded_text)
            except Exception as e:
                print("Error occurred during custom encoding:", e)

        elif action == 'cd':
            custom_aes_key = input("Enter the AES key for custom decoding: ")
            custom_encoded_text = input("Enter the encoded message for custom decoding: ")
            try:
                decoded_text = decode(custom_encoded_text, custom_aes_key)
                print("Custom Decoded:", decoded_text)
            except Exception as e:
                print("Error occurred during custom decoding:", e)

        

        elif action == 'exit':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please enter 'e', 'd', 'ce', 'cd', or 'exit'.")

if __name__ == "__main__":
    main()
