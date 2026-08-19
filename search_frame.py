from tkinter import *
from tkinter import ttk


def create_employee_table(employee_obj, parent_frame):

    # ================= Down Frame =================

    down_frame = LabelFrame(
        parent_frame,
        bd=2,
        relief=RIDGE,
        bg="white",
        text="Employee Information Table",
        font=("times new roman", 11, "bold"),
        fg="red"
    )

    down_frame.place(
        x=10,
        y=290,
        relwidth=0.98,
        relheight=0.42
    )

    # ================= Search Frame =================

    search_frame = Frame(
        down_frame,
        bd=2,
        relief=RIDGE,
        bg="white"
    )

    search_frame.place(
        x=5,
        y=5,
        relwidth=0.99,
        height=50
    )

    # ================= Search Label =================

    lbl_search = Label(
        search_frame,
        text="Search By",
        font=("arial", 12, "bold"),
        bg="white"
    )

    lbl_search.grid(row=0, column=0, padx=10, pady=10)

    # ================= Search Combo =================

    combo_search = ttk.Combobox(
        search_frame,
        textvariable=employee_obj.var_search_by,
        width=18,
        font=("arial", 11, "bold"),
        state="readonly"
    )

    combo_search["values"] = (
        "Select",
        "Name",
        "Phone",
        "Email",
        "Department"
    )

    combo_search.current(0)

    combo_search.grid(row=0, column=1, padx=5, pady=10)

    # ================= Search Entry =================

    txt_search = ttk.Entry(
        search_frame,
        textvariable=employee_obj.var_search_text,
        width=25,
        font=("arial", 11, "bold")
    )

    txt_search.grid(row=0, column=2, padx=5, pady=10)

    # ================= Search Button =================

    btn_search = Button(
        search_frame,
        text="Search",
        command=employee_obj.search_data,
        font=("arial", 12, "bold"),
        bg="blue",
        fg="white",
        cursor="hand2",
        width=12
    )

    btn_search.grid(row=0, column=3, padx=10)

    # ================= Show All Button =================

    btn_show = Button(
        search_frame,
        text="Show All",
        command=employee_obj.fetch_data,
        font=("arial", 12, "bold"),
        bg="green",
        fg="white",
        cursor="hand2",
        width=12
    )

    btn_show.grid(row=0, column=4, padx=10)

    # ================= Table Frame =================

    table_frame = Frame(
        down_frame,
        bd=3,
        relief=RIDGE,
        bg="white"
    )

    table_frame.place(
        x=5,
        y=60,
        relwidth=0.99,
        relheight=0.78
    )

    # ================= Scrollbars =================

    scroll_x = ttk.Scrollbar(
        table_frame,
        orient=HORIZONTAL
    )

    scroll_y = ttk.Scrollbar(
        table_frame,
        orient=VERTICAL
    )

    # ================= Treeview =================

    employee_obj.employee_table = ttk.Treeview(
        table_frame,
        columns=(
            "department",
            "name",
            "designation",
            "email",
            "address",
            "marital",
            "dob",
            "doj",
            "idproof",
            "gender",
            "phone",
            "country",
            "salary"
        ),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set,
        show="headings"
    )

    # ================= Scrollbar Config =================

    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)

    scroll_x.config(command=employee_obj.employee_table.xview)
    scroll_y.config(command=employee_obj.employee_table.yview)

    # ================= Table Pack =================

    employee_obj.employee_table.pack(
        side=LEFT,
        fill=BOTH,
        expand=1
    )

    # ================= Headings =================

    employee_obj.employee_table.heading("department", text="Department")
    employee_obj.employee_table.heading("name", text="Name")
    employee_obj.employee_table.heading("designation", text="Designation")
    employee_obj.employee_table.heading("email", text="Email")
    employee_obj.employee_table.heading("address", text="Address")
    employee_obj.employee_table.heading("marital", text="Marital Status")
    employee_obj.employee_table.heading("dob", text="Date of Birth")
    employee_obj.employee_table.heading("doj", text="Date of Joining")
    employee_obj.employee_table.heading("idproof", text="ID Proof")
    employee_obj.employee_table.heading("gender", text="Gender")
    employee_obj.employee_table.heading("phone", text="Phone")
    employee_obj.employee_table.heading("country", text="Country")
    employee_obj.employee_table.heading("salary", text="Salary")

    # ================= Column Width =================

    columns = (
        "department",
        "name",
        "designation",
        "email",
        "address",
        "marital",
        "dob",
        "doj",
        "idproof",
        "gender",
        "phone",
        "country",
        "salary"
    )

    for col in columns:

        employee_obj.employee_table.column(
            col,
            width=130,
            anchor=CENTER
        )