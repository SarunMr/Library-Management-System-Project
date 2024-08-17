from tkinter import *

def create_manage_books_frame(root):
    manage_books_frame = Frame(root)
    manage_books_frame.pack()

    Label(manage_books_frame, text="Manage Books").pack()
    Label(manage_books_frame, text="Add, update, or delete books from the library catalog.").pack()

    return manage_books_frame
