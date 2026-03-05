import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        if length < 4:
            result_label.config(text="Length should be at least 4")
            return
        
        all_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_chars) for _ in range(length))
        result_label.config(text="Generated Password: " + password)
    except ValueError:
        result_label.config(text="Enter a valid number!")


root = tk.Tk()
root.title("Password Generator GUI")

tk.Label(root, text="Enter password length:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()