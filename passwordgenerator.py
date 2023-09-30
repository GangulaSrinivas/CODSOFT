import tkinter as tk
import random
import string

def generate_password(length, include_lowercase, include_uppercase, include_digits, include_special_chars):
    characters = ""
    
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    
    if not characters:
        return "Complexity options are not selected."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_clicked():
    try:
        password_length = int(length_entry.get())
        include_lowercase = lowercase_var.get() == 1
        include_uppercase = uppercase_var.get() == 1
        include_digits = digits_var.get() == 1
        include_special_chars = special_chars_var.get() == 1

        generated_password = generate_password(password_length, include_lowercase, include_uppercase, include_digits, include_special_chars)
        result_text.delete("1.0", tk.END)  # Clear previous result
        result_text.insert(tk.END, "Generated Password:\n" + generated_password)
    except ValueError:
        result_text.delete("1.0", tk.END)  # Clear previous result
        result_text.insert(tk.END, "Invalid input. Please enter a valid number for password length.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Increase the size of the window
window.geometry("400x400")

# Password Length
length_label = tk.Label(window, text="Password Length:")
length_entry = tk.Entry(window)
length_label.pack()
length_entry.pack()

# Complexity Options
lowercase_var = tk.IntVar()
lowercase_check = tk.Checkbutton(window, text="Lowercase Letters", variable=lowercase_var)
lowercase_check.pack()

uppercase_var = tk.IntVar()
uppercase_check = tk.Checkbutton(window, text="Uppercase Letters", variable=uppercase_var)
uppercase_check.pack()

digits_var = tk.IntVar()
digits_check = tk.Checkbutton(window, text="Digits", variable=digits_var)
digits_check.pack()

special_chars_var = tk.IntVar()
special_chars_check = tk.Checkbutton(window, text="Special Characters", variable=special_chars_var)
special_chars_check.pack()

# Generate Password Button
generate_button = tk.Button(window, text="Generate Password", command=generate_password_button_clicked)
generate_button.pack()

# Display Result (Larger Text Area)
result_text = tk.Text(window, height=8, width=30)
result_text.pack()

# Start the GUI event loop
window.mainloop()
