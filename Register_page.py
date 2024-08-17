import tkinter as tk
from tkinter import messagebox
import sqlite3
import re
import subprocess

def create_users_table():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY,
                  username TEXT UNIQUE,
                  password TEXT,
                  email TEXT UNIQUE,
                  full_name TEXT,
                  fine_amount INETGER DEFAULT 0,
                  user_type TEXT DEFAULT 'user')''')
    conn.commit()
    conn.close()

def toggle_password():
    if show_password.get():
        entry_password.config(show="")
        entry_confirm_password.config(show="")
        label_showpass.config(fg="#008A44")
        check_showpass.config(bg="#008A44")
    else:
        entry_password.config(show="*")
        entry_confirm_password.config(show="*")
        label_showpass.config(fg="white")
        check_showpass.config(bg="#262626")

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def register():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    email = entry_email.get()
    full_name = entry_full_name.get()
    
    if not all([username, password, confirm_password, email, full_name]):
        messagebox.showerror("Registration Failed", "All fields are required")
        return
    
    if password != confirm_password:
        messagebox.showerror("Registration Failed", "Passwords do not match")
        return
    
    if not validate_email(email):
        messagebox.showerror("Registration Failed", "Invalid email format")
        return
    
    if create_user(username, password, email, full_name):
        messagebox.showinfo("Registration Successful", "Account created for " + username)
        main.destroy()  # Close the registration window
        subprocess.run(["python", "Login_page.py"])  # Launch the login page
    else:
        messagebox.showerror("Registration Failed", "Username or email already exists")

def create_user(username, password, email, full_name):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password, email, full_name, user_type) VALUES (?, ?, ?, ?, ?)",
                  (username, password, email, full_name, 'user'))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

# Create the users table if it doesn't exist
create_users_table()

# Main window setup
main = tk.Tk()
main.title("Registration Page")
main.geometry("500x600")
main.configure(bg='#868686')

show_password = tk.IntVar()

# Registration frame
register_frame = tk.Frame(main, bg='#262626')

# Username
tk.Label(register_frame, text="Username", fg='white', bg='#262626', font=("Arial", 18, "bold")).grid(row=0, column=0, padx=40, pady=(30,5), sticky="w")
entry_username = tk.Entry(register_frame, bg="#131313", fg="white", font=("Arial", 16), width=25, insertbackground="#008A44")
entry_username.grid(row=1, column=0, padx=40, pady=5, sticky="w")

# Full Name
tk.Label(register_frame, text="Full Name", fg='white', bg='#262626', font=("Arial", 18, "bold")).grid(row=2, column=0, padx=40, pady=5, sticky="w")
entry_full_name = tk.Entry(register_frame, bg="#131313", fg="white", font=("Arial", 16), width=25, insertbackground="#008A44")
entry_full_name.grid(row=3, column=0, padx=40, pady=5, sticky="w")

# Email
tk.Label(register_frame, text="Email", fg='white', bg='#262626', font=("Arial", 18, "bold")).grid(row=4, column=0, padx=40, pady=5, sticky="w")
entry_email = tk.Entry(register_frame, bg="#131313", fg="white", font=("Arial", 16), width=25, insertbackground="#008A44")
entry_email.grid(row=5, column=0, padx=40, pady=5, sticky="w")

# Password
tk.Label(register_frame, text="Password", fg='white', bg='#262626', font=("Arial", 18, "bold")).grid(row=6, column=0, padx=40, pady=5, sticky="w")
entry_password = tk.Entry(register_frame, bg="#131313", fg="white", show="*", font=("Arial", 16), width=25, insertbackground="#008A44")
entry_password.grid(row=7, column=0, padx=40, pady=5, sticky="w")

# Confirm Password
tk.Label(register_frame, text="Confirm Password", fg='white', bg='#262626', font=("Arial", 18, "bold")).grid(row=8, column=0, padx=40, pady=5, sticky="w")
entry_confirm_password = tk.Entry(register_frame, bg="#131313", fg="white", show="*", font=("Arial", 16), width=25, insertbackground="#008A44")
entry_confirm_password.grid(row=9, column=0, padx=40, pady=5, sticky="w")

# Show password
check_showpass = tk.Checkbutton(register_frame, bg="#262626", fg="black", borderwidth=0, variable=show_password, onvalue=1, offvalue=0, command=toggle_password)
check_showpass.grid(row=10, column=0, padx=(40,0), pady=5, sticky="w")
label_showpass = tk.Label(register_frame, text="Show password", bg="#262626", fg="white", font=("Arial", 10))
label_showpass.grid(row=10, column=0, padx=(60,0), pady=5, sticky="w")

# Register button
button_register = tk.Button(register_frame, text="REGISTER", bg='#008A44', fg="white", font=("Arial", 12, "bold"), width=12, command=register)
button_register.grid(row=11, column=0, pady=20, columnspan=2)

# Centering the frame
register_frame.place(relx=.5, rely=.5, anchor=tk.CENTER)

main.mainloop()
