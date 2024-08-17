from tkinter import *
from PIL import *
from .dashboard_frame import create_dashboard_frame
from .view_requests_frame import create_view_requests_frame
from .manage_books_frame import create_manage_books_frame
from .view_users_frame import create_view_users_frame
from .your_profile_frame import create_your_profile_frame

def admin_page():
    root = Tk()
    root.title("Library Management System - Admin Page")
    root.geometry("900x700+300+50")
    root.resizable(False, False)
    root.configure(bg="#f0f0f0")

    # Frames
    dashboard_frame = create_dashboard_frame(root)
    view_requests_frame = create_view_requests_frame(root)
    manage_books_frame = create_manage_books_frame(root)
    view_users_frame = create_view_users_frame(root)
    your_profile_frame = create_your_profile_frame(root)

    # ... (rest of the code remains the same)
