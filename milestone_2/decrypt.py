def decrypt(message, key):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            char = chr((ord(char) - key - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
        decrypted_message += char
    return decrypted_message

if __name__ == "__main__":
    key = int(input("Enter key: "))
    message = input("Enter message: ")
    result = decrypt(message, key)
    print(f"Result: {result}")