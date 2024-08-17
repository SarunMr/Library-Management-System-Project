from tkinter import *
from PIL import *
import tkinter.ttk as ttk
from tkinter import messagebox
import os
import sqlite3
import tkinter as tk
import shutil
import sys
from datetime import datetime,timedelta
import subprocess


user_id = int(sys.argv[1])

def setup_database():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Create books table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT,
        available INTEGER DEFAULT 1,
        image_path TEXT,
        added_date DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        full_name TEXT,
        user_type TEXT DEFAULT 'regular',
        fine_amount REAL DEFAULT 0.0,
        registration_date DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create book_requests table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS book_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        book_id INTEGER,
        request_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        status TEXT DEFAULT 'pending',
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (book_id) REFERENCES books (id)
    )
    ''')

    conn.commit()
    conn.close()

    print("Database setup completed successfully.")


setup_database()




#theme color.
TEXTCOLOR ="#FFFFFF"
FRAME_TITLEBAR_BG ="#008A44"
FRAME_MENUBAR_BG = "#262626"
SWITCH_COLOR = "#5F5F5F"
FRAME_DASHBOARD_BG = '#343233'

window = Tk()
window.configure(bg=FRAME_DASHBOARD_BG,)
#icons
menubutton_icon = PhotoImage(file="icons_lib/menu_button.png")
menubuttontoggle_icon = PhotoImage(file="icons_lib/cross.png")
dashboard_icon = PhotoImage(file="icons_lib/dash_icon.png")
request_books_icon = PhotoImage(file="icons_lib/request_books_icon.png")
return_books_icon = PhotoImage(file="icons_lib/return_ic.png")
books_log_icon =PhotoImage(file="icons_lib/log_icon.png")
profile_icon =PhotoImage(file="icons_lib/profile.png")
logout_icon = PhotoImage(file="icons_lib/logout_icon.png")

#books
b1=PhotoImage(file="books/b1.png")

window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1,weight=1)
window.grid_rowconfigure(1,weight=1)

def logout():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    login_page_path = os.path.join(current_dir, "Login_page.py")
    
    window.destroy()
    
    try:
        subprocess.Popen([sys.executable, login_page_path])
        
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred while opening the login page: {e}")
        sys.exit(1)

def update_label_color_on_tap(n):
    label_dict = {"1":lib_dash_label,"2":lib_requestbook_label,"3":lib_returnbook_label,"4":lib_profile_label}
    btn_dict = {"1":lib_dash_button,"2":lib_request_book_button,"3":lib_return_book_button,"4":lib_profile_button}
    for label in label_dict.keys():
        if label == n:
            label_dict[label].config(bg=SWITCH_COLOR)
            btn_dict[label].config(bg=SWITCH_COLOR)
        else:
            label_dict[label].config(bg=FRAME_MENUBAR_BG)
            btn_dict[label].config(bg=FRAME_MENUBAR_BG)



def default_menubar():
    labellst = [lib_dash_label,lib_requestbook_label,lib_returnbook_label,lib_profile_label]
    for label in labellst:
        label.config(width=10)
   
    lib_menu_button.config(image=menubutton_icon)
    lib_dash_button.config(text="",width=45,)
    lib_request_book_button.config(text="",width=45)
    lib_return_book_button.config(text="",width=45)
    lib_profile_button.config(text="",width=45)
    lib_logout_button.config(text="")
    lib_menu_button.config(command=extend_menubar)


def extend_menubar():
    labellst = [lib_dash_label,lib_requestbook_label,lib_returnbook_label,lib_profile_label]
    for label in labellst:
        label.config(width=40)

    lib_menu_button.config(image=menubuttontoggle_icon,padx=13,pady=30)
    lib_dash_button.config(text="Dashboard",width=200,padx=20,anchor="w")
    lib_request_book_button.config(text="Request Books",width=200,padx=20,anchor="w")
    lib_return_book_button.config(text="Return Books",width=200,padx=20,anchor="w")
    # lib_log_button.config(text="Books Log",width=200,padx=20,anchor="w")
    lib_profile_button.config(text="Your Profile",width=200,padx=20,anchor="w")
    lib_logout_button.config(text="Log out")
    lib_menu_button.config(command=default_menubar)

def dashboardframe():
    frame_dashboard = tk.Frame(window, bg=FRAME_DASHBOARD_BG, width=1120)
    frame_dashboard.grid_propagate(0)

    # Fetch user's name
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT full_name FROM users WHERE id = ?", (user_id,))
    user_name = cursor.fetchone()[0]
    conn.close()

    welcome_label = tk.Label(frame_dashboard, text=f"WELCOME {user_name}", font=("Arial", 30, "bold"), fg=FRAME_TITLEBAR_BG, bg=FRAME_DASHBOARD_BG, anchor="w", width=45)
    welcome_label.grid(row=0, column=0, padx=15, pady=(10,0), sticky="wn")

    frametracker = tk.Frame(frame_dashboard, bg=FRAME_DASHBOARD_BG)
    frametracker.grid_columnconfigure(0, weight=1)
    frametracker.grid_columnconfigure(1, weight=1)
    frametracker.grid_columnconfigure(2, weight=1)

    # Total Books
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]

    frametotalbooks = tk.Frame(frametracker, bg=FRAME_MENUBAR_BG)
    frametotalbooks.grid(row=0, column=0, padx=(15,20), sticky="w")
    labeltotalbooks = tk.Label(frametotalbooks, text="Total Books", font=("ArialBold", 16), fg=TEXTCOLOR, bg=FRAME_MENUBAR_BG, width=16)
    labelbooksquantity = tk.Label(frametotalbooks, text=str(total_books), font=("ArialBold", 16), fg=TEXTCOLOR, bg=FRAME_MENUBAR_BG)
    labeltotalbooks.grid(row=0, column=0, padx=20, pady=(10,5))
    labelbooksquantity.grid(row=1, column=0, pady=5)

    # Total Requests by User
    cursor.execute("SELECT COUNT(*) FROM book_requests WHERE user_id = ?", (user_id,))
    total_requests = cursor.fetchone()[0]

    frametotalrequests = tk.Frame(frametracker, bg=FRAME_MENUBAR_BG)
    frametotalrequests.grid(row=0, column=1, padx=80)
    labeltotalrequests = tk.Label(frametotalrequests, text="My Total Requests", font=("ArialBold", 16), fg=TEXTCOLOR, bg=FRAME_MENUBAR_BG, width=16)
    labelrequestquantity = tk.Label(frametotalrequests, text=str(total_requests), font=("ArialBold", 16), fg=TEXTCOLOR, bg=FRAME_MENUBAR_BG)
    labeltotalrequests.grid(row=0, column=0, padx=20, pady=(10,5))
    labelrequestquantity.grid(row=1, column=0, pady=5)

    # Total Fines
    cursor.execute("SELECT fine_amount FROM users WHERE id = ?", (user_id,))
    total_fines = cursor.fetchone()[0]

    frametotalfines = tk.Frame(frametracker, bg=FRAME_MENUBAR_BG)
    frametotalfines.grid(row=0, column=2, padx=(20,15), sticky="e")
    labeltotalfines = tk.Label(frametotalfines, text="Fines Remaining", font=("ArialBold", 16), fg=TEXTCOLOR, bg=FRAME_MENUBAR_BG, width=16)
    labelfinesquantity = tk.Label(frametotalfines, text=f"${total_fines:.2f}", font=("ArialBold", 16), fg=TEXTCOLOR, bg=FRAME_MENUBAR_BG)
    labeltotalfines.grid(row=0, column=0, padx=20, pady=(10,5))
    labelfinesquantity.grid(row=1, column=0, pady=5)

    conn.close()

    quickreqlabel = tk.Label(frame_dashboard, text="All Books", font=("ArialBold", 14), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    quickreqlabel.grid(row=2, column=0, padx=25, pady=(4,3), sticky="w")

    # Create Treeview for All Books
    columns = ("Book ID", "Book Name", "Author", "Available")
    tree = ttk.Treeview(frame_dashboard, columns=columns, show="headings", height=10)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.grid(row=3, column=0, padx=(25,25), pady=2, sticky="wne")

    # Populate Treeview with book data
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, available FROM books")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

    # Add scrollbar to Treeview
    scrollbar = ttk.Scrollbar(frame_dashboard, orient="vertical", command=tree.yview)
    scrollbar.grid(row=3, column=1, sticky="ns")
    tree.configure(yscrollcommand=scrollbar.set)

    frametracker.grid(row=1, column=0, padx=10, pady=2, sticky="wne")

    frame_dashboard.grid(row=1, column=1, padx=(20,0), pady=(10,0), sticky="ns")

    return frame_dashboard

def makerequestframe():
    framemakerequest = tk.Frame(window, bg=FRAME_DASHBOARD_BG, width=1120)
    framemakerequest.grid_propagate(0)
   
    framepagetitle = tk.Frame(framemakerequest, bg=FRAME_DASHBOARD_BG, width=1100, height=40)
    framepagetitle.grid_propagate(0)
    framepagetitle.grid_columnconfigure(0, weight=1)
    framepagetitle.grid_columnconfigure(1, weight=0)
    framepagetitle.grid_columnconfigure(2, weight=0)

    libtopbooks = tk.Label(framepagetitle, text="Your Request History", font=("Arial", 16, "bold"), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR, anchor="w")
    libtopbooks.grid(row=0, column=0, padx=(20,0), pady=5, sticky="wne")

    # Fetch max and remaining requests
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM book_requests WHERE user_id = ? AND status IN ('pending', 'accepted')", (user_id,))
    current_requests = cursor.fetchone()[0]
    max_requests = 3
    remaining_requests = max_requests - current_requests

    framepagetitle.grid(row=0, column=0, padx=10, pady=10, sticky="ne")

    # Request History Table
    history_frame = tk.Frame(framemakerequest, bg=FRAME_MENUBAR_BG)
    history_frame.grid(row=1, column=0, padx=25, pady=2, sticky="wne")

    columns = ("Request ID", "Book Name", "Request Date", "Status", "Due Date")
    tree = ttk.Treeview(history_frame, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=scrollbar.set)

    # Populate history table
    cursor.execute("""
        SELECT br.id, b.title, br.request_date, br.status,
               date(br.request_date, '+15 days') as due_date
        FROM book_requests br
        JOIN books b ON br.book_id = b.id
        WHERE br.user_id = ?
        ORDER BY br.request_date DESC
    """, (user_id,))
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

    lblrqstbooks = tk.Label(framemakerequest, text="Make Request", font=("Arial", 16, "bold"), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR)
    lblrqstbooks.grid(row=2, column=0, padx=25, pady=15, sticky='w')

    frame_request_label = tk.Frame(framemakerequest, bg=FRAME_DASHBOARD_BG)
    frame_request_label.grid_columnconfigure(0, weight=0)
    frame_request_label.grid_columnconfigure(1, weight=1)

    lblbookID = tk.Label(frame_request_label, text="Book ID:", font=("Arial", 12, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblbookID.grid(row=0, column=0, padx=(80,20), pady=(25,15), sticky="e")
    entbookID = tk.Entry(frame_request_label, font=("Arial", 14))
    entbookID.grid(row=0, column=1, pady=5, sticky="w")

    lblbookName = tk.Label(frame_request_label, text="Book Name:", font=("Arial", 12, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblbookName.grid(row=1, column=0, padx=(80,20), pady=15, sticky="e")
    entbookName = tk.Entry(frame_request_label, font=("Arial", 14))
    entbookName.grid(row=1, column=1, pady=15, sticky="w")

    selected_days = tk.StringVar()
    selected_days.set("15")
    days_label = tk.Label(frame_request_label, text="Days:", font=("Arial", 12, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    days_label.grid(row=2, column=0, padx=(80,10), pady=15, sticky="e")
    rb_15 = tk.Radiobutton(frame_request_label, text="15", font=("Arial", 12, "bold"), variable=selected_days, value="15", bg=FRAME_DASHBOARD_BG, fg="white", selectcolor=FRAME_DASHBOARD_BG, highlightthickness=0)
    rb_15.grid(row=2, column=1, pady=15, sticky="w")
    rb_10 = tk.Radiobutton(frame_request_label, text="10", font=("Arial", 12, "bold"), variable=selected_days, value="10", bg=FRAME_DASHBOARD_BG, fg="white", selectcolor=FRAME_DASHBOARD_BG, highlightthickness=0)
    rb_10.grid(row=2, column=1, pady=15, padx=(60,0), sticky="w")

    frame_request_label.grid(row=3, column=0, padx=25, pady=(15,5), sticky="we")

    def send_request():
        nonlocal remaining_requests
        if remaining_requests <= 0:
            messagebox.showerror("Error", "You have reached the maximum number of requests.")
            return

        book_id = entbookID.get()
        book_name = entbookName.get()
        days = int(selected_days.get())

        if not book_id or not book_name:
            messagebox.showerror("Error", "Please enter both Book ID and Book Name.")
            return

        try:
            cursor.execute("SELECT id FROM books WHERE id = ? AND title = ?", (book_id, book_name))
            book = cursor.fetchone()
            if not book:
                messagebox.showerror("Error", "Book not found or ID doesn't match the title.")
                return

            request_date = datetime.now()
            due_date = request_date + timedelta(days=days)

            cursor.execute("""
                INSERT INTO book_requests (user_id, book_id, request_date, status)
                VALUES (?, ?, ?, ?)
            """, (user_id, book_id, request_date.strftime("%Y-%m-%d %H:%M:%S"), "pending"))
            conn.commit()
            messagebox.showinfo("Success", f"Request sent successfully! Due date: {due_date.strftime('%Y-%m-%d')}")
            
            # Refresh the request history
            tree.delete(*tree.get_children())
            cursor.execute("""
                SELECT br.id, b.title, br.request_date, br.status,
                       date(br.request_date, '+' || ? || ' days') as due_date
                FROM book_requests br
                JOIN books b ON br.book_id = b.id
                WHERE br.user_id = ?
                ORDER BY br.request_date DESC
            """, (days, user_id))
            for row in cursor.fetchall():
                tree.insert("", tk.END, values=row)

            # Update remaining requests
            remaining_requests -= 1
            libremrequest.config(text=f"Remaining Request: {remaining_requests}")

            # Clear entry fields
            entbookID.delete(0, tk.END)
            entbookName.delete(0, tk.END)

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    sendrequestbutton = tk.Button(framemakerequest, text="Send Request", bg='#008A44', fg=TEXTCOLOR, font=("Arial", 12, "bold"), command=send_request)
    sendrequestbutton.grid(row=4, column=0, pady=30)

    framemakerequest.grid(row=1, column=1, padx=(20,0), pady=(10,0), sticky="ns")

    return framemakerequest

def returnbooksframe():
    framereturnbooks = tk.Frame(window, bg=FRAME_DASHBOARD_BG, width=1120)
    framereturnbooks.grid_propagate(0)
    
    lblYourbooks = tk.Label(framereturnbooks, text="Your Borrowed Books", font=("Arial", 18, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblYourbooks.grid(row=0, column=0, pady=20)
    
    # Table to display borrowed books
    framechoosebook = tk.Frame(framereturnbooks, bg=FRAME_MENUBAR_BG, height=300, width=1080)
    framechoosebook.grid_propagate(0)
    framechoosebook.grid(row=1, column=0, padx=20, pady=2, sticky="wne")
    
    columns = ("Book ID", "Book Name", "Author", "Issue Date", "Due Date")
    tree = ttk.Treeview(framechoosebook, columns=columns, show="headings", height=10)
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=200)
    
    tree.grid(row=0, column=0, sticky="nsew")
    
    # Add scrollbar
    scrollbar = ttk.Scrollbar(framechoosebook, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    tree.configure(yscrollcommand=scrollbar.set)
    
    framechoosebook.grid_columnconfigure(0, weight=1)
    framechoosebook.grid_rowconfigure(0, weight=1)
    
    # Populate the table with borrowed books
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.id, b.title, b.author, br.request_date,
               date(br.request_date, '+14 days') as due_date
        FROM book_requests br
        JOIN books b ON br.book_id = b.id
        WHERE br.user_id = ? AND br.status = 'accepted'
    """, (user_id,))
    
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    
    labelreturnbook = tk.Label(framereturnbooks, text="Return Book", font=("Arial", 15, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    labelreturnbook.grid(row=2, column=0, padx=100, pady=10, sticky="w")
    
    framereturndetails = tk.Frame(framereturnbooks, background=FRAME_DASHBOARD_BG)
    lblBookID = tk.Label(framereturndetails, text="Book ID:", font=("Arial", 12, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblBookID.grid(row=0, column=0, padx=(80,20), pady=(25,15), sticky="e")
    entbookID = tk.Entry(framereturndetails, font=("Arial", 14))
    entbookID.grid(row=0, column=1, pady=5)
    
    lblbookName = tk.Label(framereturndetails, text="Book Name:", font=("Arial", 12, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblbookName.grid(row=0, column=2, padx=(140,20), pady=(25,15))
    entbookName = tk.Entry(framereturndetails, font=("Arial", 14), width=30)
    entbookName.grid(row=0, column=3, padx=(0,10), pady=5, sticky="e")
    
    lblAuthor = tk.Label(framereturndetails, text="Author:", font=("Arial", 12, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblAuthor.grid(row=1, column=0, padx=(80,20), pady=(25,15), sticky="e")
    entAuthor = tk.Entry(framereturndetails, font=("Arial", 14))
    entAuthor.grid(row=1, column=1, pady=5)
    
    lblIssueDate = tk.Label(framereturndetails, text="Issue Date:", font=("Arial", 12, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblIssueDate.grid(row=1, column=2, padx=(140,20), pady=(25,15))
    entIssueDate = tk.Entry(framereturndetails, font=("Arial", 14), width=30)
    entIssueDate.grid(row=1, column=3, padx=(0,10), pady=5, sticky="e")
    
    framereturndetails.grid(row=3, column=0, padx=(20,0), pady=(10,0), sticky="ns")
    
    def on_tree_select(event):
        selected_item = tree.selection()[0]
        values = tree.item(selected_item)['values']
        entbookID.delete(0, tk.END)
        entbookID.insert(0, values[0])
        entbookName.delete(0, tk.END)
        entbookName.insert(0, values[1])
        entAuthor.delete(0, tk.END)
        entAuthor.insert(0, values[2])
        entIssueDate.delete(0, tk.END)
        entIssueDate.insert(0, values[3])
    
    tree.bind("<Double-1>", on_tree_select)
    
    def return_book():
        book_id = entbookID.get()
        if not book_id:
            messagebox.showerror("Error", "Please select a book to return")
            return
        
        try:
            # Update book_requests table
            cursor.execute("""
                UPDATE book_requests
                SET status = 'returned'
                WHERE user_id = ? AND book_id = ? AND status = 'accepted'
            """, (user_id, book_id))
            
            # Update books table
            cursor.execute("""
                UPDATE books
                SET available = 1
                WHERE id = ?
            """, (book_id,))
            
            conn.commit()
            messagebox.showinfo("Success", "Book returned successfully")
            
            # Refresh the table
            for item in tree.get_children():
                tree.delete(item)
            
            cursor.execute("""
                SELECT b.id, b.title, b.author, br.request_date,
                       date(br.request_date, '+14 days') as due_date
                FROM book_requests br
                JOIN books b ON br.book_id = b.id
                WHERE br.user_id = ? AND br.status = 'accepted'
            """, (user_id,))
            
            for row in cursor.fetchall():
                tree.insert("", "end", values=row)
            
            # Clear the entry fields
            entbookID.delete(0, tk.END)
            entbookName.delete(0, tk.END)
            entAuthor.delete(0, tk.END)
            entIssueDate.delete(0, tk.END)
            
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
    
    returnbutton = tk.Button(framereturnbooks, text="Return", bg='#008A44', fg=TEXTCOLOR, font=("Arial", 12, "bold"), width=20, command=return_book)
    returnbutton.grid(row=4, column=0, pady=40)
    
    framereturnbooks.grid(row=1, column=1, padx=(20,0), pady=(10,0), sticky="ns")
    
    return framereturnbooks

def yourprofile():
    frameyourprofile = tk.Frame(window, bg=FRAME_DASHBOARD_BG, width=1120)
    frameyourprofile.grid_propagate(0)

    # Photo placeholder
    photo_placeholder = tk.Frame(frameyourprofile, width=150, height=150, bg='grey')
    photo_placeholder.grid(row=0, column=0, padx=10, pady=(30,10))

    # Form fields
    framecredential = tk.Frame(frameyourprofile, bg=FRAME_DASHBOARD_BG, width=1100, height=300)
    framecredential.grid_propagate(0)
    framecredential.grid_columnconfigure(2, weight=1)

    firstnamelbl = tk.Label(framecredential, text="FirstName:", bg=FRAME_DASHBOARD_BG, font=("Arial",18), fg=TEXTCOLOR)
    firstnamelbl.grid(row=1, column=0, sticky='w', padx=(60,10), pady=(50,10))
    firstnameent = tk.Entry(framecredential, font=("Arial",18), bg=FRAME_MENUBAR_BG, fg=TEXTCOLOR)
    firstnameent.grid(row=1, column=1, sticky='we', padx=10, pady=(50,10))

    lastnamelbl = tk.Label(framecredential, text="LastName:", font=("Arial",18), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR)
    lastnamelbl.grid(row=2, column=0, sticky='w', padx=(60,10), pady=15)
    lastnameent = tk.Entry(framecredential, font=("Arial",18), bg=FRAME_MENUBAR_BG, fg=TEXTCOLOR)
    lastnameent.grid(row=2, column=1, sticky='we', padx=10, pady=15)

    contactlbl = tk.Label(framecredential, text="Contact:", font=("Arial",18), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR)
    contactlbl.grid(row=3, column=0, sticky='w', padx=(60,10), pady=15)
    contactent = tk.Entry(framecredential, font=("Arial",18), bg=FRAME_MENUBAR_BG, fg=TEXTCOLOR)
    contactent.grid(row=3, column=1, sticky='we', padx=10, pady=15)

    emaillbl = tk.Label(framecredential, text="Email:", font=("Arial",18), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR)
    emaillbl.grid(row=4, column=0, sticky='w', padx=(60,10), pady=15)
    emaillent = tk.Entry(framecredential, bg=FRAME_MENUBAR_BG, font=("Arial",18), fg=TEXTCOLOR)
    emaillent.grid(row=4, column=1, sticky='we', padx=10, pady=15)

    # Gender radio buttons
    genderlbl = tk.Label(framecredential, text="Gender:", font=("Arial",18), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR)
    genderlbl.grid(row=1, column=2, sticky='e', padx=(30,10), pady=15)
    gender_var = tk.StringVar()
    rdM = tk.Radiobutton(framecredential, text="Male", font=("Arial",18), variable=gender_var, value="male", bg=FRAME_DASHBOARD_BG, selectcolor=FRAME_DASHBOARD_BG, fg=TEXTCOLOR)
    rdM.grid(row=1, column=3, sticky='e', padx=10, pady=15)
    rdF = tk.Radiobutton(framecredential, text="Female", font=("Arial",18), variable=gender_var, value="female", bg=FRAME_DASHBOARD_BG, selectcolor=FRAME_DASHBOARD_BG, fg=TEXTCOLOR)
    rdF.grid(row=1, column=4, sticky='e', padx=10, pady=15)

    framecredential.grid(row=1, column=0, padx=10, pady=10)

    # Load user data
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user_data = cursor.fetchone()
    conn.close()

    if user_data:
        firstnameent.insert(0, user_data[4].split()[0] if user_data[4] else "")
        lastnameent.insert(0, user_data[4].split()[1] if user_data[4] and len(user_data[4].split()) > 1 else "")
        contactent.insert(0, user_data[5] if len(user_data) > 5 else "")
        emaillent.insert(0, user_data[3])
        gender_var.set(user_data[6] if len(user_data) > 6 else "")
        
        # Load profile picture if it exists
        if len(user_data) > 7 and user_data[7]:
            load_profile_picture(photo_placeholder, user_data[7])

    def save_profile():
        firstname = firstnameent.get()
        lastname = lastnameent.get()
        contact = contactent.get()
        email = emaillent.get()
        gender = gender_var.get()
        full_name = f"{firstname} {lastname}"

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE users 
                SET full_name = ?, email = ?, contact = ?, gender = ?
                WHERE id = ?
            """, (full_name, email, contact, gender, user_id))
            conn.commit()
            messagebox.showinfo("Success", "Profile updated successfully")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close()

    def upload_photo():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
        if file_path:
            try:
                # Create a directory to store profile pictures if it doesn't exist
                os.makedirs("profile_pictures", exist_ok=True)
                
                # Generate a unique filename
                _, ext = os.path.splitext(file_path)
                new_filename = f"user_{user_id}{ext}"
                new_path = os.path.join("profile_pictures", new_filename)
                
                # Copy the selected image to the profile_pictures directory
                shutil.copy(file_path, new_path)
                
                # Update the database with the new image path
                conn = sqlite3.connect('library.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET profile_picture = ? WHERE id = ?", (new_path, user_id))
                conn.commit()
                conn.close()
                
                # Display the new image
                load_profile_picture(photo_placeholder, new_path)
                messagebox.showinfo("Success", "Profile picture updated successfully")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def delete_account():
        if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete your account? This action cannot be undone."):
            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
                conn.commit()
                messagebox.showinfo("Success", "Your account has been deleted.")
                window.quit()  # Close the application
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                conn.close()

    # Buttons
    framebutncredential = tk.Frame(frameyourprofile, bg=FRAME_DASHBOARD_BG, width=1100, height=80)
    framebutncredential.grid_propagate(0)
    tk.Button(framebutncredential, text="Save", font=("Arial",18), bg=FRAME_TITLEBAR_BG, fg=TEXTCOLOR, command=save_profile).grid(row=0, column=0, pady=20, padx=(250,50), sticky='w')
    tk.Button(framebutncredential, text="Upload Photo", font=("Arial",18), bg=FRAME_TITLEBAR_BG, fg=TEXTCOLOR, command=upload_photo).grid(row=0, column=1, pady=20, padx=50)
    tk.Button(framebutncredential, text="Delete Account", font=("Arial",18), bg=FRAME_TITLEBAR_BG, fg=TEXTCOLOR, command=delete_account).grid(row=0, column=2, pady=20, padx=50, sticky='e')
    framebutncredential.grid(row=2, column=0, padx=10, pady=10, sticky="we")

    frameyourprofile.grid(row=1, column=1, padx=(20,0), pady=(10,0), sticky="ns")

    return frameyourprofile

def load_profile_picture(photo_placeholder, image_path):
    try:
        img = Image.open(image_path)
        img = img.resize((150, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        lbl = tk.Label(photo_placeholder, image=photo)
        lbl.image = photo
        lbl.pack(fill=tk.BOTH, expand=True)
    except Exception as e:
        print(f"Error loading profile picture: {e}") 
 

def switchframe(current_frame):
    # Clear any existing frame in the main content area
    for widget in window.winfo_children():
        if isinstance(widget, Frame) and widget.grid_info()['row'] == 1 and widget.grid_info()['column'] == 1:
            widget.destroy()
    # Create and display the new frame
    current_frame()


frame_titlebar =Frame(window,bg=FRAME_TITLEBAR_BG)
frame_titlebar.columnconfigure(0,weight=0)
frame_titlebar.columnconfigure(1,weight=1)
lib_menu_button=Button(frame_titlebar,image=menubutton_icon,bg=FRAME_TITLEBAR_BG,borderwidth=0,activebackground=FRAME_TITLEBAR_BG,command=extend_menubar)
lib_name = Label(frame_titlebar,text="Library Hub",font=("Arial",35,"bold"),fg=TEXTCOLOR,bg=FRAME_TITLEBAR_BG,anchor="w")
#placingwidgets
lib_menu_button.grid(row= 0,column=0,padx=10,pady=10)
lib_name.grid(row=0,column=1,padx=(35,0),sticky="w")


frame_menubar=Frame(window,bg=FRAME_MENUBAR_BG)
lib_dash_label = Label(frame_menubar,bg=SWITCH_COLOR,height=4,width=10)
lib_dash_button =Button(frame_menubar,image=dashboard_icon,text="",font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=SWITCH_COLOR,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:[update_label_color_on_tap("1"),switchframe(dashboardframe)])
lib_requestbook_label = Label(frame_menubar,bg=FRAME_MENUBAR_BG,height=4,width=10)
lib_request_book_button =Button(frame_menubar,image=request_books_icon,font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:[update_label_color_on_tap("2"),switchframe(makerequestframe)])
lib_returnbook_label = Label(frame_menubar,bg=FRAME_MENUBAR_BG,height=4,width=10)
lib_return_book_button =Button(frame_menubar,image=return_books_icon,font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:[update_label_color_on_tap("3"),switchframe(returnbooksframe)])
# lib_log_label = Label(frame_menubar,bg=FRAME_MENUBAR_BG,height=4,width=10)
# lib_log_button =Button(frame_menubar,image=books_log_icon,font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:update_label_color_on_tap("4"))
lib_profile_label = Label(frame_menubar,bg=FRAME_MENUBAR_BG,height=4,width=10)
lib_profile_button =Button(frame_menubar,image=profile_icon,font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:[update_label_color_on_tap("4"),switchframe(yourprofile)])
lib_logout_button =Button(frame_menubar,image=logout_icon,bg=FRAME_MENUBAR_BG,font=("Arial",15,"bold"),compound=LEFT,fg="#FF4500",borderwidth=0,activebackground=FRAME_MENUBAR_BG,command=logout)

#placing inside menuframe
lib_dash_label.grid(row=0,column=0,padx=13,pady=(30,35))
lib_dash_button.grid(row=0,column=0,padx=13,pady=(30,35))
lib_requestbook_label.grid(row=1,column=0,padx=13,pady=(0,35))
lib_request_book_button.grid(row=1,column=0,padx=13,pady=(0,35))
lib_returnbook_label.grid(row=2,column=0,padx=13,pady=(0,35))
lib_return_book_button.grid(row=2,column=0,padx=13,pady=(0,35))
# lib_log_label.grid(row=3,column=0,padx=13,pady=(0,35))
# lib_log_button.grid(row=3,column=0,padx=13,pady=(0,35))
lib_profile_label.grid(row=3,column=0,padx=13,pady=(0,35))
lib_profile_button.grid(row=3,column=0,padx=13,pady=(0,35))
lib_logout_button.grid(row=4,column=0,padx=13,pady=(30))


#placing frames
frame_titlebar.grid(row=0, column=0,columnspan=2,sticky="we")
frame_menubar.grid(row=1,column=0,sticky="wsn")

if __name__ == "__main__":
    dashboardframe()

window.mainloop()

