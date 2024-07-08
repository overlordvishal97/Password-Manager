# Password-Manager
This is a password manager application built with tkinter. It allows users to generate strong passwords, save them to a text file, and copy them to the clipboard.

# Usage
Run the code in a Python environment with tkinter installed.
A window will appear with a lock image, input fields for website, email, and password, and two buttons: "Generate Password" and "Add".
Enter a website and email address in the respective input fields.
Click the "Generate Password" button to generate a strong password.
The generated password will be displayed in the password input field and copied to the clipboard.
Click the "Add" button to save the website, email, and password to a text file named "data.txt".
The input fields will be cleared after saving.

# Features
Password generator with a mix of uppercase and lowercase letters, numbers, and symbols
Password copying to the clipboard
Saving of website, email, and password to a text file
User-friendly GUI interface

# Technical Details
The application uses the tkinter library to create the GUI.
The generating_password function generates a strong password using a combination of letters, numbers, and symbols.
The save function saves the website, email, and password to a text file and clears the input fields.
The pyperclip library is used to copy the generated password to the clipboard.
