from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from mysql.connector import Error

def rawmaterials_form(app):
    rawmaterials_frame = Frame(app, width=1070, height=800, bg="white")
    rawmaterials_frame.place(x=250, y=110)

    heading_label = Label(rawmaterials_frame,
                          text="Raw materials",
                          font=("Times New Roman", 20, "bold"),
                          bg="#F1BA88",
                          fg = "#521C0D")
    heading_label.place(x=0, y=0, relwidth=1)

    # Frame chứa phần nội dung chính (frame trống)
    Rawmaterialframe = Frame(rawmaterials_frame, bd=15, relief="ridge", bg="#F4E7E1")
    Rawmaterialframe.place(x=20, y=250, width=980, height=290)  # Giả sử frame này là "trống"

    Scroll_x = ttk.Scrollbar(Rawmaterialframe, orient="horizontal")
    Scroll_y = ttk.Scrollbar(Rawmaterialframe, orient="vertical")
   
    Rawmaterialtable = ttk.Treeview(Rawmaterialframe, columns=("MaterialID", "MaterialName", "Unit", "quantity", "SupplierID", "Unit_Cost"), xscrollcommand = Scroll_x.set, yscrollcommand = Scroll_y.set)
    Scroll_x.pack(side=BOTTOM, fill=X) 
    Scroll_y.pack(side=RIGHT, fill=Y)

    Scroll_x.config(command=Rawmaterialtable.xview)
    Scroll_y.config(command=Rawmaterialtable.yview)

    Rawmaterialtable.heading("MaterialID", text="Material ID")
    Rawmaterialtable.heading("MaterialName", text="Material Name") 
    Rawmaterialtable.heading("Unit", text="Unit")
    Rawmaterialtable.heading("quantity", text="Quantity")
    Rawmaterialtable.heading("SupplierID", text="Supplier ID")
    Rawmaterialtable.heading("Unit_Cost", text="Unit Cost")
    Rawmaterialtable["show"] = "headings"  # Hiển thị tiêu đề cột

    Rawmaterialtable.pack(fill=BOTH, expand=True)  # Đặt Treeview vào frame trống

    load_products_to_treeview(Rawmaterialtable)

    # Frame chứa các nút, đặt ở góc trên của rawmaterialsandsuppliers_frame
    ButtonFrame = Frame(rawmaterials_frame, bg="white")
    ButtonFrame.place(x=200, y=50)  # Điều chỉnh x, y nếu cần căn chỉnh

    
    # Các nhãn và ô nhập liệu
    MaterialNameLabel = Label(ButtonFrame, text="Material Name", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg = "#521C0D")
    MaterialNameLabel.grid(row=3, column=0, padx=5, pady=5)
    MaterialNameEntry = Entry(ButtonFrame, font=("Times New Roman", 16), width=13, selectbackground="#F1BA88", bg="#F4E7E1", fg = "#521C0D")
    MaterialNameEntry.grid(row=3, column=1, padx=5, pady=2)

    UnitLabel = Label(ButtonFrame, text="Unit", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg = "#521C0D")
    UnitLabel.grid(row=4, column=0, padx=5, pady=8)
    UnitEntry = Entry(ButtonFrame, font=("Times New Roman", 16), width=13, selectbackground="#F1BA88", bg="#F4E7E1", fg = "#521C0D")
    UnitEntry.grid(row=4, column=1, padx=5, pady=8)

    UnitCostLabel = Label(ButtonFrame, text="Unit Cost", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg = "#521C0D")
    UnitCostLabel.grid(row=5, column=0, padx=5, pady=8)
    UnitCostEntry = Entry(ButtonFrame, font=("Times New Roman", 16), width=13, selectbackground="#F1BA88", bg="#F4E7E1", fg = "#521C0D")
    UnitCostEntry.grid(row=5, column=1, padx=5, pady=8)

    MaterialIDLabel = Label(ButtonFrame, text="Material ID", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg = "#521C0D")
    MaterialIDLabel.grid(row=3, column = 2, padx=5, pady=8)
    MaterialIDEntry = Entry(ButtonFrame, font=("Times New Roman", 16), width=13, selectbackground="#F1BA88", bg="#F4E7E1", fg = "#521C0D")
    MaterialIDEntry.grid(row=3, column=3, padx=5, pady=8)

    QuantityLabel = Label(ButtonFrame, text="Quantity", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg = "#521C0D")
    QuantityLabel.grid(row=4, column=2, padx=5, pady=8)
    QuantityLabelEntry = Entry(ButtonFrame, font=("Times New Roman", 16), width=13, selectbackground="#F1BA88", bg="#F4E7E1", fg = "#521C0D")
    QuantityLabelEntry.grid(row=4, column=3, padx=5, pady=8)

    SupplierIDLabel = Label(ButtonFrame, text="Supplier ID", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg = "#521C0D")
    SupplierIDLabel.grid(row=5, column=2, padx=5, pady=8)
    SupplierIDEntry = Entry(ButtonFrame, font=("Times New Roman", 16), width=13, selectbackground="#F1BA88", bg="#F4E7E1", fg = "#521C0D")
    SupplierIDEntry.grid(row=5, column=3, padx=5, pady=8)

    def handle_purchase_rawmaterial():
        purchase_rawmaterial(
            SupplierIDEntry.get(),
            MaterialIDEntry.get(),
            MaterialNameEntry.get(),
            UnitEntry.get(),
            QuantityLabelEntry.get(),
            UnitCostEntry.get(),
            Rawmaterialtable = Rawmaterialtable            
        )
        load_products_to_treeview(Rawmaterialtable)  # làm mới bảng

    PurchaseRMButton = Button(ButtonFrame, text="Purchase", font=("Times New Roman", 18, "bold"), fg="#521C0D", bg="#F1BA88", width=8, command = handle_purchase_rawmaterial )
    PurchaseRMButton.grid(row = 0, column = 1, pady=5)

    DeleteRMButton = Button(ButtonFrame, text="Delete", font=("Times New Roman", 18, "bold"), fg="#521C0D", bg="#F1BA88", width=8, command = lambda: delete_rawmaterial(Rawmaterialtable))
    DeleteRMButton.grid(row = 0, column = 2, padx = 10,  pady=5)

    UpdateRMButton = Button(
        ButtonFrame,
        text="Update",
        font=("Times New Roman", 18, "bold"),
        fg="#521C0D",
        bg="#F1BA88",
        width=8,
        command=lambda: update_rawmaterial(
            MaterialIDEntry,
            MaterialNameEntry,
            UnitEntry,
            QuantityLabelEntry,
            SupplierIDEntry,
            UnitCostEntry,
            Rawmaterialtable
        )
    )
    UpdateRMButton.grid(row=0, column=3, padx=10, pady=5)

    load_products_to_treeview(Rawmaterialtable)
#========================================================================Functions for buttons============================================================================
    
def connect_database():
    # Replace with your actual database connection details
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="nguyenhue",
        database="manufacturing_process"
    )

def load_products_to_treeview(Rawmaterialtable):
    # Xóa dữ liệu cũ (nếu có)
    for item in Rawmaterialtable.get_children():
        Rawmaterialtable.delete(item)

    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT MaterialID, MaterialName, Unit, quantity, SupplierID, Unit_Cost FROM material_with_suppliers")
        rows = cursor.fetchall()

        for row in rows:
            Rawmaterialtable.insert("", "end", values=row)

        conn.close()
    except Exception as err:
        messagebox.showerror("Database Error", f"Failed to load data: {err}")

def purchase_rawmaterial(SupplierID, MaterialID, MaterialName, Unit, quantity, Unit_Cost, Rawmaterialtable):
    if MaterialID == "" or MaterialName == "" or Unit == "" or quantity == "" or SupplierID == "" or Unit_Cost == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        qty = int(quantity)
        unit_cost = float(Unit_Cost)
    except ValueError:
        messagebox.showerror("Error", "Quantity and Unit Cost must be numbers")
        return

    try:
        conn = connect_database()
        cursor = conn.cursor()
        # Check if material already exists
        cursor.execute("SELECT quantity FROM material_with_suppliers WHERE MaterialID = %s", (MaterialID,))
        result = cursor.fetchone()

        if result:
            # Material exists, update quantity
            new_quantity = result[0] + qty
            cursor.execute("""
                UPDATE material_with_suppliers
                SET quantity = %s, MaterialName = %s, Unit = %s, SupplierID = %s, Unit_Cost = %s
                WHERE MaterialID = %s
            """, (new_quantity, MaterialName, Unit, SupplierID, unit_cost, MaterialID))
        else:
            # Material does not exist, insert new
            cursor.execute("""
                INSERT INTO material_with_suppliers (MaterialID, MaterialName, Unit, quantity, SupplierID, Unit_Cost)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (MaterialID, MaterialName, Unit, qty, SupplierID, unit_cost))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Material {MaterialID} purchased successfully! Quantity added: {qty}")
        load_products_to_treeview(Rawmaterialtable)
    except Exception as e:
        messagebox.showerror("Database Error", f"Failed to purchase raw materials: {str(e)}")

def delete_rawmaterial(treeview):
    selected_item = treeview.focus()
    if not selected_item:
        messagebox.showerror("Error", "Please select a raw material to delete.")
        return

    values = treeview.item(selected_item, "values")
    material_id = values[0]  # cột material ID

    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete this material with ID: {material_id}?")
    if not confirm:
        return

    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM material_with_suppliers WHERE MaterialID = %s", (material_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Material {material_id} deleted successfully!")
        load_products_to_treeview(treeview)
    except Error as e:
        messagebox.showerror("Database Error", f"Failed to delete material: {str(e)}")

def update_rawmaterial(MaterialIDEntry, MaterialNameEntry, UnitEntry, QuantityLabelEntry, SupplierIDEntry, UnitCostEntry ,Rawmaterialtable):
    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE material_with_suppliers
            SET MaterialName=%s, Unit=%s, quantity=%s, SupplierID=%s, Unit_Cost=%s
            WHERE MaterialID=%s
        """, (
            MaterialNameEntry.get(),
            UnitEntry.get(),
            QuantityLabelEntry.get(),
            SupplierIDEntry.get(),
            UnitCostEntry.get(),
            MaterialIDEntry.get()
            ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Material updated successfully!")
        load_products_to_treeview(Rawmaterialtable)
    except Error as e:
        messagebox.showerror("Database Error", f"Failed to update material: {str(e)}")