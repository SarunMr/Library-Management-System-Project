from tkinter import *

def create_dashboard_frame(root):
    dashboard_frame = Frame(root)
    dashboard_frame.pack()

    Label(dashboard_frame, text="Welcome to the Dashboard!").pack()
    Label(dashboard_frame, text="Here you can see an overview of the library system.").pack()

    return dashboard_frame
