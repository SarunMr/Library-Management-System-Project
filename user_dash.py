from tkinter import *
from PIL import *


#theme color.
TEXTCOLOR ="#FFFFFF"
FRAME_TITLEBAR_BG ="#008A44"

window = Tk()
window.grid_columnconfigure(1, weight=1)
frame_titlebar =Frame(window,bg=FRAME_TITLEBAR_BG)
frame_titlebar.columnconfigure(0,weight=0)
frame_titlebar.columnconfigure(1,weight=2)
lib_menu_button=Button(frame_titlebar,text="not set")
lib_name = Label(frame_titlebar,text="Lorem Library",font=("Arial",35,"bold"),fg=TEXTCOLOR,bg=FRAME_TITLEBAR_BG,anchor="w")



lib_menu_button.grid(row= 0,column=0,padx=20,pady=(10,0))
lib_name.grid(row=0,column=1,padx=(25,0),sticky="we")

frame_titlebar.grid(row=0, column=1, sticky="ew")
window.mainloop()