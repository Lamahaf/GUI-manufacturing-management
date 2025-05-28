from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from mysql.connector import Error

def suppliers_form(app):
    suppliers_frame = Frame(app, width=1070, height=800, bg="white")
    suppliers_frame.place(x=250, y=110)

    heading_label = Label(suppliers_frame,
                          text="Suppliers",
                          font=("Times New Roman", 20, "bold"),
                          bg="#F1BA88",
                          fg = "#521C0D")
    heading_label.place(x=0, y=0, relwidth=1)

    # Frame chứa phần nội dung chính (frame trống)
    Suppliersframe = Frame(suppliers_frame, bd=15, relief="ridge", bg="#F4E7E1")
    Suppliersframe.place(x=20, y=250, width=980, height=290)  # Giả sử frame này là "trống"
    
    Scroll_x = ttk.Scrollbar(Suppliersframe, orient="horizontal")
    Scroll_y = ttk.Scrollbar(Suppliersframe, orient="vertical")
    
    SuppliersTable = ttk.Treeview(Suppliersframe, columns=("SupplierID", "SupplierName", "Address", "PhoneNumber", "MaterialID", "created_at", "expected_delitime", "quantity_delivery", "unit_cost", "tot_price", "status" ), xscrollcommand = Scroll_x.set, yscrollcommand = Scroll_y.set)
    Scroll_x.pack(side=BOTTOM, fill=X)
    Scroll_y.pack(side=RIGHT, fill=Y)

    Scroll_x.config(command=SuppliersTable.xview)
    Scroll_y.config(command=SuppliersTable.yview)

    SuppliersTable.heading("SupplierID", text="Supplier ID")
    SuppliersTable.heading("SupplierName", text="Supplier Name")
    SuppliersTable.heading("Address", text="Address")
    SuppliersTable.heading("PhoneNumber", text="Phone Number")
    SuppliersTable.heading("MaterialID", text="Material ID")
    SuppliersTable.heading("created_at", text="Start Date")
    SuppliersTable.heading("expected_delitime", text="Expected Date")
    SuppliersTable.heading("quantity_delivery", text="Quantity")
    SuppliersTable.heading("unit_cost", text="Unit Cost")
    SuppliersTable.heading("tot_price", text="Total Price")
    SuppliersTable.heading("status", text="Status")

    SuppliersTable.column("Address", width = 400)
    SuppliersTable["show"] = "headings"  # Hiển thị tiêu đề cột

    SuppliersTable.pack(fill=BOTH, expand=True)  # Đặt Treeview vào frame trống

    load_products_to_treeview(SuppliersTable)

    # Frame chứa các nút, đặt ở góc trên của suppliers_frame
    ButtonFrame = Frame(suppliers_frame, bg="white")
    ButtonFrame.place(x=10, y=50)  # Điều chỉnh x, y nếu cần căn chỉnh

    # Các nhãn và ô nhập liệu
    SupllierIDLabel = Label(ButtonFrame, text="Supplier ID", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    SupllierIDLabel.grid(row=2, column=0, padx=0, pady=8)
    SupplierIDEntry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=8, bg="#F4E7E1", fg="#521C0D")
    SupplierIDEntry.grid(row=2, column=1, padx=0, pady=8)
        
    SupplierNameLabel = Label(ButtonFrame, text="Supplier Name", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    SupplierNameLabel.grid(row=3, column=0, padx=0, pady=8)
    SupplierNameEntry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=8, bg="#F4E7E1", fg="#521C0D")
    SupplierNameEntry.grid(row=3, column=1, padx=0, pady=8)

    AddressLabel = Label(ButtonFrame, text="Address", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    AddressLabel.grid(row=2, column=2, padx=0, pady=8)
    AddressEntry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=8, bg="#F4E7E1", fg="#521C0D")
    AddressEntry.grid(row=2, column=3, padx=0, pady=8)

    PhoneNumberLabel = Label(ButtonFrame, text="Phone Number", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    PhoneNumberLabel.grid(row=3, column=2, padx=0, pady=8)
    PhoneNumberEntry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=8, bg = "#F4E7E1", fg = "#521C0D")
    PhoneNumberEntry.grid(row=3, column=3, padx=0, pady=8)

    MaterialIDLabel = Label(ButtonFrame, text="Material ID", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    MaterialIDLabel.grid(row=4, column=0, padx=0, pady=8)
    MaterialIDEntry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=8, bg="#F4E7E1", fg="#521C0D")
    MaterialIDEntry.grid(row=4, column=1, padx=0, pady=8)

    StartDateLabel = Label(ButtonFrame, text="Start Date", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    StartDateLabel.grid(row=4, column=2, padx=0, pady=8)
    StartDateEntry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=8, bg="#F4E7E1", fg="#521C0D")
    StartDateEntry.grid(row=4, column=3, padx=0, pady=8)

    ExpectedDateLabel = Label(ButtonFrame, text="Expected Date", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    ExpectedDateLabel.grid(row=2, column=4, padx=0, pady=8)
    ExpectedDateEntry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=8, bg="#F4E7E1", fg="#521C0D")
    ExpectedDateEntry.grid(row=2, column=5, padx=0, pady=8)

    QuantityLabel = Label(ButtonFrame, text="Quantity", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    QuantityLabel.grid(row=3, column=4, padx=0, pady=8)
    QuantityEntry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=8, bg="#F4E7E1", fg="#521C0D")
    QuantityEntry.grid(row=3, column=5, padx=0, pady=8)

    UnitCostLabel = Label(ButtonFrame, text="Unit Cost", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    UnitCostLabel.grid(row=4, column=4, padx=0, pady=8)
    UnitCostEntry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=8, bg="#F4E7E1", fg="#521C0D")
    UnitCostEntry.grid(row=4, column=5, padx=0, pady=8)

    TotalPriceLabel = Label(ButtonFrame, text="Total Price", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    TotalPriceLabel.grid(row=2, column=6, padx=0, pady=8)
    TotalPriceEntry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=8, bg="#F4E7E1", fg="#521C0D")
    TotalPriceEntry.grid(row=2, column=7, padx=0, pady=8)

    StatusLabel = Label(ButtonFrame, text="Status", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    StatusLabel.grid(row=3, column=6, padx=0, pady=8)
    StatusEntry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=8, bg="#F4E7E1", fg="#521C0D")
    StatusEntry.grid(row=3, column=7, padx=0, pady=8)

    def handle_add_supplier():
        add_supplier(
            SupplierIDEntry.get(),
            SupplierNameEntry.get(),
            AddressEntry.get(),
            PhoneNumberEntry.get(),
            MaterialIDEntry.get(),
            StartDateEntry.get(),
            ExpectedDateEntry.get(),
            QuantityEntry.get(),
            UnitCostEntry.get(),
            TotalPriceEntry.get(),
            StatusEntry.get()
        )
        load_products_to_treeview(SuppliersTable)  # làm mới bảng

    AddSupplierButton = Button(ButtonFrame, text="Add", font=("Times New Roman", 18, "bold"),
                                   fg="#521C0D", bg="#F1BA88", width=8,
                                   command=handle_add_supplier)
    AddSupplierButton.grid(row=0, column=2, padx = 5, pady=5)

    DeleteSupplierButton = Button(ButtonFrame, text="Delete", font=("Times New Roman", 18, "bold"),
                              fg="#521C0D", bg="#F1BA88", width=8,
                              command=lambda: delete_supplier(SuppliersTable))
    DeleteSupplierButton.grid(row=0, column=3, padx = 5, pady=5)

    UpdateSupplierButton = Button(
        ButtonFrame,
        text="Update",
        font=("Times New Roman", 18, "bold"),
        fg="#521C0D",
        bg="#F1BA88",
        width=8,
        command=lambda: update_supplier(
            SupplierIDEntry, SupplierNameEntry, AddressEntry, PhoneNumberEntry,
            MaterialIDEntry, StartDateEntry, ExpectedDateEntry, QuantityEntry,
            UnitCostEntry, TotalPriceEntry, StatusEntry, SuppliersTable
        )
    )
    UpdateSupplierButton.grid(row=0, column=4, padx=5, pady=5)

def connect_database():
    # Replace with your actual database connection details
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="nguyenhue",
        database="manufacturing_process"
    )

def load_products_to_treeview(SuppliersTable):
    # Xóa dữ liệu cũ (nếu có)
    for item in SuppliersTable.get_children():
        SuppliersTable.delete(item)

    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT SupplierID, SupplierName, Address, PhoneNumber, MaterialID, created_at, expected_delitime, quantity_delivery, unit_cost, tot_price, status FROM suppliers_with_deliveries")
        rows = cursor.fetchall()

        for row in rows:
            SuppliersTable.insert("", "end", values=row)

        conn.close()
    except Exception as err:
        messagebox.showerror("Database Error", f"Failed to load data: {err}")

def add_supplier(SupplierID, SupplierName, Address, PhoneNumber, MaterialID, created_at, expected_delitime, quantity_delivery, unit_cost, tot_price, status):
    if SupplierID =="" or SupplierName =="" or Address =="" or PhoneNumber =="" or MaterialID =="" or created_at =="" or expected_delitime =="" or quantity_delivery =="" or unit_cost =="" or tot_price =="" or status =="":
        messagebox.showerror("Error", "All fields are required")
        return
    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO suppliers_with_deliveries 
            (SupplierID, SupplierName, Address, PhoneNumber, MaterialID, created_at, expected_delitime, quantity_delivery, unit_cost, tot_price, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (SupplierID, SupplierName, Address, PhoneNumber, MaterialID, created_at, expected_delitime, quantity_delivery, unit_cost, tot_price, status))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Supplier added successfully!")
        # Optionally, reload the data in the Treeview here
    except Exception as e:
        messagebox.showerror("Database Error", f"Failed to add supplier: {str(e)}")

def delete_supplier(treeview):
    selected_item = treeview.focus()
    if not selected_item:
        messagebox.showerror("Error", "Please select a supplier to delete.")
        return

    values = treeview.item(selected_item, "values")
    supplier_id = values[0]  # cột Supplier ID

    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Supplier ID: {supplier_id}?")
    if not confirm:
        return
def update_supplier(SupplierIDEntry, SupplierNameEntry, AddressEntry, PhoneNumberEntry, MaterialIDEntry, StartDateEntry, ExpectedDateEntry, QuantityEntry, UnitCostEntry, TotalPriceEntry, StatusEntry, SuppliersTable):
    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE suppliers_with_deliveries
            SET SupplierName=%s, Address=%s, PhoneNumber=%s, MaterialID=%s, created_at=%s, expected_delitime=%s,
                quantity_delivery=%s, unit_cost=%s, tot_price=%s, status=%s
            WHERE SupplierID=%s
        """, (
            SupplierNameEntry.get(), AddressEntry.get(), PhoneNumberEntry.get(), MaterialIDEntry.get(),
            StartDateEntry.get(), ExpectedDateEntry.get(), QuantityEntry.get(), UnitCostEntry.get(),
            TotalPriceEntry.get(), StatusEntry.get(), SupplierIDEntry.get()
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Supplier updated successfully!")
        load_products_to_treeview(SuppliersTable)
    except Error as e:
        messagebox.showerror("Database Error", f"Failed to update supplier: {str(e)}")