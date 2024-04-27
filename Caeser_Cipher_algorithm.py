def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char  # Keep non-alphabetic characters unchanged
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char  # Keep non-alphabetic characters unchanged
    return decrypted_text

def main():
    # Input message and shift value from the user
    message = input("Enter the message to encrypt or decrypt: ")
    shift = int(input("Enter the shift value (positive integer): "))

    # Encrypt the message
    encrypted_message = caesar_encrypt(message, shift)
    print("Encrypted message:", encrypted_message)

    # Decrypt the encrypted message
    decrypted_message = caesar_decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
