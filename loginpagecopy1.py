from tkinter import*
from tkinter import ttk
from unicodedata import name
from PIL import Image,ImageTk
from tkinter import messagebox

from pip import main
class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.bg=ImageTk.PhotoImage(file=r"E:\Register and Login Form\backgroundimage.jfif")
        frame = Frame(self.root, bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        img1=Image.open("E:\Register and Login Form\loginimage.jfif")
        img1=img1.resize((60,60),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        #Label use create entry fill and registration
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=185,width=270)
        # Label use create entry fill for password
        password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=255, width=270)
        #Icon image for username and password
        img2 = Image.open("E:\Register and Login Form\loginimage1.jfif")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=326, width=25, height=25)
        #icon image for password

        # Icon image for username and password
        img3 = Image.open("E:\Register and Login Form\passwordimage.jfif")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=400, width=25, height=25)
        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=120,y=300,width=120,height=40)
        #registerbutton
        registerbtn = Button(frame, text="New Registeration", font=("times new roman", 10, "bold"), borderwidth=0, fg="white",
                          bg="black", activeforeground="white", activebackground="red")
        registerbtn.place(x=40, y=350, width=120)
        #forgotpasswordbtn
        forgotpass = Button(frame, text="Forgot password", font=("times new roman", 10, "bold"), borderwidth=0, fg="white",
                          bg="black", activeforeground="white", activebackground="red")
        forgotpass.place(x=30, y=370, width=120)
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fiels required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","welcome tp codewithvivek")
        else:
            messagebox.showerror("Invalid username and password")
       # lbl_bg=Label(self.root,image=self.bg)

       # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
      #img1=Image.open(r"E:\Register and Login Form\loginimage.jfif")
       # img1=img1.resize(100,100),Image.ANTIALIAS
        #self.photoimage1=ImageTk.PhotoImage(img1)
        #lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        #lblimg1.place(x=730,y=175,width=100,height=100)



if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()