# **Password Manager**

The **Password Manager** is a Python-based project designed to securely store, encrypt, and retrieve user passwords. By leveraging the `cryptography` library, this tool ensures that all stored passwords are encrypted and accessible only with the correct encryption key. This project highlights essential skills in security-focused programming, including encryption, file management, and secure storage practices.

## Requirements 
- cryptography library

## Features

- **Save Passwords**: Encrypts and securely stores passwords for different services.
- **View Passwords**: Decrypts and displays stored passwords in a human-readable format.
- **Encryption Key Management**: Automatically generates a unique encryption key for each user and securely stores it.

## How It Works

1. When first run, the program generates an encryption key and saves it in a local file (`key.key`).
2. Passwords entered by the user are encrypted and saved in a `passwords.txt` file.
3. Users can view all stored passwords, which are decrypted using the same encryption key.

> ⚠️ **Important**: If the `key.key` file is deleted, all stored passwords will become inaccessible. Keep the key safe!

## Installation
To get started, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/Password_Manager.git
   cd Password_Manager

2. Install the required library:
   pip install cryptography

3. Run the script:
   python password_manager.py

## Usage
**Menu Options**
1. Save a new password:
    - Enter the name of the service (e.g., "Facebook") and the password to save.

2. View saved passwords:
    - View all stored passwords in decrypted format.

3. Exit:
    - Quit the program.

## Example Output

Password Manager
1. Save a new password
2. View saved passwords
3. Exit
Enter your choice: 1
Enter the service name: Facebook
Enter the password: SecurePass123!
Password saved for Facebook.

Password Manager
1. Save a new password
2. View saved passwords
3. Exit
Enter your choice: 2
Service: Facebook, Password: SecurePass123!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
