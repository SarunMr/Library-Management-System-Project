import tkinter as tk
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

main = tk.Tk()
main.geometry("500x500")
main.configure(bg="black")
login_frame = tk.Frame(main, bg='#262626')

def toggle_password():
    if show_password.get():
        entry_password.config(show="")
        label_showpass.config(fg="#008A44")
        check_showpass.config(bg="#008A44")
    else:
        entry_password.config(show="*")
        label_showpass.config(fg="white")
        check_showpass.config(bg="#262626")

def change_password():
    username = entry_name.get()
    new_password = entry_password.get()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user:
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
        conn.commit()
        messagebox.showinfo("Success", "Password changed successfully!")
    else:
        messagebox.showerror("Error", "Username not found.")

# Username
show_password = tk.IntVar()
label_user_name = tk.Label(login_frame, text="Email or Username", fg='white', bg='#262626', font=("Arial", 18, "bold"))
entry_name = tk.Entry(login_frame, bg="#131313", fg="white", font=("Arial", 20), width=25, insertbackground="#008A44")

# Password
label_password = tk.Label(login_frame, text="Enter New Password", fg='white', bg='#262626', font=("Arial", 18, "bold"))
entry_password = tk.Entry(login_frame, bg="#131313", fg="white", show="*", font=("Arial", 20), width=25, insertbackground="#008A44")

# Show password
check_showpass = tk.Checkbutton(login_frame, bg="#262626", fg="black", borderwidth=0, onvalue=1, offvalue=0, variable=show_password, command=toggle_password)
label_showpass = tk.Label(login_frame, text="Show password", bg="#262626", fg="white", font=("Arial", 10))

# Login button
change_Login = tk.Button(login_frame, text="Change Password", bg='#008A44', fg="white", font=("Arial", 12, "bold"), width=15, command=change_password)

# Placing widgets
label_user_name.grid(row=1, column=0, padx=40, pady=(60,5), sticky="w")
entry_name.grid(row=2, column=0, padx=40, pady=5, sticky="w")
label_password.grid(row=3, column=0, padx=40, pady=5, sticky="w")
entry_password.grid(row=4, column=0, padx=40, pady=5, sticky="w")
check_showpass.grid(row=5, column=0, padx=(40,0), pady=5, sticky="w")
label_showpass.grid(row=5, column=0, padx=(60,0), pady=5, sticky="w")
change_Login.grid(row=6, column=0, pady=(5,30), columnspan=2)

# Centering the frame
login_frame.place(relx=.5, rely=.5, anchor=tk.CENTER)

def on_closing():
    conn.close()
    main.destroy()

main.protocol("WM_DELETE_WINDOW", on_closing)

main.mainloop()
