from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

from database import connect_db
from dashboard import create_dashboard
from employee_form import create_employee_form
from employee_table import create_employee_table
from utils import move_title


class Employee:

    def __init__(self, root):

        self.root = root

        self.root.state("zoomed")

        self.root.title("Employee Management System")

        self.root.configure(bg="white")

        # ================= Variables =================

        self.var_department = StringVar()
        self.var_name = StringVar()
        self.var_designation = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_marital = StringVar()
        self.var_date_of_birth = StringVar()
        self.var_date_of_joining = StringVar()
        self.var_id_proof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()

        # Search Variables
        self.var_search_by = StringVar()
        self.var_search_text = StringVar()

        # ================= Title =================

        self.title_text = " EMPLOYEE MANAGEMENT SYSTEM "

        self.lbl_title = Label(self.root,text=self.title_text,font=("times new roman", 37, "bold"),fg="darkblue",bg="white")

        self.lbl_title.place(x=0, y=0, relwidth=1, height=50)

        move_title(self)

        # ================= Logo =================

        img_logo = Image.open("collage_image/s1.jpg")

        img_logo = img_logo.resize((50, 50), Image.LANCZOS)

        self.photo_logo = ImageTk.PhotoImage(img_logo)

        logo = Label(self.root,image=self.photo_logo,bg="white")

        logo.place(x=20, y=0, width=50, height=50)

        # ================= Dashboard =================

        create_dashboard(self.root)

        # ================= Image Frame =================

        img_frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        img_frame.place(x=0, y=50, relwidth=1, height=140)

        # ================= 1st Image =================

        img1 = Image.open("collage_image/i1.jpg")
        img1 = img1.resize((500, 140), Image.LANCZOS)

        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)

        self.img_1.place(relx=0.0, y=0, relwidth=0.33, height=140)

        # ================= 2nd Image =================

        img2 = Image.open("collage_image/i2.jpg")
        img2 = img2.resize((500, 140), Image.LANCZOS)

        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)

        self.img_2.place(relx=0.33, y=0, relwidth=0.33, height=140)

        # ================= 3rd Image =================

        img3 = Image.open("collage_image/i3.jpg")
        img3 = img3.resize((450, 140), Image.LANCZOS)

        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)

        self.img_3.place(relx=0.66, y=0, relwidth=0.34, height=140)

        # ================= Main Frame =================

        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")

        main_frame.place(relx=0,rely=0.15,relwidth=1,relheight=0.85)

        # ================= Employee Form =================

        create_employee_form(self, main_frame)

        # ================= Employee Table + Search =================

        create_employee_table(self, main_frame)

    # ================= Search Data =================

    def search_data(self):
        print("Search button clicked")

    # ================= Fetch Data =================

    def fetch_data(self):
        print("Show all data")

    # ================= Add Data =================

    def add_data(self):

        if self.var_department.get() == "Select Department" or \
           self.var_name.get() == "" or \
           self.var_email.get() == "":

            messagebox.showerror(
                "Error",
                "All Fields Are Required"
            )

        else:

            try:

                conn = connect_db()

                my_cursor = conn.cursor()

                my_cursor.execute(
                    "INSERT INTO employee VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_department.get(),
                        self.var_name.get(),
                        self.var_designation.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_marital.get(),
                        self.var_date_of_birth.get(),
                        self.var_date_of_joining.get(),
                        self.var_id_proof.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_country.get(),
                        self.var_salary.get()
                    )
                )

                conn.commit()

                conn.close()

                messagebox.showinfo(
                    "Success",
                    "Data Added Successfully"
                )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    f"Error: {str(e)}"
                )