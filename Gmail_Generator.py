import tkinter as tk
import random
import string


# Lists for random generation
adjectives = ["cool", "fast", "tech", "pro", "smart", "quick", "code", "dev", "neo", "cyber"]
names = ["user", "guy", "kid", "bot", "ninja", "hero", "star", "boss", "guru", "master"]
domains = ["gmail.com", "yahoo.com", "outlook.com"]


def generate_gmail():
    adj = random.choice(adjectives)
    name = random.choice(names)
    num = ''.join(random.choices(string.digits, k=3))
    domain = random.choice(domains)
    email = f"{adj}{name}{num}@{domain}"
    entry.delete(0, tk.END)
    entry.insert(0, email)
    label_status.config(text=f"Generated: {email}", foreground="green")


def copy_email():
    email = entry.get()
    if email:
        root.clipboard_clear()
        root.clipboard_append(email)
        label_status.config(text="Copied to clipboard!", foreground="blue")
    else:
        label_status.config(text="Nothing to copy.", foreground="red")


# Main window setup
root = tk.Tk()
root.title("Gmail Generator")
root.geometry("400x220")
root.resizable(False, False)


# Title
title_label = tk.Label(root, text="Random Gmail Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)


# Entry field for email display
entry = tk.Entry(root, font=("Arial", 12), width=35, justify="center")
entry.pack(pady=5)


# Generate button
generate_btn = tk.Button(
    root,
    text="Generate Email",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=generate_gmail,
    relief="flat",
    padx=20,
    pady=5,
    width=20
)
generate_btn.pack(pady=5)


# Copy button (bigger, same style)
copy_btn = tk.Button(
    root,
    text="Copy Email",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=copy_email,
    relief="flat",
    padx=20,
    pady=5,
    width=20
)
copy_btn.pack(pady=5)


# Status label
label_status = tk.Label(root, text="Click Generate to create email", font=("Arial", 10))
label_status.pack(pady=5)


root.mainloop()



in this code give me like the title for youtube video and dricption and thumanil idea
