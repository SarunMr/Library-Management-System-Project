from tkinter import *

def create_view_users_frame(root):
    view_users_frame = Frame(root)
    view_users_frame.pack()

    Label(view_users_frame, text="View Users").pack()
    Label(view_users_frame, text="This section will display a list of registered users.").pack()

    return view_users_frame
