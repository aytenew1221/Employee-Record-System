from tkinter import *
def create_dashboard(root):

    dashboard_frame = Frame(
        root,
        bd=2,
        relief=RIDGE,
        bg="#f0f0f0"
    )

    dashboard_frame.place(x=0, y=190, relwidth=1, height=90)

    # ================= DASHBOARD CARDS =============

    cards = [
        ("TOTAL EMPLOYEES\n120", "#4CAF50"),
        ("HR DEPARTMENT\n25", "#2196F3"),
        ("MANAGERS\n15", "#FF9800"),
        ("SOFTWARE ENGINEERS\n80", "#9C27B0"),
        ("TOTAL SALARY\n500,000 ETB", "#E91E63")
    ]

    x_positions = [20, 270, 520, 770, 1020]
    widths = [220, 220, 220, 220, 250]

    for i in range(len(cards)):

        card = Frame(
            dashboard_frame,
            bg=cards[i][1],
            bd=2,
            relief=RIDGE
        )

        card.place(
            x=x_positions[i],
            y=10,
            width=widths[i],
            height=65
        )

        lbl = Label(
            card,
            text=cards[i][0],
            font=("arial", 15, "bold"),
            bg=cards[i][1],
            fg="white"
        )

        lbl.pack(fill=BOTH, expand=True)