def vigenere_encrypt(plaintext, keyword):
    ciphertext = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    keyword_index = 0

    for char in plaintext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            k = ord(keyword[keyword_index % keyword_length]) - 65
            encrypted_char = chr((ord(char) - offset + k) % 26 + offset)
            ciphertext += encrypted_char
            keyword_index += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, keyword):
    plaintext = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    keyword_index = 0

    for char in ciphertext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            k = ord(keyword[keyword_index % keyword_length]) - 65
            decrypted_char = chr((ord(char) - offset - k + 26) % 26 + offset)
            plaintext += decrypted_char
            keyword_index += 1
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    text = input("Enter your message: ")
    keyword = input("Enter keyword: ")

    if choice == 'e':
        encrypted = vigenere_encrypt(text, keyword)
        print(f"Encrypted text: {encrypted}")
    elif choice == 'd':
        decrypted = vigenere_decrypt(text, keyword)
        print(f"Decrypted text: {decrypted}")
    else:
        print("Invalid choice.")
