from tkinter import *
from tkinter import messagebox
from employee import Employee


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400+450+150")
        self.root.title("Login System")
        self.root.config(bg="white")

        title = Label(self.root,text="Employee Login",font=("times new roman", 28, "bold"),bg="white",fg="darkblue")
        title.pack(pady=30)

        # Username
        lbl_user = Label(self.root,text="Username",font=("arial", 15, "bold"),bg="white")
        lbl_user.pack(pady=10)

        self.txt_user = Entry(self.root,font=("arial", 14),bd=3,relief=RIDGE)
        self.txt_user.pack(ipady=5, ipadx=50)

        # Password
        lbl_pass = Label(self.root,text="Password",font=("arial", 15, "bold"),bg="white")
        lbl_pass.pack(pady=10)

        self.txt_pass = Entry(self.root,font=("arial", 14),bd=3,relief=RIDGE,show="*")
        self.txt_pass.pack(ipady=5, ipadx=50)

        # Login Button
        btn_login = Button(self.root, text="LOGIN",command=self.login,font=("arial", 15, "bold"),bg="blue",fg="white",cursor="hand2")
        btn_login.pack(pady=30)

    def login(self):

        if self.txt_user.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")

        elif self.txt_user.get() == "admin" and self.txt_pass.get() == "1234":
            messagebox.showinfo("Success", "Welcome")

            self.root.destroy()

            new_root = Tk()
            obj = Employee(new_root)
            new_root.mainloop()

        else:
            messagebox.showerror("Error", "Invalid Username or Password")