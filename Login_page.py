import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess
import os

def toggle_password():
    if show_password.get():
        entry_password.config(show="")
        label_showpass.config(fg="#008A44")
        check_showpass.config(bg="#008A44")
    else:
        entry_password.config(show="*")
        label_showpass.config(fg="white")
        check_showpass.config(bg="#262626")

def login():
    username = entry_name.get()
    password = entry_password.get()
    
    user_info = validate_login(username, password)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    if user_info:
        user_type, user_id = user_info
        main.destroy()  
        if user_type.lower() == 'admin':
            admin_page_path = os.path.join(current_dir, "admin_page.py")
            subprocess.run(["python", admin_page_path, str(user_id)])
        else:
            user_page_path = os.path.join(current_dir, "user_page.py")
            subprocess.run(["python", user_page_path, str(user_id)])
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def validate_login(username, password):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT user_type, id FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result if result else None 

def signup():
    subprocess.run(["python", "registration_page.py"])
    main.destroy()  # Close the login window

# Main window setup
main = tk.Tk()
main.title("Login Page")
main.geometry("500x500")
main.configure(bg='#868686')

show_password = tk.IntVar()

# Login frame
login_frame = tk.Frame(main, bg='#262626')

# Username
label_user_name = tk.Label(login_frame, text="Email or Username", fg='white', bg='#262626', font=("Arial", 18, "bold"))
entry_name = tk.Entry(login_frame, bg="#131313", fg="white", font=("Arial", 20), width=25, insertbackground="#008A44")

# Password
label_password = tk.Label(login_frame, text="Password", fg='white', bg='#262626', font=("Arial", 18, "bold"))
entry_password = tk.Entry(login_frame, bg="#131313", fg="white", show="*", font=("Arial", 20), width=25, insertbackground="#008A44")

# Show password
check_showpass = tk.Checkbutton(login_frame, bg="#262626", fg="black", borderwidth=0, variable=show_password, onvalue=1, offvalue=0, command=toggle_password)
label_showpass = tk.Label(login_frame, text="Show password", bg="#262626", fg="white", font=("Arial", 10))

# Login button
button_Login = tk.Button(login_frame, text="LOG IN", bg='#008A44', fg="white", font=("Arial", 12, "bold"), width=12, command=login)

# Forgot password
button_forgot_pass = tk.Button(login_frame, text="Forgot Password?", borderwidth=0, font=("Arial", 10, "underline"), fg="white", bg="#262626")

# Sign up
label_signup = tk.Label(login_frame, text="Don't have an account?", font=("Arial", 11), bg="#262626", fg="#b9b9b9")
button_signup = tk.Button(login_frame, text="Sign up", borderwidth=0, font=("Arial", 10, "underline"), fg="white", bg="#262626", command=signup)

# Placing widgets
label_user_name.grid(row=1, column=0, padx=40, pady=(60,5), sticky="w")
entry_name.grid(row=2, column=0, padx=40, pady=5, sticky="w")
label_password.grid(row=3, column=0, padx=40, pady=5, sticky="w")
entry_password.grid(row=4, column=0, padx=40, pady=5, sticky="w")
check_showpass.grid(row=5, column=0, padx=(40,0), pady=5, sticky="w")
label_showpass.grid(row=5, column=0, padx=(60,0), pady=5, sticky="w")
button_Login.grid(row=6, column=0, pady=5, columnspan=2)
button_forgot_pass.grid(row=7, column=0, pady=5, columnspan=2)
label_signup.grid(row=8, column=0, padx=(118,0), pady=5, sticky="nw")
button_signup.grid(row=8, column=0, padx=(140,0), pady=(5,60))

# Centering the frame
login_frame.place(relx=.5, rely=.5, anchor=tk.CENTER)

main.mainloop()
