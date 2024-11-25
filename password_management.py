from cryptography.fernet import Fernet
import os

# Generate or upload a cryptographic key
def load_or_create_key():
    key_file = "key.key"
    if os.path.exists(key_file):
        with open(key_file, "rb") as file:
            key = file.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, "wb") as file:
            file.write(key)
    return key

# Initialize the encryption manager
key = load_or_create_key()
cipher = Fernet(key)

# Save a new password
def save_password(service, password):
    encrypted_password = cipher.encrypt(password.encode())
    with open("passwords.txt", "a") as file:
        file.write(f"{service}:{encrypted_password.decode()}\n")
    print(f"Password saved for {service}.")

# View saved passwords
def view_passwords():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return
    with open("passwords.txt", "r") as file:
        for line in file:
            service, encrypted_password = line.strip().split(":")
            decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
            print(f"Service: {service}, Password: {decrypted_password}")

# Main menu
def main():
    while True:
        print("\nPassword Manager")
        print("1. Save a new password")
        print("2. View saved passwords")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Enter the service name: ")
            password = input("Enter the password: ")
            save_password(service, password)
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
