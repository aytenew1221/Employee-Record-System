from tkinter import *
from tkinter import ttk


def create_employee_form(employee_obj, parent_frame):

    upper_frame = LabelFrame(
        parent_frame,
        bd=2,
        relief=RIDGE,
        bg="white",
        text="Employee Information",
        font=("times new roman", 11, "bold"),
        fg="red"
    )

    upper_frame.place(x=10, y=10, relwidth=0.98, height=270)

    # ================= Department =================

    lbl_dep = Label(
        upper_frame,
        text="Department",
        font=("arial", 11, "bold"),
        bg="white"
    )

    lbl_dep.grid(row=0, column=0, padx=5, pady=7, sticky=W)

    combo_dep = ttk.Combobox(
        upper_frame,
        textvariable=employee_obj.var_department,
        font=("arial", 12, "bold"),
        width=17,
        state="readonly"
    )

    combo_dep["values"] = (
        "Select Department",
        "HR",
        "Software Engineer",
        "Manager"
    )

    combo_dep.current(0)

    combo_dep.grid(row=0, column=1, padx=5, pady=7, sticky=W)

    # ================= Name =================

    lbl_name = Label(
        upper_frame,
        text="Name",
        font=("arial", 12, "bold"),
        bg="white"
    )

    lbl_name.grid(row=0, column=2, padx=5, pady=7, sticky=W)

    txt_name = ttk.Entry(
        upper_frame,
        textvariable=employee_obj.var_name,
        width=22,
        font=("arial", 11, "bold")
    )

    txt_name.grid(row=0, column=3, padx=5, pady=7)

    # ================= Designation =================

    lbl_designation = Label(
        upper_frame,
        text="Designation",
        font=("arial", 12, "bold"),
        bg="white"
    )

    lbl_designation.grid(row=1, column=0, padx=5, pady=7, sticky=W)

    txt_designation = ttk.Entry(
        upper_frame,
        textvariable=employee_obj.var_designation,
        width=22,
        font=("arial", 11, "bold")
    )

    txt_designation.grid(row=1, column=1, padx=5, pady=7)

    # ================= Email =================

    lbl_email = Label(
        upper_frame,
        text="Email",
        font=("arial", 12, "bold"),
        bg="white"
    )

    lbl_email.grid(row=1, column=2, padx=5, pady=7, sticky=W)

    txt_email = ttk.Entry(
        upper_frame,
        textvariable=employee_obj.var_email,
        width=22,
        font=("arial", 11, "bold")
    )

    txt_email.grid(row=1, column=3, padx=5, pady=7)

    # ================= Address =================

    lbl_address = Label(
        upper_frame,
        text="Address",
        font=("arial", 12, "bold"),
        bg="white"
    )

    lbl_address.grid(row=2, column=0, padx=5, pady=7, sticky=W)

    txt_address = ttk.Entry(
        upper_frame,
        textvariable=employee_obj.var_address,
        width=22,
        font=("arial", 11, "bold")
    )

    txt_address.grid(row=2, column=1, padx=5, pady=7)

    # ================= Marital Status =================

    lbl_marital = Label(
        upper_frame,
        text="Marital Status",
        font=("arial", 11, "bold"),
        bg="white"
    )

    lbl_marital.grid(row=2, column=2, padx=5, pady=7, sticky=W)

    combo_marital = ttk.Combobox(
        upper_frame,
        textvariable=employee_obj.var_marital,
        font=("arial", 12, "bold"),
        width=17,
        state="readonly"
    )

    combo_marital["values"] = (
        "Select Status",
        "Single",
        "Married",
        "Divorced"
    )

    combo_marital.current(0)

    combo_marital.grid(row=2, column=3, padx=5, pady=7, sticky=W)

    # ================= Date of Birth =================

    lbl_dob = Label(
        upper_frame,
        text="Date of Birth",
        font=("arial", 12, "bold"),
        bg="white"
    )

    lbl_dob.grid(row=3, column=0, padx=5, pady=7, sticky=W)

    txt_dob = ttk.Entry(
        upper_frame,
        textvariable=employee_obj.var_date_of_birth,
        width=22,
        font=("arial", 11, "bold")
    )

    txt_dob.grid(row=3, column=1, padx=5, pady=7)

    # ================= Date of Joining =================

    lbl_joining = Label(
        upper_frame,
        text="Date of Joining",
        font=("arial", 12, "bold"),
        bg="white"
    )

    lbl_joining.grid(row=3, column=2, padx=5, pady=7, sticky=W)

    txt_joining = ttk.Entry(
        upper_frame,
        textvariable=employee_obj.var_date_of_joining,
        width=22,
        font=("arial", 11, "bold")
    )

    txt_joining.grid(row=3, column=3, padx=5, pady=7)

    # # ================= ID Proof =================

    # lbl_id = Label(
    #     upper_frame,
    #     text="ID Proof",
    #     font=("arial", 11, "bold"),
    #     bg="white"
    # )

    # lbl_id.grid(row=4, column=0, padx=5, pady=7, sticky=W)

    # combo_id_proof = ttk.Combobox(
    #     upper_frame,
    #     textvariable=employee_obj.var_id_proof,
    #     font=("arial", 12, "bold"),
    #     width=17,
    #     state="readonly"
    # )

    # combo_id_proof["values"] = (
    #     "Select ID Proof",
    #     "FIDA",
    #     "Kebele ID",
    #     "Passport",
    #     "Driving License",
    #     "Employee ID"
    # )
    # combo_id_proof.current(0)

    # combo_id_proof.grid(row=4, column=1, padx=5, pady=7, sticky=W)
   
    #================ID_PROOF================================
    com_txt_proof = ttk.Combobox(upper_frame, state='readonly',width=18,font=('arial', 12, 'bold'))
    com_txt_proof['values'] = ("Select ID Proof","Kebele ID", "FIDA", "Driving Licence", "Driving Licence", "Employee ID")
    com_txt_proof.current(0)
    com_txt_proof.grid(row=4, column=0, padx=2, pady=7, sticky=W)

    txt_proof = ttk.Entry(upper_frame, textvariable=employee_obj.var_id_proof, width=22, font=('arial', 11, 'bold'))
    txt_proof.grid(row=4, column=1, padx=2, pady=7, sticky=W)
        


    # ================= Gender =================

    lbl_gender = Label(
        upper_frame,
        text="Gender",
        font=("arial", 12, "bold"),
        bg="white"
    )

    lbl_gender.grid(row=4, column=2, padx=5, pady=7, sticky=W)

    combo_gender = ttk.Combobox(
        upper_frame,
        textvariable=employee_obj.var_gender,
        font=("arial", 12, "bold"),
        width=17,
        state="readonly"
    )

    combo_gender["values"] = (
        "Male",
        "Female",
        "Other"
    )

    combo_gender.current(0)

    combo_gender.grid(row=4, column=3, padx=5, pady=7, sticky=W)

    # ================= Phone =================

    lbl_phone = Label(
        upper_frame,
        text="Phone Number",
        font=("arial", 12, "bold"),
        bg="white"
    )

    lbl_phone.grid(row=0, column=4, padx=5, pady=7, sticky=W)

    txt_phone = ttk.Entry(
        upper_frame,
        textvariable=employee_obj.var_phone,
        width=22,
        font=("arial", 11, "bold")
    )

    txt_phone.grid(row=0, column=5, padx=5, pady=7)

    # ================= Country =================

    lbl_country = Label(
        upper_frame,
        text="Country",
        font=("arial", 12, "bold"),
        bg="white"
    )

    lbl_country.grid(row=1, column=4, padx=5, pady=7, sticky=W)

    txt_country = ttk.Entry(
        upper_frame,
        textvariable=employee_obj.var_country,
        width=22,
        font=("arial", 11, "bold")
    )

    txt_country.grid(row=1, column=5, padx=5, pady=7)

    # ================= Salary =================

    lbl_salary = Label(
        upper_frame,
        text="Salary",
        font=("arial", 12, "bold"),
        bg="white"
    )

    lbl_salary.grid(row=2, column=4, padx=5, pady=7, sticky=W)

    txt_salary = ttk.Entry(
        upper_frame,
        textvariable=employee_obj.var_salary,
        width=22,
        font=("arial", 11, "bold")
    )

    txt_salary.grid(row=2, column=5, padx=5, pady=7)

    # ================= Button Frame =================

    button_frame = Frame(
        upper_frame,
        bd=2,
        relief=RIDGE,
        bg="white"
    )

    button_frame.place(
        relx=0.82,
        rely=0.05,
        relwidth=0.15,
        relheight=0.85
    )

    # ================= Buttons =================

    btn_add = Button(
        button_frame,
        text="Save",
        command=employee_obj.add_data,
        font=("arial", 14, "bold"),
        width=13,
        bg="blue",
        fg="white"
    )

    btn_add.grid(row=0, column=0, padx=1, pady=5)

    btn_update = Button(
        button_frame,
        text="Update",
        font=("arial", 14, "bold"),
        width=13,
        bg="blue",
        fg="white"
    )

    btn_update.grid(row=1, column=0, padx=1, pady=5)

    btn_delete = Button(
        button_frame,
        text="Delete",
        font=("arial", 14, "bold"),
        width=13,
        bg="blue",
        fg="white"
    )

    btn_delete.grid(row=2, column=0, padx=1, pady=5)

    btn_clear = Button(
        button_frame,
        text="Clear",
        font=("arial", 14, "bold"),
        width=13,
        bg="blue",
        fg="white"
    )

    btn_clear.grid(row=3, column=0, padx=1, pady=5)