from tkinter import *

def create_view_requests_frame(root):
    view_requests_frame = Frame(root)
    view_requests_frame.pack()

    Label(view_requests_frame, text="View Book Requests").pack()
    Label(view_requests_frame, text="This section will display pending book requests.").pack()

    return view_requests_frame
