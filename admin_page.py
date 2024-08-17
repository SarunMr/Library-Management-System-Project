from tkinter import *
from PIL import *
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
view_users_icon = PhotoImage(file="icons_lib/log_icon.png")
profile_icon =PhotoImage(file="icons_lib/profile.png")
logout_icon = PhotoImage(file="icons_lib/logout_icon.png")

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
    frame_dashboard = Frame(window,bg=FRAME_DASHBOARD_BG,width=1120)
    frame_dashboard.grid_propagate(0)
    welcome_label = Label(frame_dashboard,text="WELCOME AdminName",font=("Arial",30,"bold"),fg=FRAME_TITLEBAR_BG,bg=FRAME_DASHBOARD_BG,anchor="w",width=45)
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
    labeltotalfines =Label(frametotalfines,text="Total Requests",font=("ArialBold",16),fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG,width=16)
    labelfinesquantity = Label(frametotalfines,text=f"0",font=("ArialBold",16),fg=TEXTCOLOR,bg=FRAME_MENUBAR_BG)
    labeltotalfines.grid(row=0,column=0,padx=20,pady=(10,5))
    labelfinesquantity.grid(row=1,column=0,pady=5)

    quickreqlabel = Label(frame_dashboard,text="All Books",font=("ArialBold",14),fg=TEXTCOLOR,bg=FRAME_DASHBOARD_BG)

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
    buttonb1=Button(framelatestbooks,image=b1,bg=FRAME_DASHBOARD_BG,borderwidth=0,activebackground=FRAME_DASHBOARD_BG)
    buttonb1.grid(row=0,column=0,padx=(20,0),sticky="w")



    frametracker.grid(row=1,column=0,padx=10,pady=2,sticky="wne")
    quickreqlabel.grid(row=2,column=0,padx=25,pady=(4,3),sticky="w")
    framequickrequesttable.grid(row=3,column=0,padx=(25,25),pady=2,sticky="wne")
    latestbooklabel.grid(row=4,column=0,padx=25,pady=(4,3),sticky="w")
    framelatestbooks.grid(row=5,column=0,padx=(25,25),pady=2,sticky="wnes")

    frame_dashboard.grid(row=1,column=1,padx=(20,0),pady=(10,0),sticky="ns")

def viewrequestframe():
    frameviewrequest = Frame(window,bg=FRAME_DASHBOARD_BG,width=1120)
    frameviewrequest.grid_propagate(0)
    
    framepagetitle = Frame(frameviewrequest,bg=FRAME_DASHBOARD_BG,width=1100,height=40)
    framepagetitle.grid_propagate(0)
    framepagetitle.grid_columnconfigure(0,weight=1)
    framepagetitle.grid_columnconfigure(1,weight=0)
    framepagetitle.grid_columnconfigure(2,weight=0)

    libtopbooks = Label(framepagetitle,text="Request From Users",font=("ArialBold",16,"bold"),bg=FRAME_DASHBOARD_BG,fg=TEXTCOLOR,anchor="w")
    libtopbooks.grid(row=0,column=0,padx=(20,0),pady=5,sticky="wne")


    framepagetitle.grid(row=0,column=0,padx=10,pady=10,sticky="ne")

    frametoppicks = Frame(frameviewrequest,bg=FRAME_MENUBAR_BG,height=250)
    frametoppicks.grid_columnconfigure(0,weight=0)
    frametoppicks.grid_columnconfigure(1,weight=1)
    frametoppicks.grid_columnconfigure(2,weight=1)
    frametoppicks.grid_columnconfigure(3,weight=0)
    frametoppicks.grid_columnconfigure(4,weight=0)
    frametoppicks.grid_propagate(0)
    frametoppicks.grid(row=1,column=0,padx=25,pady=2,sticky="wne")

    lblrqstbooks = Label(frameviewrequest,text="Request Approval",font=("ArialBold",16,"bold"),bg=FRAME_DASHBOARD_BG,fg=TEXTCOLOR)
    lblrqstbooks.grid(row=2,column=0,padx=25,pady=15,sticky='w')

    frame_request_label = Frame(frameviewrequest,bg = FRAME_DASHBOARD_BG)
    frame_request_label.grid_columnconfigure(0,weight=0)
    frame_request_label.grid_columnconfigure(1,weight=0)
    frame_request_label.grid_columnconfigure(2,weight=0)
    frame_request_label.grid_columnconfigure(3,weight=0)
    lblbookID = Label(frame_request_label,text="Account ID:",font=("Arial",12,"bold"),fg=TEXTCOLOR,bg=FRAME_DASHBOARD_BG)
    lblbookID.grid(row=0,column=0,padx=(80,20),pady=(25,15),sticky="e")
    entbookID = Entry(frame_request_label,font=("Arial",14))
    entbookID.grid(row=0,column=1,pady=5)
    lblaccountid = Label(frame_request_label,text="Username",font=("Arial",12,"bold"),fg=TEXTCOLOR,bg=FRAME_DASHBOARD_BG)
    lblaccountid.grid(row=0,column=2,padx=(140,20),pady=(25,15))
    entaccountId = Entry(frame_request_label,font=("Arial",14))
    entaccountId.grid(row=0,column=3,padx=(0,10),pady=5,sticky="e",)
    
    # Create a StringVar to hold the selected value
    selected_days = StringVar()
    selected_days.set("15")
    # Create a frame to hold the label and radio buttons
    RDframe = Frame(frame_request_label, bg=FRAME_DASHBOARD_BG)
    RDframe.grid(row=2,column=1,pady=15,sticky="n")
    acceptrequestbuttton = Button(frameviewrequest,text ="Accept",bg ='#008A44',fg=TEXTCOLOR,font=("Arial",12,"bold"))
    acceptrequestbuttton.grid(row=4,column=0,pady=30)
    declinerequestbutton = Button(frameviewrequest,text="Decline",bg='#FF4500',fg=TEXTCOLOR,font=("Arial",12,"bold"))
    declinerequestbutton.grid(row=5,column=0,pady=0)

    frame_request_label.grid(row=3,column=0,padx=25,pady=(15,5),sticky="we")

    frameviewrequest.grid(row=1,column=1,padx=(20,0),pady=(10,0),sticky="ns")

def managebooksframe():
    framemanagebooks = Frame(window,bg=FRAME_DASHBOARD_BG,width=1120)
    framemanagebooks.grid_propagate(0)

    lblYourbooks=Label(framemanagebooks,text="Manage Books",font=("Arial",18,"bold"),fg=TEXTCOLOR,bg=FRAME_DASHBOARD_BG)
    lblYourbooks.grid(row=0,column=0,padx=20,pady=20,sticky='w')


    framereturndetails = Frame(framemanagebooks,background=FRAME_DASHBOARD_BG)
    lblBookID = Label(framereturndetails,text="Book ID:",font=("Arial",18,"bold"),fg=TEXTCOLOR,bg=FRAME_DASHBOARD_BG)
    lblBookID.grid(row=0,column=0,padx=(80,20),pady=(25,15),sticky="w")
    entbookID = Entry(framereturndetails,font=("Arial",18),width=30)
    entbookID.grid(row=0,column=1,pady=5)
    lblbookName = Label(framereturndetails,text="Book Name:",font=("Arial",18,"bold"),fg=TEXTCOLOR,bg=FRAME_DASHBOARD_BG)
    lblbookName.grid(row=1,column=0,padx=(80,20),pady=(25,15),sticky='w')
    entbookName = Entry(framereturndetails,font=("Arial",18),width=30)
    entbookName.grid(row=1,column=1,padx=(0,10),pady=5,sticky="e",)
    lblAuthor = Label(framereturndetails,text="Author:",font=("Arial",18,"bold"),fg=TEXTCOLOR,bg=FRAME_DASHBOARD_BG)
    lblAuthor.grid(row=2,column=0,padx=(80,20),pady=(25,15),sticky="w")
    entAuthor = Entry(framereturndetails,font=("Arial",18),width=30)
    entAuthor.grid(row=2,column=1,pady=5)
    lblgenre = Label(framereturndetails,text="Genre:",font=("Arial",18,"bold"),fg=TEXTCOLOR,bg=FRAME_DASHBOARD_BG)
    lblgenre.grid(row=3,column=0,padx=(80,20),pady=(25,15),sticky="w")
    entgenre = Entry(framereturndetails,font=("Arial",18),width=30)
    entgenre.grid(row=3,column=1,padx=(0,10),pady=5,sticky="e") 
    lblissueamount = Label(framereturndetails,text="Issue Amount:",font=("Arial",18,"bold"),fg=TEXTCOLOR,bg=FRAME_DASHBOARD_BG)
    lblissueamount.grid(row=4,column=0,padx=(80,20),pady=(25,15),sticky="w")
    entissueamount = Entry(framereturndetails,font=("Arial",18),width=30)
    entissueamount.grid(row=4,column=1,padx=(0,10),pady=5,sticky="e")  
    framereturndetails.grid(row=1,column=0,padx=(20,0),pady=(10,0),sticky="ns")

    Addbookbutton= Button(framemanagebooks,text="Add book",bg ='#008A44',fg=TEXTCOLOR,font=("Arial",14,"bold"),width=20)
    Addbookbutton.grid(row=6,column=0,pady=140)
    Removebookbutton= Button(framemanagebooks,text="Remove",bg ='#FF4500',fg=TEXTCOLOR,font=("Arial",14,"bold"),width=20)
    Removebookbutton.grid(row=6,column=1,pady=140)
    # Photo placeholder
    frame_photo = Frame(framemanagebooks, background="white", width=150, height=150)
    frame_photo.grid(row=1, column=1, padx=(50, 20), pady=(0, 20), sticky='ne')
    frame_photo.grid_propagate(0)

    # Upload Photo button
    upload_button = Button(framemanagebooks, text="Upload Photo", bg='#008A44', fg=TEXTCOLOR, font=("Arial", 12), width=15)
    upload_button.grid(row=1, column=1, padx=(80, 20), pady=(0, 20), sticky='')

    framemanagebooks.grid(row=1,column=1,padx=(20,0),pady=(10,0),sticky="ns")



def viewuserframe():
    frameviewuser = Frame(window, bg=FRAME_DASHBOARD_BG, width=1120)
    frameviewuser.grid_propagate(0)

    # All User section
    lbl_all_user = Label(frameviewuser, text="All User", font=("Arial", 16, "bold"), fg="white",bg=FRAME_DASHBOARD_BG)
    lbl_all_user.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    # User list area (placeholder)
    user_list_frame = Frame(frameviewuser, bg=FRAME_MENUBAR_BG, width=1100, height=300)
    user_list_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 20), sticky="nsew")
    user_list_frame.grid_propagate(0)
    frameuserdetails =Frame(frameviewuser, bg=FRAME_DASHBOARD_BG)
    # User details section
    lbl_userid = Label(frameuserdetails, text="UserID :", font=("Arial", 15), fg="white", bg=FRAME_DASHBOARD_BG)
    lbl_userid.grid(row=0, column=0, sticky="w", padx=(50, 5), pady=5)
    entry_userid = Entry(frameuserdetails, font=("Arial", 15), width=20)
    entry_userid.grid(row=0, column=1, sticky="w", padx=(80, 10), pady=5)

    lbl_username = Label(frameuserdetails, text="Username :", font=("Arial", 15), fg="white", bg=FRAME_DASHBOARD_BG)
    lbl_username.grid(row=0, column=2, sticky="w", padx=(140, 10), pady=10)
    entry_username = Entry(frameuserdetails, font=("Arial", 15), width=20)
    entry_username.grid(row=0, column=3, sticky="w", padx=(60, 10), pady=5)

    lbl_fine_amount = Label(frameuserdetails, text="Fine Amount :", font=("Arial", 15), fg="white", bg=FRAME_DASHBOARD_BG)
    lbl_fine_amount.grid(row=1, column=0, sticky="w", padx=(10, 5), pady=5)
    entry_fine_amount = Entry(frameuserdetails, font=("Arial", 15), width=20)
    entry_fine_amount.grid(row=1, column=1, sticky="w", padx=(80, 10), pady=5)

    frameuserdetails.grid(row=3,column=0)
    # Send Fine button
    btn_send_fine = Button(frameviewuser, text="Send Fine", font=("Arial", 12, "bold"), bg="#008A44", fg="white", width=15)
    btn_send_fine.grid(row=4, column=0, padx=10, pady=80)

    frameviewuser.grid(row=1, column=1, padx=(20, 0), pady=(10, 0), sticky="ns")


def yourprofile():
    frameyourprofile = Frame(window,bg=FRAME_DASHBOARD_BG,width=1120)
    frameyourprofile.grid_propagate(0)
 # Photo placeholder
    photo_placeholder = Frame(frameyourprofile, width=150, height=150, bg='grey')
    photo_placeholder.grid(row=0, column=0, padx=10, pady=(30,10))

    # Form fields
    framecredential = Frame(frameyourprofile,bg=FRAME_DASHBOARD_BG,width=1100,height=300,)
    framecredential.grid_propagate(0)
    framecredential.grid_columnconfigure(2,weight=1)
    firstnamelbl = Label(framecredential, text="FirstName:", bg=FRAME_DASHBOARD_BG,font=("Arial",18), fg=TEXTCOLOR).grid(row=1, column=0, sticky='w', padx=(60,10), pady=(50,10))
    firstnamernt = Entry(framecredential,font=("Arial",18), bg=FRAME_MENUBAR_BG, fg=TEXTCOLOR).grid(row=1, column=1, sticky='we', padx=10, pady=(50,10))

    lastnamelbl = Label(framecredential, text="LastName:",font=("Arial",18), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR).grid(row=2, column=0, sticky='w', padx=(60,10), pady=15)
    fisttnaement = Entry(framecredential,font=("Arial",18), bg=FRAME_MENUBAR_BG, fg=TEXTCOLOR).grid(row=2, column=1, sticky='we', padx=10, pady=15)

    contactlbl = Label(framecredential, text="Contact:",font=("Arial",18), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR).grid(row=3, column=0, sticky='w',padx=(60,10), pady=15)
    contactent = Entry(framecredential,font=("Arial",18), bg=FRAME_MENUBAR_BG, fg=TEXTCOLOR).grid(row=3, column=1, sticky='we', padx=10, pady=15)

    emaillbl = Label(framecredential, text="Email:",font=("Arial",18), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR).grid(row=4, column=0, sticky='w',padx=(60,10), pady=15)
    emaillent  =Entry(framecredential, bg=FRAME_MENUBAR_BG,font=("Arial",18), fg=TEXTCOLOR).grid(row=4, column=1, sticky='we', padx=10, pady=15)

    # Gender radio buttons
    genderlbl = Label(framecredential, text="Gender:",font=("Arial",18), bg=FRAME_DASHBOARD_BG, fg=TEXTCOLOR).grid(row=1, column=2, sticky='e', padx=(30,10), pady=15)
    rdM = Radiobutton(framecredential, text="Male",font=("Arial",18), value="male", bg=FRAME_DASHBOARD_BG, selectcolor=FRAME_DASHBOARD_BG, fg=TEXTCOLOR).grid(row=1, column=3, sticky='e', padx=10, pady=15)
    rdF = Radiobutton(framecredential, text="Female",font=("Arial",18), value="female", bg=FRAME_DASHBOARD_BG, selectcolor=FRAME_DASHBOARD_BG, fg=TEXTCOLOR).grid(row=1, column=4, sticky='e', padx=10,pady=15)

    framecredential.grid(row=1,column=0,padx=10,pady=10,)
    # Buttons
    framebutncredential = Frame(frameyourprofile,bg=FRAME_DASHBOARD_BG,width=1100,height=80)
    framebutncredential.grid_propagate(0)
    Button(framebutncredential, text="Save",font=("Arial",18),bg=FRAME_TITLEBAR_BG, fg=TEXTCOLOR).grid(row=0, column=0, pady=20, padx=(250,50), sticky='w')
    Button(framebutncredential, text="Upload Photo",font=("Arial",18), bg=FRAME_TITLEBAR_BG, fg=TEXTCOLOR).grid(row=0, column=1, pady=20,padx=50)
    Button(framebutncredential, text="Delete",font=("Arial",18), bg=FRAME_TITLEBAR_BG, fg=TEXTCOLOR).grid(row=0, column=2, pady=20, padx=50, sticky='e')
    framebutncredential.grid(row=2,column=0,padx=10,pady=10,sticky="we")

    frameyourprofile.grid(row=1,column=1,padx=(20,0),pady=(10,0),sticky="ns")
    
 

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
lib_logout_button =Button(frame_menubar,image=logout_icon,bg=FRAME_MENUBAR_BG,font=("Arial",15,"bold"),compound=LEFT,fg="#FF4500",borderwidth=0,activebackground=FRAME_MENUBAR_BG,)

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
