import tkinter as tk
from Crypto.Cipher import AES
import json

# Initialize the user interface
root = tk.Tk()

# Add input fields and buttons for adding, editing, and deleting passwords
website_entry = tk.Entry(root)
username_entry = tk.Entry(root)
password_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add")
edit_button = tk.Button(root, text="Edit")
delete_button = tk.Button(root, text="Delete")

# Encrypt and decrypt passwords using PyCrypto
key = b'mysecretpassword'
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce

def encrypt_password(password):
    ciphertext, tag = cipher.encrypt_and_digest(password.encode('utf-8'))
    return (ciphertext, tag, nonce)

def decrypt_password(ciphertext, tag, nonce):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('utf-8')

# Store and retrieve passwords from a JSON file
passwords = {}

def load_passwords():
    global passwords
    try:
        with open('passwords.json', 'r') as f:
            passwords = json.load(f)
    except FileNotFoundError:
        pass

def save_passwords():
    with open('passwords.json', 'w') as f:
        json.dump(passwords, f)

def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    encrypted_password = encrypt_password(password)
    passwords[website] = {'username': username, 'password': encrypted_password}
    save_passwords()

def edit_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    encrypted_password = encrypt_password(password)
    passwords[website] = {'username': username, 'password': encrypted_password}
    save_passwords()

def delete_password():
    website = website_entry.get()
    del passwords[website]
    save_passwords()

def get_password():
    website = website_entry.get()
    if website in passwords:
        password = passwords[website]['password']
        return decrypt_password(*password)
    else:
        return ''

# Load passwords from the JSON file on startup
load_passwords()

# Add the input fields and buttons to the user interface
website_entry.pack()
username_entry.pack()
password_entry.pack()
add_button.pack()
edit_button.pack()
delete_button.pack()

# Bind the add, edit, and delete