# import random
# import string

# class PasswordGenerator:
#     def __init__(self):
#         self.lowercase_letters = string.ascii_lowercase
#         self.uppercase_letters = string.ascii_uppercase
#         self.digits = string.digits
#         self.special_chars = string.punctuation

#     def generate_password(self, length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
#         chars = ""

#         if use_lowercase:
#             chars += self.lowercase_letters
#         if use_uppercase:
#             chars += self.uppercase_letters
#         if use_digits:
#             chars += self.digits
#         if use_special_chars:
#             chars += self.special_chars

#         if not chars:
#             return "No character set selected."

#         password = ''.join(random.choice(chars) for _ in range(length))
#         return password

# def main():
#     password_generator = PasswordGenerator()

#     try:
#         length = int(input("Enter the desired length of the password: "))
#         use_lowercase = input("Use lowercase letters? (y/n): ").lower() == 'y'
#         use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
#         use_digits = input("Use digits? (y/n): ").lower() == 'y'
#         use_special_chars = input("Use special characters? (y/n): ").lower() == 'y'

#         password = password_generator.generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
#         print("Generated Password:", password)
#     except ValueError:
#         print("Invalid input. Please enter a valid length.")

# if __name__ == "__main__":
#     main()




import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(root , width = 40 )
        self.length_entry.pack()

        self.lowercase_var = tk.IntVar()
        self.lowercase_checkbox = tk.Checkbutton(root, text="Lowercase Letters", variable=self.lowercase_var)
        self.lowercase_checkbox.pack()

        self.uppercase_var = tk.IntVar()
        self.uppercase_checkbox = tk.Checkbutton(root, text="Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_checkbox.pack()

        self.digits_var = tk.IntVar()
        self.digits_checkbox = tk.Checkbutton(root, text="Digits", variable=self.digits_var)
        self.digits_checkbox.pack()

        self.special_chars_var = tk.IntVar()
        self.special_chars_checkbox = tk.Checkbutton(root, text="Special Characters", variable=self.special_chars_var)
        self.special_chars_checkbox.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(root, text="")
        self.password_label.pack()

    def generate_password(self):
        length = self.length_entry.get()

        if not length.isdigit():
            messagebox.showerror("Error", "Please enter a valid password length.")
            return

        length = int(length)
        use_lowercase = bool(self.lowercase_var.get())
        use_uppercase = bool(self.uppercase_var.get())
        use_digits = bool(self.digits_var.get())
        use_special_chars = bool(self.special_chars_var.get())

        if not (use_lowercase or use_uppercase or use_digits or use_special_chars):
            messagebox.showerror("Error", "Please select at least one character set.")
            return

        chars = ""
        if use_lowercase:
            chars += string.ascii_lowercase
        if use_uppercase:
            chars += string.ascii_uppercase
        if use_digits:
            chars += string.digits
        if use_special_chars:
            chars += string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_label.config(text="Generated Password: " + password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
