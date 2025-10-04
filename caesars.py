# Caesar Cipher Program

def encrypt(text, shift):
    if text is None:
        return ""
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def get_shift():
    while True:
        shift_input = input("Enter shift value (e.g. 3):  ")
        if shift_input.isdigit():
            return int(shift_input)
        else:
            print(" Shift must be a number. try again. ")

def get_message():
    while True:
        message = input("Enter your message: ")
        if message.strip() != " ":
            return message
        else:
            print(" Message cannot be empty. Try again. ")

# Main Program
print("=== Caesar Cipher Menu ===")
print("1. Encrypt")
print("2. Decrypt")
choice = input("Choose an option (1 or 2): ")

if choice not in ['1', '2']:
    print(" Invalid choice. Exiting. ")
    exit()

message = get_message()
shift = get_shift()

if choice =='1':
    encrypted_message = encrypt(message, shift)
    print(f"\n Encrypted message: {encrypted_message}")
elif choice == '2':
    decrypted_message = decrypt(message, shift)
    print(f"\n Decrypted message: {decrypted_message}")
