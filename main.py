# main.py

from my_cryptography import encode, decode

def main():
    while True:
        action = input("Encode or decode? (e/d): ")

        if action == 'e':
            input_text = input("Enter text to encode: ")
            try:
                encoded_text = encode(input_text)
                print("Encoded:", encoded_text)
            except Exception as e:
                print("Error occurred during encoding:", e)

        elif action == 'd':
            input_text = input("Enter text to decode: ")
            try:
                decoded_text = decode(input_text)
                print("Decoded:", decoded_text)
            except Exception as e:
                print("Error occurred during decoding:", e)

        elif action == 'exit':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please enter 'e', 'd', or 'exit.")

if __name__ == "__main__":
    main()
