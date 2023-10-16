import tkinter as tk
from tkinter import PhotoImage
string = "abcdefghijklmnopqrstuvwxyz"

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            offset = ord('a')
            shifted = (ord(char) - offset + shift) % 26
            encrypted_char = chr(shifted + offset)
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def modified_caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            offset = ord('a')
            shifted = (ord(char) - offset + shift) % 26
            encrypted_char = chr(shifted + offset)
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def rail_fence_encrypt(text, rails):
    fence = [[' ' for _ in range(len(text))] for _ in range(rails)]
    direction, row, col = 1, 0, 0

    for char in text:
        fence[row][col] = char
        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1
        row += direction
        col += 1

    encrypted_text = ''.join(''.join(row) for row in fence)
    return encrypted_text

def columnar_encrypt(text, key):
    keyword = text.lower()  # Convert the keyword to lowercase for consistency
    keyword_order = sorted(range(len(keyword)), key=lambda k: keyword[k])
    num_cols = len(keyword)
    num_rows = -(-len(text) // num_cols)  # Ceiling division

    # Pad the text if needed
    padded_text = text + ' ' * (num_cols * num_rows - len(text))

    # Create the matrix for encryption
    matrix = [[padded_text[i * num_cols + j] for j in keyword_order] for i in range(num_rows)]

    encrypted_text = ''.join(''.join(row) for row in matrix)
    return encrypted_text

def polyalphabetic_encrypt(text, key):
    encrypted_text = ""
    key_len = len(text)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            offset = ord('a')

            shift = ord(text[i % key_len]) - offset  # Get the shift value from the key
            shifted = (ord(char) - offset + shift) % 26
            encrypted_char = chr(shifted + offset)

            if is_upper:
                encrypted_char = encrypted_char.upper()

            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def monoalphabetic_encrypt(text, key):
    key = text.lower()  # Convert the key to lowercase for consistency
    key = key + ''.join(chr(i) for i in range(97, 123) if chr(i) not in key)  # Ensure the key has all lowercase letters

    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()  # Convert the character to lowercase for consistency
            offset = ord('a')

            if char in key:
                index = key.index(char)  # Find the index of the character in the key
                encrypted_char = key[(index + offset) % 26]  # Perform the substitution
            else:
                encrypted_char = char  # If the character is not in the key, leave it unchanged

            if is_upper:
                encrypted_char = encrypted_char.upper()

            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def encrypt_caesar():
    shift = int(shift_entry.get())
    plaintext = input_text.get("1.0", "end-1c")
    encrypted_text = caesar_cipher(plaintext, shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

def encrypt_modified_caesar():
    shift = int(shift_entry.get())
    plaintext = input_text.get("1.0", "end-1c")
    encrypted_text = modified_caesar_cipher(plaintext, shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

def rail_fence():
    shift = int(shift_entry.get())
    plaintext = input_text.get("1.0", "end-1c")
    encrypted_text = rail_fence_encrypt(plaintext, shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

def columnar():
    shift = int(shift_entry.get())
    plaintext = input_text.get("1.0", "end-1c")
    encrypted_text = columnar_encrypt(plaintext, shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

def polyalphabetic():
    shift = int(shift_entry.get())
    plaintext = input_text.get("1.0", "end-1c")
    encrypted_text = polyalphabetic_encrypt(plaintext, shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

def monoalphabetic():
    shift = int(shift_entry.get())
    plaintext = input_text.get("1.0", "end-1c")
    encrypted_text = monoalphabetic_encrypt(plaintext, shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

# Create the main window
window = tk.Tk()
window.title("Encryption Techniques")
background_image = PhotoImage(file="C:/Users/suraj/Downloads/2.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

blank_label = tk.Label(window, text="")  # An empty label acts as a blank line
blank_label.pack()

# Input text box
input_label = tk.Label(window, text="𝓔𝓷𝓽𝓮𝓻 𝓣𝓮𝔁𝓽 :")
input_label.pack()
blank_label = tk.Label(window, text="")  # An empty label acts as a blank line
blank_label.pack()
input_text = tk.Text(window, height=3, width=50, bg="light grey")
input_text.pack()

blank_label = tk.Label(window, text="")  # An empty label acts as a blank line
blank_label.pack()

# Shift value
shift_label = tk.Label(window, text="𝓚𝓮𝔂 :")
shift_label.pack()
blank_label = tk.Label(window, text="")  # An empty label acts as a blank line
blank_label.pack()
shift_entry = tk.Entry(window,bg="light grey")
shift_entry.pack()

blank_label = tk.Label(window, text="")  # An empty label acts as a blank line
blank_label.pack()

# Output text box
output_label = tk.Label(window, text="𝓡𝓮𝓼𝓾𝓵𝓽 :")
output_label.pack()
blank_label = tk.Label(window, text="")  # An empty label acts as a blank line
blank_label.pack()
output_text = tk.Text(window, height=3, width=50, bg="light grey")
output_text.pack()

blank_label = tk.Label(window, text="")  # An empty label acts as a blank line
blank_label.pack()

# Buttons for Caesar Cipher and Modified Caesar Cipher
caesar_button = tk.Button(window, text="Caesar Cipher", command=encrypt_caesar, bg="green", fg="white",height=3,width=20)
caesar_button.pack(side="left")

modified_caesar_button = tk.Button(window, text="Modified Caesar Cipher", command=encrypt_modified_caesar, bg="red",fg="white",height=3,width=20)
modified_caesar_button.pack(side="left")

rail_fence_button = tk.Button(window, text="Rail Fence", command=rail_fence, bg="yellow", fg="black",height=3,width=20)
rail_fence_button.pack(side="right")

columnar_button = tk.Button(window, text="Columnar", command=columnar, bg="blue", fg="white",height=3,width=20)
columnar_button.pack(side="right")

poly_button = tk.Button(window, text="Polyalphabetic", command=polyalphabetic, bg="purple", fg="white",height=3,width=20)
poly_button.pack(side="right")

poly_button = tk.Button(window, text="Monoalphabetic", command=monoalphabetic, bg="orange", fg="black",height=3,width=20)
poly_button.pack(side="left")
# Start the GUI event loop
window.mainloop()

