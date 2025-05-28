from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from mysql.connector import Error

def bom_form(app):
    bom_frame = Frame(app, width=1070, height=800, bg="white")
    bom_frame.place(x=250, y=110)

    billofmaterials_frame = Frame(bom_frame, bd=15, relief="ridge", bg="#F4E7E1")
    billofmaterials_frame.place(x=20, y=20, width=980, height=500)  # Giả sử frame này là "trống"

    Scroll_x = ttk.Scrollbar(billofmaterials_frame, orient="horizontal")
    Scroll_y = ttk.Scrollbar(billofmaterials_frame, orient="vertical")

    bom_table = ttk.Treeview(billofmaterials_frame, columns=("ProductID", "MaterialID", "QuantityNeeded"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
    Scroll_x.pack(side=BOTTOM, fill=X)
    Scroll_y.pack(side=RIGHT, fill=Y)
    
    Scroll_x.config(command=bom_table.xview)
    Scroll_y.config(command=bom_table.yview)

    bom_table.heading("ProductID", text="Product ID")
    bom_table.heading("MaterialID", text="Material ID")
    bom_table.heading("QuantityNeeded", text="Quantity Needed")
    bom_table["show"] = "headings"  # Hiển thị tiêu đề cột
    bom_table.pack(fill=BOTH, expand=True)  # Đặt Treeview vào frame trống

    load_products_to_treeview(bom_table)

def connect_database():
    # Replace with your actual database connection details
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="nguyenhue",
        database="manufacturing_process"
    )

def load_products_to_treeview(bom_table):
    # Xóa dữ liệu cũ (nếu có)
    for item in bom_table.get_children():
        bom_table.delete(item)

    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT ProductID, MaterialID, QuantityNeeded FROM bom")
        rows = cursor.fetchall()

        for row in rows:
            bom_table.insert("", "end", values=row)

        conn.close()
    except Exception as err:
        messagebox.showerror("Database Error", f"Failed to load data: {err}")