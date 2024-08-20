from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import sqlite3
import shutil
import os
import subprocess
import sys

my_user_id = int(sys.argv[1])



#theme color.
TEXTCOLOR ="#FFFFFF"
FRAME_TITLEBAR_BG ="#008A44"
FRAME_MENUBAR_BG = "#262626"
SWITCH_COLOR = "#5F5F5F"
FRAME_DASHBOARD_BG = '#343233'


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

window = Tk()
window.configure(bg=FRAME_DASHBOARD_BG,)
#icons
menubutton_icon = PhotoImage(file="icons_lib/menu_button.png")
menubuttontoggle_icon = PhotoImage(file="icons_lib/cross.png")
dashboard_icon = PhotoImage(file="icons_lib/dash_icon.png")
request_books_icon = PhotoImage(file="icons_lib/request_books_icon.png")
return_books_icon = PhotoImage(file="icons_lib/return_ic.png")
view_users_icon = PhotoImage(file="icons_lib/log_icon.png")
profile_icon =PhotoImage(file="icons_lib/profile.png")
logout_icon = PhotoImage(file="icons_lib/logout_icon.png")

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


#books
b1=PhotoImage(file="books/b1.png")

window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1,weight=1)
window.grid_rowconfigure(1,weight=1)

def update_label_color_on_tap(n):
    label_dict = {"1":lib_dash_label,"2":lib_requestbook_label,"3":lib_returnbook_label,"4":lib_view_users_label,"5":lib_profile_label}
    btn_dict = {"1":lib_dash_button,"2":lib_request_book_button,"3":lib_return_book_button,"4":lib_view_users_button,"5":lib_profile_button}
    for label in label_dict.keys():
        if label == n:
            label_dict[label].config(bg=SWITCH_COLOR)
            btn_dict[label].config(bg=SWITCH_COLOR)
        else:
            label_dict[label].config(bg=FRAME_MENUBAR_BG)
            btn_dict[label].config(bg=FRAME_MENUBAR_BG)



def default_menubar():
    labellst = [lib_dash_label,lib_requestbook_label,lib_returnbook_label,lib_view_users_label,lib_profile_label]
    for label in labellst:
        label.config(width=10)
    
    lib_menu_button.config(image=menubutton_icon)
    lib_dash_button.config(text="",width=45,)
    lib_request_book_button.config(text="",width=45)
    lib_return_book_button.config(text="",width=45)
    lib_view_users_button.config(text="",width=45)
    lib_profile_button.config(text="",width=45)
    lib_menu_button.config(command=extend_menubar)


def extend_menubar():
    labellst = [lib_dash_label,lib_requestbook_label,lib_returnbook_label,lib_view_users_label,lib_profile_label]
    for label in labellst:
        label.config(width=40)

    lib_menu_button.config(image=menubuttontoggle_icon,padx=13,pady=30)
    lib_dash_button.config(text="Dashboard",width=200,padx=20,anchor="w")
    lib_request_book_button.config(text="View Request",width=200,padx=20,anchor="w")
    lib_return_book_button.config(text="Manage Books",width=200,padx=20,anchor="w")
    lib_view_users_button.config(text="View Users",width=200,padx=20,anchor="w")
    lib_profile_button.config(text="Your Profile",width=200,padx=20,anchor="w")
    lib_logout_button.config(text="Log out")
    lib_menu_button.config(command=default_menubar)

def dashboardframe():
    frame_dashboard = Frame(window, bg=FRAME_DASHBOARD_BG, width=1120)
    frame_dashboard.grid_propagate(0)
    welcome_label = Label(frame_dashboard, text="WELCOME AdminName", font=("Arial", 30, "bold"), fg=FRAME_TITLEBAR_BG, bg=FRAME_DASHBOARD_BG, anchor="w", width=45)
    welcome_label.grid(row=0, column=0, padx=15, pady=(10,0), sticky="wn")

    frametracker = Frame(frame_dashboard, bg=FRAME_DASHBOARD_BG)
    frametracker.grid_columnconfigure(0, weight=1)
    frametracker.grid_columnconfigure(1, weight=1)
    frametracker.grid_columnconfigure(2, weight=1)

    # Connect to the database
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Total Books
    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]

    frametotalbooks = Frame(frametracker, bg=FRAME_MENUBAR_BG)
    frametotalbooks.grid(row=0, column=0, padx=(15,20), sticky="w")
    labeltotalbooks = Label(frametotalbooks, text="Total Books", font=("ArialBold", 16), fg=TEXTCOLOR, bg=FRAME_MENUBAR_BG, width=16)
    labelbooksquantity = Label(frametotalbooks, text=str(total_books), font=("ArialBold", 16), fg=TEXTCOLOR, bg=FRAME_MENUBAR_BG)
    labeltotalbooks.grid(row=0, column=0, padx=20, pady=(10,5))
    labelbooksquantity.grid(row=1, column=0, pady=5)

    # Total Book Requests from Users
    cursor.execute("SELECT COUNT(*) FROM book_requests WHERE status='pending'")
    total_requests = cursor.fetchone()[0]

    frametotalrequests = Frame(frametracker, bg=FRAME_MENUBAR_BG)
    frametotalrequests.grid(row=0, column=1, padx=80)
    labeltotalrequests = Label(frametotalrequests, text="Total Book Request", font=("ArialBold", 16), fg=TEXTCOLOR, bg=FRAME_MENUBAR_BG, width=16)
    labelrequestquantity = Label(frametotalrequests, text=str(total_requests), font=("ArialBold", 16), fg=TEXTCOLOR, bg=FRAME_MENUBAR_BG)
    labeltotalrequests.grid(row=0, column=0, padx=20, pady=(10,5))
    labelrequestquantity.grid(row=1, column=0, pady=5)

    # Total Requests Till Now
    cursor.execute("SELECT COUNT(*) FROM book_requests")
    total_all_requests = cursor.fetchone()[0]

    frametotalfines = Frame(frametracker, bg=FRAME_MENUBAR_BG)
    frametotalfines.grid(row=0, column=2, padx=(20,15), sticky="e")
    labeltotalfines = Label(frametotalfines, text="Total Requests", font=("ArialBold", 16), fg=TEXTCOLOR, bg=FRAME_MENUBAR_BG, width=16)
    labelfinesquantity = Label(frametotalfines, text=str(total_all_requests), font=("ArialBold", 16), fg=TEXTCOLOR, bg=FRAME_MENUBAR_BG)
    labeltotalfines.grid(row=0, column=0, padx=20, pady=(10,5))
    labelfinesquantity.grid(row=1, column=0, pady=5)

    quickreqlabel = Label(frame_dashboard, text="All Books", font=("ArialBold", 14), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)

    framequickrequesttable = Frame(frame_dashboard, bg=FRAME_MENUBAR_BG, height=240)
    framequickrequesttable.grid_columnconfigure(0, weight=0)
    framequickrequesttable.grid_columnconfigure(1, weight=1)
    framequickrequesttable.grid_columnconfigure(2, weight=1)
    framequickrequesttable.grid_columnconfigure(3, weight=0)
    framequickrequesttable.grid_columnconfigure(4, weight=0)
    framequickrequesttable.grid_propagate(0)

    # Create a Treeview widget for All Books
    all_books_tree = ttk.Treeview(framequickrequesttable, columns=("Book ID", "Book Name", "Author", "Available"), show="headings", height=10)
    all_books_tree.heading("Book ID", text="Book ID")
    all_books_tree.heading("Book Name", text="Book Name")
    all_books_tree.heading("Author", text="Author")
    all_books_tree.heading("Available", text="Available")

    all_books_tree.column("Book ID", width=100)
    all_books_tree.column("Book Name", width=200)
    all_books_tree.column("Author", width=200)
    all_books_tree.column("Available", width=100)

    all_books_tree.grid(row=0, column=0, columnspan=5, sticky="nsew")

    # Fetch and display all books
    cursor.execute("SELECT id, title, author, available FROM books ORDER BY id DESC")
    for row in cursor.fetchall():
        all_books_tree.insert("", "end", values=row)

    latestbooklabel = Label(frame_dashboard, text="Latest Book Added", font=("ArialBold", 14), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    framelatestbooks = Frame(frame_dashboard, bg=FRAME_DASHBOARD_BG, height=230, width=900)
    framelatestbooks.grid_columnconfigure(0, weight=1)
    framelatestbooks.grid_columnconfigure(1, weight=1)
    framelatestbooks.grid_columnconfigure(2, weight=1)
    framelatestbooks.grid_columnconfigure(3, weight=1)
    framelatestbooks.grid_propagate(0)

    # Fetch and display latest added book
    cursor.execute("SELECT title, author, image_path FROM books ORDER BY id DESC LIMIT 1")
    latest_book = cursor.fetchone()

    if latest_book:
        title, author, image_path = latest_book
        if image_path and os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((150, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
        else:
            # Use a default image if no image is available or the file doesn't exist
            default_image_path = "path/to/your/default/image.png"  # Replace with your default image path
            if os.path.exists(default_image_path):
                img = Image.open(default_image_path)
                img = img.resize((150, 200), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
            else:
                # If even the default image is not found, create a blank image
                photo = ImageTk.PhotoImage(Image.new('RGB', (150, 200), color='gray'))

        buttonb1 = tk.Button(framelatestbooks, image=photo, bg=FRAME_DASHBOARD_BG, borderwidth=0, activebackground=FRAME_DASHBOARD_BG)
        buttonb1.image = photo  # Keep a reference to avoid garbage collection
        buttonb1.grid(row=0, column=0, padx=(20,0), sticky="w")

    frametracker.grid(row=1, column=0, padx=10, pady=2, sticky="wne")
    quickreqlabel.grid(row=2, column=0, padx=25, pady=(4,3), sticky="w")
    framequickrequesttable.grid(row=3, column=0, padx=(25,25), pady=2, sticky="wne")
    latestbooklabel.grid(row=4, column=0, padx=25, pady=(4,3), sticky="w")
    framelatestbooks.grid(row=5, column=0, padx=(25,25), pady=2, sticky="wnes")

    frame_dashboard.grid(row=1, column=1, padx=(20,0), pady=(10,0), sticky="ns")

    # Close the database connection
    conn.close()

def viewrequestframe():
    frameviewrequest = tk.Frame(window, bg=FRAME_DASHBOARD_BG, width=1120)
    frameviewrequest.grid_propagate(0)
    
    framepagetitle = tk.Frame(frameviewrequest, bg=FRAME_DASHBOARD_BG, width=1100, height=40)
    framepagetitle.grid_propagate(0)
    framepagetitle.grid_columnconfigure(0, weight=1)
    framepagetitle.grid_columnconfigure(1, weight=0)
    framepagetitle.grid_columnconfigure(2, weight=0)
    
    libtopbooks = tk.Label(framepagetitle, text="Request From Users", font=("ArialBold", 16, "bold"), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR, anchor="w")
    libtopbooks.grid(row=0, column=0, padx=(20,0), pady=5, sticky="wne")
    framepagetitle.grid(row=0, column=0, padx=10, pady=10, sticky="ne")
    
    frametoppicks = tk.Frame(frameviewrequest, bg=FRAME_MENUBAR_BG, height=250)
    frametoppicks.grid_columnconfigure(0, weight=1)
    frametoppicks.grid_propagate(0)
    frametoppicks.grid(row=1, column=0, padx=25, pady=2, sticky="wne")
    
    # Create Treeview
    columns = ("Request ID", "User ID", "Username", "Book ID", "Book Title", "Request Date", "Status")
    tree = ttk.Treeview(frametoppicks, columns=columns, show='headings', height=10)
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    tree.grid(row=0, column=0, sticky='nsew')
    
    # Add a scrollbar
    scrollbar = ttk.Scrollbar(frametoppicks, orient=tk.VERTICAL, command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    tree.configure(yscroll=scrollbar.set)
    
    # Fetch and display requests
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT br.id, br.user_id, u.username, br.book_id, b.title, br.request_date, br.status
        FROM book_requests br
        JOIN users u ON br.user_id = u.id
        JOIN books b ON br.book_id = b.id
        WHERE br.status = 'pending'
    ''')
    for row in cursor.fetchall():
        tree.insert('', 'end', values=row)
    
    lblrqstbooks = tk.Label(frameviewrequest, text="Request Approval", font=("ArialBold", 16, "bold"), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR)
    lblrqstbooks.grid(row=2, column=0, padx=25, pady=15, sticky='w')
    
    frame_request_label = tk.Frame(frameviewrequest, bg=FRAME_DASHBOARD_BG)
    frame_request_label.grid_columnconfigure(0, weight=0)
    frame_request_label.grid_columnconfigure(1, weight=0)
    frame_request_label.grid_columnconfigure(2, weight=0)
    frame_request_label.grid_columnconfigure(3, weight=0)
    
    lblbookID = tk.Label(frame_request_label, text="Account ID:", font=("Arial", 12, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblbookID.grid(row=0, column=0, padx=(80,20), pady=(25,15), sticky="e")
    entbookID = tk.Entry(frame_request_label, font=("Arial", 14))
    entbookID.grid(row=0, column=1, pady=5)
    
    lblaccountid = tk.Label(frame_request_label, text="Username", font=("Arial", 12, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblaccountid.grid(row=0, column=2, padx=(140,20), pady=(25,15))
    entaccountId = tk.Entry(frame_request_label, font=("Arial", 14))
    entaccountId.grid(row=0, column=3, padx=(0,10), pady=5, sticky="e")
    
    # Double-click event
    def on_tree_double_click(event):
        selected_item = tree.selection()[0]
        values = tree.item(selected_item)['values']
        entbookID.delete(0, tk.END)
        entbookID.insert(0, values[1])  # User ID
        entaccountId.delete(0, tk.END)
        entaccountId.insert(0, values[2])  # Username
    
    tree.bind("<Double-1>", on_tree_double_click)
    
    # Accept request function
    def accept_request():
        selected_item = tree.selection()[0]
        request_id = tree.item(selected_item)['values'][0]
        
        cursor.execute("UPDATE book_requests SET status = 'accepted' WHERE id = ?", (request_id,))
        conn.commit()
        
        messagebox.showinfo("Success", "Request accepted successfully!")
        refresh_tree()
    
    # Decline request function
    def decline_request():
        selected_item = tree.selection()[0]
        request_id = tree.item(selected_item)['values'][0]
        
        cursor.execute("UPDATE book_requests SET status = 'declined' WHERE id = ?", (request_id,))
        conn.commit()
        
        messagebox.showinfo("Success", "Request declined successfully!")
        refresh_tree()
    
    # Refresh tree function
    def refresh_tree():
        for item in tree.get_children():
            tree.delete(item)
        
        cursor.execute('''
            SELECT br.id, br.user_id, u.username, br.book_id, b.title, br.request_date, br.status
            FROM book_requests br
            JOIN users u ON br.user_id = u.id
            JOIN books b ON br.book_id = b.id
            WHERE br.status = 'pending'
        ''')
        for row in cursor.fetchall():
            tree.insert('', 'end', values=row)
    
    acceptrequestbuttton = tk.Button(frameviewrequest, text="Accept", bg='#008A44', fg=TEXTCOLOR, font=("Arial", 12, "bold"), command=accept_request)
    acceptrequestbuttton.grid(row=4, column=0, pady=30)
    
    declinerequestbutton = tk.Button(frameviewrequest, text="Decline", bg='#FF4500', fg=TEXTCOLOR, font=("Arial", 12, "bold"), command=decline_request)
    declinerequestbutton.grid(row=5, column=0, pady=0)
    
    frame_request_label.grid(row=3, column=0, padx=25, pady=(15,5), sticky="we")
    frameviewrequest.grid(row=1, column=1, padx=(20,0), pady=(10,0), sticky="ns")

    # Clean up
    def on_closing():
        conn.close()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)

def managebooksframe():
    framemanagebooks = tk.Frame(window, bg=FRAME_DASHBOARD_BG, width=1120)
    framemanagebooks.grid_propagate(0)
    
    lblYourbooks = tk.Label(framemanagebooks, text="Manage Books", font=("Arial", 18, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblYourbooks.grid(row=0, column=0, padx=20, pady=20, sticky='w')
    
    framereturndetails = tk.Frame(framemanagebooks, background=FRAME_DASHBOARD_BG)
    
    lblBookID = tk.Label(framereturndetails, text="Book ID:", font=("Arial", 18, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblBookID.grid(row=0, column=0, padx=(80,20), pady=(25,15), sticky="w")
    entbookID = tk.Entry(framereturndetails, font=("Arial", 18), width=30)
    entbookID.grid(row=0, column=1, pady=5)
    
    lblbookName = tk.Label(framereturndetails, text="Book Name:", font=("Arial", 18, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblbookName.grid(row=1, column=0, padx=(80,20), pady=(25,15), sticky='w')
    entbookName = tk.Entry(framereturndetails, font=("Arial", 18), width=30)
    entbookName.grid(row=1, column=1, padx=(0,10), pady=5, sticky="e")
    
    lblAuthor = tk.Label(framereturndetails, text="Author:", font=("Arial", 18, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblAuthor.grid(row=2, column=0, padx=(80,20), pady=(25,15), sticky="w")
    entAuthor = tk.Entry(framereturndetails, font=("Arial", 18), width=30)
    entAuthor.grid(row=2, column=1, pady=5)
    
    lblgenre = tk.Label(framereturndetails, text="Genre:", font=("Arial", 18, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblgenre.grid(row=3, column=0, padx=(80,20), pady=(25,15), sticky="w")
    entgenre = tk.Entry(framereturndetails, font=("Arial", 18), width=30)
    entgenre.grid(row=3, column=1, padx=(0,10), pady=5, sticky="e")
    
    lblissueamount = tk.Label(framereturndetails, text="Issue Amount:", font=("Arial", 18, "bold"), fg=TEXTCOLOR, bg=FRAME_DASHBOARD_BG)
    lblissueamount.grid(row=4, column=0, padx=(80,20), pady=(25,15), sticky="w")
    entissueamount = tk.Entry(framereturndetails, font=("Arial", 18), width=30)
    entissueamount.grid(row=4, column=1, padx=(0,10), pady=5, sticky="e")
    
    framereturndetails.grid(row=1, column=0, padx=(20,0), pady=(10,0), sticky="ns")
    
    # Photo placeholder
    frame_photo = tk.Frame(framemanagebooks, background="white", width=150, height=150)
    frame_photo.grid(row=1, column=1, padx=(50, 20), pady=(0, 20), sticky='ne')
    frame_photo.grid_propagate(0)
    
    # Image handling
    selected_image_path = tk.StringVar()
    
    
    def add_book():
        book_name = entbookName.get()
        author = entAuthor.get()
        genre = entgenre.get()
        issue_amount = entissueamount.get()
        image_path = selected_image_path.get()
        
        if not all([book_name, author, genre, issue_amount]):
            messagebox.showerror("Error", "All fields are required")
            return
        
        try:
            issue_amount = float(issue_amount)
        except ValueError:
            messagebox.showerror("Error", "Issue Amount must be a number")
            return
        
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        
        try:
            if image_path:
                # Copy image to a folder in your project
                new_image_path = os.path.join("book_images", os.path.basename(image_path))
                os.makedirs("book_images", exist_ok=True)
                shutil.copy(image_path, new_image_path)
            else:
                new_image_path = ""
            
            cursor.execute('''
                INSERT INTO books (title, author, genre, available, image_path, added_date)
                VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (book_name, author, genre, 1, new_image_path))
            
            conn.commit()
            messagebox.showinfo("Success", "Book added successfully")
            clear_fields()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            conn.close()
    
    def remove_book():
        book_id = entbookID.get()
        
        if not book_id:
            messagebox.showerror("Error", "Please enter a Book ID")
            return
        
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT image_path FROM books WHERE id = ?", (book_id,))
            result = cursor.fetchone()
            
            if result:
                image_path = result[0]
                cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
                conn.commit()
                
                if image_path and os.path.exists(image_path):
                    os.remove(image_path)
                
                messagebox.showinfo("Success", "Book removed successfully")
                clear_fields()
            else:
                messagebox.showerror("Error", "Book not found")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            conn.close()
    
    def clear_fields():
        entbookID.delete(0, tk.END)
        entbookName.delete(0, tk.END)
        entAuthor.delete(0, tk.END)
        entgenre.delete(0, tk.END)
        entissueamount.delete(0, tk.END)
        selected_image_path.set("")
        for widget in frame_photo.winfo_children():
            widget.destroy()
    
    Addbookbutton = tk.Button(framemanagebooks, text="Add book", bg='#008A44', fg=TEXTCOLOR, font=("Arial", 14, "bold"), width=20, command=add_book)
    Addbookbutton.grid(row=6, column=0, pady=140)
    
    Removebookbutton = tk.Button(framemanagebooks, text="Remove", bg='#FF4500', fg=TEXTCOLOR, font=("Arial", 14, "bold"), width=20, command=remove_book)
    Removebookbutton.grid(row=6, column=1, pady=140)
    
    framemanagebooks.grid(row=1, column=1, padx=(20,0), pady=(10,0), sticky="ns")


def viewuserframe():
    frameviewuser = tk.Frame(window, bg=FRAME_DASHBOARD_BG, width=1120)
    frameviewuser.grid_propagate(0)

    # All User section
    lbl_all_user = tk.Label(frameviewuser, text="All Users", font=("Arial", 16, "bold"), fg="white", bg=FRAME_DASHBOARD_BG)
    lbl_all_user.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    # User list area
    user_list_frame = tk.Frame(frameviewuser, bg=FRAME_MENUBAR_BG, width=1100, height=300)
    user_list_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 20), sticky="nsew")
    user_list_frame.grid_propagate(0)

    # Create Treeview
    columns = ("User ID", "Username", "Email", "Full Name", "Fine Amount")
    tree = ttk.Treeview(user_list_frame, columns=columns, show='headings', height=10)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=200)

    tree.grid(row=0, column=0, sticky='nsew')

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(user_list_frame, orient=tk.VERTICAL, command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    tree.configure(yscroll=scrollbar.set)

    # Fetch and display users
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, full_name, fine_amount FROM users")
    for row in cursor.fetchall():
        tree.insert('', 'end', values=row)

    frameuserdetails = tk.Frame(frameviewuser, bg=FRAME_DASHBOARD_BG)

    # User details section
    lbl_userid = tk.Label(frameuserdetails, text="UserID :", font=("Arial", 15), fg="white", bg=FRAME_DASHBOARD_BG)
    lbl_userid.grid(row=0, column=0, sticky="w", padx=(50, 5), pady=5)
    entry_userid = tk.Entry(frameuserdetails, font=("Arial", 15), width=20)
    entry_userid.grid(row=0, column=1, sticky="w", padx=(80, 10), pady=5)

    lbl_username = tk.Label(frameuserdetails, text="Username :", font=("Arial", 15), fg="white", bg=FRAME_DASHBOARD_BG)
    lbl_username.grid(row=0, column=2, sticky="w", padx=(140, 10), pady=10)
    entry_username = tk.Entry(frameuserdetails, font=("Arial", 15), width=20)
    entry_username.grid(row=0, column=3, sticky="w", padx=(60, 10), pady=5)

    lbl_fine_amount = tk.Label(frameuserdetails, text="Fine Amount :", font=("Arial", 15), fg="white", bg=FRAME_DASHBOARD_BG)
    lbl_fine_amount.grid(row=1, column=0, sticky="w", padx=(10, 5), pady=5)
    entry_fine_amount = tk.Entry(frameuserdetails, font=("Arial", 15), width=20)
    entry_fine_amount.grid(row=1, column=1, sticky="w", padx=(80, 10), pady=5)

    frameuserdetails.grid(row=3, column=0)

    # Double-click event
    def on_tree_double_click(event):
        selected_item = tree.selection()[0]
        values = tree.item(selected_item)['values']
        entry_userid.delete(0, tk.END)
        entry_userid.insert(0, values[0])
        entry_username.delete(0, tk.END)
        entry_username.insert(0, values[1])
        entry_fine_amount.delete(0, tk.END)
        entry_fine_amount.insert(0, values[4])

    tree.bind("<Double-1>", on_tree_double_click)

    # Send Fine function
    def send_fine():
        user_id = entry_userid.get()
        fine_amount = entry_fine_amount.get()

        if not user_id or not fine_amount:
            messagebox.showerror("Error", "Please select a user and enter a fine amount")
            return

        try:
            fine_amount = float(fine_amount)
        except ValueError:
            messagebox.showerror("Error", "Fine amount must be a number")
            return

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        try:
            cursor.execute("UPDATE users SET fine_amount = fine_amount + ? WHERE id = ?", (fine_amount, user_id))
            conn.commit()
            messagebox.showinfo("Success", f"Fine of ${fine_amount:.2f} sent successfully to user {user_id}")

            # Refresh the Treeview
            for item in tree.get_children():
                tree.delete(item)
            cursor.execute("SELECT id, username, email, full_name, fine_amount FROM users")
            for row in cursor.fetchall():
                tree.insert('', 'end', values=row)

            # Clear entry fields
            entry_userid.delete(0, tk.END)
            entry_username.delete(0, tk.END)
            entry_fine_amount.delete(0, tk.END)

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            conn.close()

    # Send Fine button
    btn_send_fine = tk.Button(frameviewuser, text="Send Fine", font=("Arial", 12, "bold"), bg="#008A44", fg="white", width=15, command=send_fine)
    btn_send_fine.grid(row=4, column=0, padx=10, pady=80)

    frameviewuser.grid(row=1, column=1, padx=(20, 0), pady=(10, 0), sticky="ns")

    # Clean up
    def on_closing():
        conn.close()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)

def yourprofile():
    frameyourprofile = tk.Frame(window, bg=FRAME_DASHBOARD_BG, width=1120)
    frameyourprofile.grid_propagate(0)

    # Form fields
    framecredential = tk.Frame(frameyourprofile, bg=FRAME_DASHBOARD_BG, width=1100, height=300)
    framecredential.grid_propagate(0)
    framecredential.grid_columnconfigure(2, weight=1)

    firstnamelbl = tk.Label(framecredential, text="FirstName:", bg=FRAME_DASHBOARD_BG, font=("Arial", 18), fg=TEXTCOLOR)
    firstnamelbl.grid(row=1, column=0, sticky='w', padx=(60,10), pady=(50,10))
    firstnameent = tk.Entry(framecredential, font=("Arial", 18), bg=FRAME_MENUBAR_BG, fg=TEXTCOLOR)
    firstnameent.grid(row=1, column=1, sticky='we', padx=10, pady=(50,10))

    lastnamelbl = tk.Label(framecredential, text="LastName:", font=("Arial", 18), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR)
    lastnamelbl.grid(row=2, column=0, sticky='w', padx=(60,10), pady=15)
    lastnameent = tk.Entry(framecredential, font=("Arial", 18), bg=FRAME_MENUBAR_BG, fg=TEXTCOLOR)
    lastnameent.grid(row=2, column=1, sticky='we', padx=10, pady=15)

    emaillbl = tk.Label(framecredential, text="Email:", font=("Arial", 18), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR)
    emaillbl.grid(row=4, column=0, sticky='w', padx=(60,10), pady=15)
    emaillent = tk.Entry(framecredential, bg=FRAME_MENUBAR_BG, font=("Arial", 18), fg=TEXTCOLOR)
    emaillent.grid(row=4, column=1, sticky='we', padx=10, pady=15)

    framecredential.grid(row=1, column=0, padx=10, pady=10)

    # Load admin data
    def load_admin_data():
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        
        # First, let's get the column names
        cursor.execute("PRAGMA table_info(users)")
        columns = [column[1] for column in cursor.fetchall()]
        
        # Now, let's fetch the admin data
        cursor.execute("SELECT * FROM users WHERE id = ?", (my_user_id,))
        admin_data = cursor.fetchone()
        conn.close()

        if admin_data:
            # Create a dictionary of the admin data
            admin_dict = dict(zip(columns, admin_data))
            
            # Now we can safely access the data, providing defaults if not present
            full_name = admin_dict.get('full_name', '').split()
            firstnameent.delete(0, tk.END)
            firstnameent.insert(0, full_name[0] if full_name else "")
            
            lastnameent.delete(0, tk.END)
            lastnameent.insert(0, full_name[1] if len(full_name) > 1 else "")
            
            emaillent.delete(0, tk.END)
            emaillent.insert(0, admin_dict.get('email', ''))
            
            
    load_admin_data()


    def save_profile():
        firstname = firstnameent.get()
        lastname = lastnameent.get()
        email = emaillent.get()
        full_name = f"{firstname} {lastname}"

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE users 
                SET full_name = ?, email = ?
                WHERE id = ?
            """, (full_name, email, my_user_id))
            conn.commit()
            messagebox.showinfo("Success", "Profile updated successfully")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close()

    def delete_profile():
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete your profile? This action cannot be undone."):
            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM users WHERE id = 1")
                conn.commit()
                messagebox.showinfo("Success", "Profile deleted successfully")
                window.quit()  # Close the application after deleting the profile
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", str(e))
            finally:
                conn.close()

    # Buttons
    framebutncredential = tk.Frame(frameyourprofile, bg=FRAME_DASHBOARD_BG, width=1100, height=80)
    framebutncredential.grid_propagate(0)
    tk.Button(framebutncredential, text="Save", font=("Arial", 18), bg=FRAME_TITLEBAR_BG, fg=TEXTCOLOR, command=save_profile).grid(row=0, column=0, pady=20, padx=(250,50), sticky='w')
    tk.Button(framebutncredential, text="Delete", font=("Arial", 18), bg=FRAME_TITLEBAR_BG, fg=TEXTCOLOR, command=delete_profile).grid(row=0, column=2, pady=20, padx=50, sticky='e')
    framebutncredential.grid(row=2, column=0, padx=10, pady=10, sticky="we")

    frameyourprofile.grid(row=1, column=1, padx=(20,0), pady=(10,0), sticky="ns") 
 

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
lib_request_book_button =Button(frame_menubar,image=request_books_icon,font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:[update_label_color_on_tap("2"),switchframe(viewrequestframe)])
lib_returnbook_label = Label(frame_menubar,bg=FRAME_MENUBAR_BG,height=4,width=10)
lib_return_book_button =Button(frame_menubar,image=return_books_icon,font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:[update_label_color_on_tap("3"),switchframe(managebooksframe)])
lib_view_users_label = Label(frame_menubar,bg=FRAME_MENUBAR_BG,height=4,width=10)
lib_view_users_button =Button(frame_menubar,image=view_users_icon,font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:{update_label_color_on_tap("4"),switchframe(viewuserframe)})
lib_profile_label = Label(frame_menubar,bg=FRAME_MENUBAR_BG,height=4,width=10)
lib_profile_button =Button(frame_menubar,image=profile_icon,font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:[update_label_color_on_tap("5"),switchframe(yourprofile)])
lib_logout_button =Button(frame_menubar,image=logout_icon,bg=FRAME_MENUBAR_BG,font=("Arial",15,"bold"),compound=LEFT,fg="#FF4500",borderwidth=0,activebackground=FRAME_MENUBAR_BG,command=logout)

#placing inside menuframe
lib_dash_label.grid(row=0,column=0,padx=13,pady=(30,35))
lib_dash_button.grid(row=0,column=0,padx=13,pady=(30,35))
lib_requestbook_label.grid(row=1,column=0,padx=13,pady=(0,35))
lib_request_book_button.grid(row=1,column=0,padx=13,pady=(0,35))
lib_returnbook_label.grid(row=2,column=0,padx=13,pady=(0,35))
lib_return_book_button.grid(row=2,column=0,padx=13,pady=(0,35))
lib_view_users_label.grid(row=3,column=0,padx=13,pady=(0,35))
lib_view_users_button.grid(row=3,column=0,padx=13,pady=(0,35))
lib_profile_label.grid(row=4,column=0,padx=13,pady=(0,35))
lib_profile_button.grid(row=4,column=0,padx=13,pady=(0,35))
lib_logout_button.grid(row=5,column=0,padx=13,pady=(30))


#placing frames
frame_titlebar.grid(row=0, column=0,columnspan=2,sticky="we")
frame_menubar.grid(row=1,column=0,sticky="wsn")

if __name__ == "__main__":
    dashboardframe() 

window.mainloop()
