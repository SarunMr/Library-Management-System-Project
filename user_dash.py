from tkinter import *
from PIL import *
#theme color.
TEXTCOLOR ="#FFFFFF"
FRAME_TITLEBAR_BG ="#008A44"
FRAME_MENUBAR_BG = "#262626"
SWITCH_COLOR = "#5F5F5F"
FRAME_DASHBOARD_BG = '#343233'

window = Tk()

#icons
menubutton_icon = PhotoImage(file="icons_lib/menu_button.png")
menubuttontoggle_icon = PhotoImage(file="icons_lib/cross.png")
dashboard_icon = PhotoImage(file="icons_lib/dash_icon.png")
request_books_icon = PhotoImage(file="icons_lib/request_books_icon.png")
return_books_icon = PhotoImage(file="icons_lib/return_ic.png")
books_log_icon =PhotoImage(file="icons_lib/log_icon.png")
profile_icon =PhotoImage(file="icons_lib/profile.png")
logout_icon = PhotoImage(file="icons_lib/logout_icon.png")


window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1,weight=1)
window.grid_rowconfigure(1,weight=1)

def update_label_color_on_tap(n):
    label_dict = {"1":lib_dash_label,"2":lib_requestbook_label,"3":lib_returnbook_label,"4":lib_log_label,"5":lib_profile_label}
    btn_dict = {"1":lib_dash_button,"2":lib_request_book_button,"3":lib_return_book_button,"4":lib_log_button,"5":lib_profile_button}
    for label in label_dict.keys():
        if label == n:
            label_dict[label].config(bg=SWITCH_COLOR)
            btn_dict[label].config(bg=SWITCH_COLOR)
        else:
            label_dict[label].config(bg=FRAME_MENUBAR_BG)
            btn_dict[label].config(bg=FRAME_MENUBAR_BG)

def default_menubar():
    labellst = [lib_dash_label,lib_requestbook_label,lib_returnbook_label,lib_log_label,lib_profile_label]
    for label in labellst:
        label.config(width=10)
    
    lib_menu_button.config(image=menubutton_icon)
    lib_dash_button.config(text="",width=45,)
    lib_request_book_button.config(text="",width=45)
    lib_return_book_button.config(text="",width=45)
    lib_log_button.config(text="",width=45)
    lib_profile_button.config(text="",width=45)
    lib_logout_button.config(text="")
    lib_menu_button.config(command=extend_menubar)


def extend_menubar():
    labellst = [lib_dash_label,lib_requestbook_label,lib_returnbook_label,lib_log_label,lib_profile_label]
    for label in labellst:
        label.config(width=40)

    lib_menu_button.config(image=menubuttontoggle_icon,padx=13,pady=30)
    lib_dash_button.config(text="Dashboard",width=200,padx=20,anchor="w")
    lib_request_book_button.config(text="Request Books",width=200,padx=20,anchor="w")
    lib_return_book_button.config(text="Return Books",width=200,padx=20,anchor="w")
    lib_log_button.config(text="Books Log",width=200,padx=20,anchor="w")
    lib_profile_button.config(text="Your Profile",width=200,padx=20,anchor="w")
    lib_logout_button.config(text="Log out")
    lib_menu_button.config(command=default_menubar)



frame_titlebar =Frame(window,bg=FRAME_TITLEBAR_BG)
frame_titlebar.columnconfigure(0,weight=0)
frame_titlebar.columnconfigure(1,weight=1)
lib_menu_button=Button(frame_titlebar,image=menubutton_icon,bg=FRAME_TITLEBAR_BG,borderwidth=0,activebackground=FRAME_TITLEBAR_BG,command=extend_menubar)
lib_name = Label(frame_titlebar,text="Lorem Library",font=("Arial",35,"bold"),fg=TEXTCOLOR,bg=FRAME_TITLEBAR_BG,anchor="w")
#placingwidgets
lib_menu_button.grid(row= 0,column=0,padx=10,pady=10)
lib_name.grid(row=0,column=1,padx=(35,0),sticky="w")


frame_menubar=Frame(window,bg=FRAME_MENUBAR_BG)
lib_dash_label = Label(frame_menubar,bg=SWITCH_COLOR,height=4,width=10)
lib_dash_button =Button(frame_menubar,image=dashboard_icon,text="",font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=SWITCH_COLOR,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:update_label_color_on_tap("1"))
lib_requestbook_label = Label(frame_menubar,bg=FRAME_MENUBAR_BG,height=4,width=10)
lib_request_book_button =Button(frame_menubar,image=request_books_icon,font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:update_label_color_on_tap("2"))
lib_returnbook_label = Label(frame_menubar,bg=FRAME_MENUBAR_BG,height=4,width=10)
lib_return_book_button =Button(frame_menubar,image=return_books_icon,font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:update_label_color_on_tap("3"))
lib_log_label = Label(frame_menubar,bg=FRAME_MENUBAR_BG,height=4,width=10)
lib_log_button =Button(frame_menubar,image=books_log_icon,font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:update_label_color_on_tap("4"))
lib_profile_label = Label(frame_menubar,bg=FRAME_MENUBAR_BG,height=4,width=10)
lib_profile_button =Button(frame_menubar,image=profile_icon,font=("Arial",15,"bold"),compound=LEFT,fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,borderwidth=0,activebackground=SWITCH_COLOR,command=lambda:update_label_color_on_tap("5"))
lib_logout_button =Button(frame_menubar,image=logout_icon,bg=FRAME_MENUBAR_BG,font=("Arial",15,"bold"),compound=LEFT,fg="#FF4500",borderwidth=0,activebackground=FRAME_MENUBAR_BG,)

#placing inside menuframe
lib_dash_label.grid(row=0,column=0,padx=13,pady=(30,35))
lib_dash_button.grid(row=0,column=0,padx=13,pady=(30,35))
lib_requestbook_label.grid(row=1,column=0,padx=13,pady=(0,35))
lib_request_book_button.grid(row=1,column=0,padx=13,pady=(0,35))
lib_returnbook_label.grid(row=2,column=0,padx=13,pady=(0,35))
lib_return_book_button.grid(row=2,column=0,padx=13,pady=(0,35))
lib_log_label.grid(row=3,column=0,padx=13,pady=(0,35))
lib_log_button.grid(row=3,column=0,padx=13,pady=(0,35))
lib_profile_label.grid(row=4,column=0,padx=13,pady=(0,35))
lib_profile_button.grid(row=4,column=0,padx=13,pady=(0,35))
lib_logout_button.grid(row=5,column=0,padx=13,pady=(30))


frame_dashboard = Frame(window,bg=FRAME_DASHBOARD_BG,width=1120)
frame_dashboard.grid_propagate(0)
welcome_label = Label(frame_dashboard,text="WELCOME Username",font=("Arial",30,"bold"),fg=FRAME_TITLEBAR_BG,bg=FRAME_DASHBOARD_BG,anchor="w",width=45)
welcome_label.grid(row =0,column=0,padx=15,pady=(10,0),sticky="wn")

frametracker = Frame(frame_dashboard,bg=FRAME_DASHBOARD_BG)
frametracker.grid_columnconfigure(0,weight=1)
frametracker.grid_columnconfigure(1,weight=1)
frametracker.grid_columnconfigure(2,weight=1)

frametotalbooks = Frame(frametracker,bg=FRAME_MENUBAR_BG)
frametotalbooks.grid(row=0,column=0,padx=(15,20),sticky="w")
labeltotalbooks =Label(frametotalbooks,text="Total Books",font=("ArialBold",16),fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,width=16)
labelbooksquantity = Label(frametotalbooks,text="0",font=("ArialBold",16),fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG)
labeltotalbooks.grid(row=0,column=0,padx=20,pady=(10,5))
labelbooksquantity.grid(row=1,column=0,pady=5)

frametotalrequests = Frame(frametracker,bg=FRAME_MENUBAR_BG)
frametotalrequests.grid(row=0,column=1,padx=80)
labeltotalrequests =Label(frametotalrequests,text="Total Book Request",font=("ArialBold",16),fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,width=16)
labelrequestquantity = Label(frametotalrequests,text="0",font=("ArialBold",16),fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG)
labeltotalrequests.grid(row=0,column=0,padx=20,pady=(10,5))
labelrequestquantity.grid(row=1,column=0,pady=5)

frametotalfines = Frame(frametracker,bg=FRAME_MENUBAR_BG)
frametotalfines.grid(row=0,column=2,padx=(20,15),sticky="e")
labeltotalfines =Label(frametotalfines,text="Fines Remianing",font=("ArialBold",16),fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,width=16)
labelfinesquantity = Label(frametotalfines,text=f"$0",font=("ArialBold",16),fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG)
labeltotalfines.grid(row=0,column=0,padx=20,pady=(10,5))
labelfinesquantity.grid(row=1,column=0,pady=5)

quickreqlabel = Label(frame_dashboard,text="Quick Request",font=("ArialBold",14),fg=TEXTCOLOR,bg=FRAME_DASHBOARD_BG)



framequickrequesttable = Frame(frame_dashboard,bg=FRAME_MENUBAR_BG,height=240)
framequickrequesttable.grid_columnconfigure(0,weight=0)
framequickrequesttable.grid_columnconfigure(1,weight=1)
framequickrequesttable.grid_columnconfigure(2,weight=1)
framequickrequesttable.grid_columnconfigure(3,weight=0)
framequickrequesttable.grid_columnconfigure(4,weight=0)
framequickrequesttable.grid_propagate(0)


Lbookid = Label(framequickrequesttable,text="Book ID",font=("ArialLightRegular",12),fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG).grid(row=1,column=0,padx=35,sticky="w")
Lbookname = Label(framequickrequesttable,text="Book Name",font=("ArialLightRegular",12),fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG).grid(row=1,column=1,padx=5,sticky="w")
Lauthor = Label(framequickrequesttable,text="Author",font=("ArialLightRegular",12),fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG).grid(row=1,column=2,sticky="w")
Lavialable = Label(framequickrequesttable,text="Avialable",font=("ArialLightRegular",12),fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG).grid(row=1,column=3,padx=35,sticky="w")
Ladd = Label(framequickrequesttable,text="Add",font=("ArialLightRegular",12),fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,width=5).grid(row=1,column=4,padx=10,sticky="we")

latestbooklabel = Label(frame_dashboard,text="Latest Book Added",font=("ArialBold",14),fg=TEXTCOLOR,bg=FRAME_DASHBOARD_BG)
framelatestbooks = Frame(frame_dashboard,bg=FRAME_DASHBOARD_BG,height=230,width=900,)
framelatestbooks.grid_columnconfigure(0,weight=1)
framelatestbooks.grid_columnconfigure(1,weight=1)
framelatestbooks.grid_columnconfigure(2,weight=1)
framelatestbooks.grid_columnconfigure(3,weight=1)
framelatestbooks.grid_propagate(0)
b1=PhotoImage(file="books/b1.png")
buttonb1=Button(framelatestbooks,image=b1,bg=FRAME_DASHBOARD_BG,borderwidth=0,activebackground=FRAME_DASHBOARD_BG)
buttonb1.grid(row=0,column=0,padx=(20,0),sticky="w")



frametracker.grid(row=1,column=0,padx=10,pady=2,sticky="wne")
quickreqlabel.grid(row=2,column=0,padx=25,pady=(4,3),sticky="w")
framequickrequesttable.grid(row=3,column=0,padx=(25,25),pady=2,sticky="wne")
latestbooklabel.grid(row=4,column=0,padx=25,pady=(4,3),sticky="w")
framelatestbooks.grid(row=5,column=0,padx=(25,25),pady=2,sticky="wnes")

#placing frames
frame_titlebar.grid(row=0, column=0,columnspan=2,sticky="we")
frame_menubar.grid(row=1,column=0,sticky="wsn")
frame_dashboard.grid(row=1,column=1,padx=(20,0),pady=(10,0),sticky="ns",)
window.mainloop()
