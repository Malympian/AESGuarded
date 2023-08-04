import base64

def reverse_text(text):
    return text[::-1]

def encode_base64(text):
    return base64.urlsafe_b64encode(text.encode()).decode()

def decode_base64(text):
    try:
        return base64.urlsafe_b64decode(text).decode()
    except base64.binascii.Error:
        # Try decoding without padding if there's an incorrect padding error
        padding = len(text) % 4
        if padding:
            text += '=' * (4 - padding)
        return base64.urlsafe_b64decode(text).decode()

def main():
    while True:
        action = input("Do you want to encode or decode? (Type 'encode' or 'decode' or 'exit' to quit): ").lower()

        if action == 'exit':
            print("Exiting the program.")
            break

        if action not in ('encode', 'decode'):
            print("Invalid option. Please choose 'encode', 'decode', or 'exit'.")
            continue

        input_text = input("Enter the text: ")

        if action == 'encode':
            reversed_text = reverse_text(input_text)
            encoded_text = encode_base64(reversed_text)
            print("Encoded and Reversed text:", encoded_text)
        elif action == 'decode':
            decoded_text = decode_base64(input_text)
            reversed_text = reverse_text(decoded_text)
            print("Decoded and Reversed text:", reversed_text)

if __name__ == "__main__":
    main()
