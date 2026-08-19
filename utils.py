from tkinter import *

#Animated imployee table
def move_title(employee_obj):

    text = employee_obj.title_text

    employee_obj.title_text = text[1:] + text[0]

    employee_obj.lbl_title.config(text=employee_obj.title_text)

    employee_obj.lbl_title.after(200, lambda: move_title(employee_obj))