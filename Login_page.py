from tkinter import *

main = Tk()
main.geometry("500x500")
main.configure(bg='#868686')
Show = IntVar()


def LOGIN_PAGE():     #first page
    main.title("Login Page")
    def check_Password():#function to show password
        if Show.get():
            entry_password.config(show="")
            label_showpass.config(fg="#008A44")
            check_showpass.config(bg="#008A44")
        else:
            entry_password.config(show="*")
            label_showpass.config(fg="white")
            check_showpass.config(bg="#262626")

    login_frame = Frame(main,bg='#262626')
    #adding widgets
    #username
    label_user_name = Label(login_frame,text="Email or UserID",fg='white',bg='#262626',font=("Arial",18,"bold"))
    entry_name = Entry(login_frame,bg="#131313",fg="white",font=("Arial",20),width=25,insertbackground="#008A44")
    #password
    label_password = Label(login_frame,text="Password",fg='white',bg='#262626',font=("Arial",18,"bold"))
    entry_password = Entry(login_frame,bg="#131313",fg="white",show ="*",font=("Arial",20),width=25,insertbackground="#008A44")
    #show password
    check_showpass = Checkbutton(login_frame,bg="#262626",fg="black",borderwidth=0,variable=Show,onvalue=1,offvalue=0,command=check_Password)
    label_showpass = Label(login_frame,text="Show password",bg="#262626",fg="white",font=("Arial",10))
    #login button
    button_Login = Button(login_frame,text ="LOG IN",bg ='#008A44',fg="white",font=("Arial",12,"bold"),width=12)
    #Forgot password
    button_forgot_pass = Button(login_frame,text="Forgot Password?",borderwidth=0,font=("Arial",10,"underline"),fg="white",bg="#262626")
    #signup
    label_signup=Label(login_frame,text="Don't have an account?",font=("Arial",11),bg="#262626",fg="#b9b9b9")
    button_signup=Button(login_frame,text="Sign up",borderwidth=0,font=("Arial",10,"underline"),fg="white",bg="#262626")

    #placing widget
    label_user_name.grid(row=1,column = 0,padx = 40,pady=(60,5),sticky="w")
    entry_name.grid(row = 2,column=0,padx=40,pady=5,sticky="w")
    label_password.grid(row = 3,column=0,padx=40,pady=5,sticky="w")
    entry_password.grid(row = 4,column=0,padx=40,pady=5,sticky="w")
    check_showpass.grid(row = 5,column=0,padx=(40,0),pady=5,sticky="w")
    label_showpass.grid(row = 5,column=0,padx=(60,0),pady=5,sticky="w")
    button_Login.grid(row = 6,column=0,pady=5,columnspan=2)
    button_forgot_pass.grid(row = 7,column=0,pady=5,columnspan=2)
    label_signup.grid(row=8,column=0,padx=(118,0),pady=5,sticky="nw")
    button_signup.grid(row=8,column=0,padx=(140,0),pady=(5,60))  
    #centering a frame
    login_frame.place(relx=.5, rely=.5,anchor= CENTER)
    
LOGIN_PAGE()
main.mainloop()