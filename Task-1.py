def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? (q to quit): ").lower()
        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")
            continue

        text = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            encrypted_text = caesar_cipher_encrypt(text, shift)
            print(f"Encrypted message: {encrypted_text}")
        elif choice == 'd':
            decrypted_text = caesar_cipher_decrypt(text, shift)
            print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
