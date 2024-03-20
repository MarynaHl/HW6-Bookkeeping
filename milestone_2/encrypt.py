def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            char = chr((ord(char) + key - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
        encrypted_message += char
    return encrypted_message

if __name__ == "__main__":
    key = int(input("Enter key: "))
    message = input("Enter message: ")
    result = encrypt(message, key)
    print(f"Result: {result}")