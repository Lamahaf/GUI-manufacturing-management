from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

def productscatalog_form(app):
    productscatalog_frame = Frame(app, width=1070, height=800, bg="white")
    productscatalog_frame.place(x=250, y=110)

    heading_label = Label(productscatalog_frame,
                          text="Products Catalog",
                          font=("Times New Roman", 20, "bold"),
                          bg="#F1BA88",
                          fg = "#521C0D")
    heading_label.place(x=0, y=0, relwidth=1)

    # Frame chứa phần nội dung chính (frame trống)
    Productframe = Frame(productscatalog_frame, bd=15, relief="ridge", bg="#F4E7E1")
    Productframe.place(x=20, y=260, width=980, height=270)  # Giả sử frame này là "trống"

    Scroll_x = ttk.Scrollbar(Productframe, orient="horizontal")
    Scroll_y = ttk.Scrollbar(Productframe, orient="vertical")
    Producttable = ttk.Treeview(Productframe, columns=("ProductID", "ProductName", "CategoryID", "Description", "UnitPrice", "StockQuantity"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)

    Scroll_x.pack(side=BOTTOM, fill=X)
    Scroll_y.pack(side=RIGHT, fill=Y)

    Scroll_x.config(command=Producttable.xview)
    Scroll_y.config(command=Producttable.yview)

    Producttable.heading("ProductID", text="Product ID")
    Producttable.heading("ProductName", text="Product Name")
    Producttable.heading("CategoryID", text="Category ID")
    Producttable.heading("Description", text="Description")
    Producttable.heading("UnitPrice", text="Unit Price")
    Producttable.heading("StockQuantity", text="Quantity")

    Producttable.column("Description", width=400)  # Điều chỉnh độ rộng cột mô tả
    Producttable["show"] = "headings"  # Hiển thị tiêu đề cột
    Producttable.pack(fill=BOTH, expand=True)  # Đặt Treeview vào frame trống

    # Load products into the Treeview after it is created
    load_products_to_treeview(Producttable)

    # Frame chứa các nút, đặt ở góc trên của productscatalog_frame

    ButtonFrame = Frame(productscatalog_frame, bg="white")
    ButtonFrame.place(x=50, y=50)  # Điều chỉnh x, y nếu cần căn chỉnh

                                                
    ProductIDlabel = Label(ButtonFrame, text="Product ID", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    ProductIDlabel.grid(row=1, column=0, padx=5, pady=5)
    ProductIDentry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=20, bg="#F4E7E1", fg="#521C0D")
    ProductIDentry.grid(row=1, column=1, padx=5, pady=5)

    ProductNamelabel = Label(ButtonFrame, text="Product Name", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    ProductNamelabel.grid(row=2, column=0, padx=5, pady=5)
    ProductNameentry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=20, bg="#F4E7E1", fg="#521C0D")
    ProductNameentry.grid(row=2, column=1, padx=5, pady=5)

    CategoryIDlabel = Label(ButtonFrame, text="Category ID", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    CategoryIDlabel.grid(row=3, column=0, padx=5, pady=5)
    CategoryIDentry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=20, bg="#F4E7E1", fg="#521C0D")
    CategoryIDentry.grid(row=3, column=1, padx=5, pady=5)

    UnitPricelabel = Label(ButtonFrame, text="Unit Price", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    UnitPricelabel.grid(row=1, column=2, padx=5, pady=5)
    UnitPriceentry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=20, bg="#F4E7E1", fg="#521C0D")
    UnitPriceentry.grid(row=1, column=3, padx=5, pady=5)

    Descriptionlabel = Label(ButtonFrame, text="Description", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    Descriptionlabel.grid(row=2, column=2, padx=5, pady=5)
    Descriptionentry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=20, bg="#F4E7E1", fg="#521C0D")
    Descriptionentry.grid(row=2, column=3, padx=5, pady=5)
    
    StockQuantitylabel = Label(ButtonFrame, text="Quantity", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    StockQuantitylabel.grid(row=3, column=2, padx=5, pady=5)
    StockQuantityentry = Entry(ButtonFrame, font=("Times New Roman", 16, "bold"), width=20, bg="#F4E7E1", fg="#521C0D")
    StockQuantityentry.grid(row=3, column=3, padx=5, pady=5)

    def handle_manufacture_product():
        manufacture_product(
        ProductID = ProductIDentry.get(),
        ProductName = ProductNameentry.get(),
        CategoryID = CategoryIDentry.get(),
        Description = Descriptionentry.get(),
        UnitPrice = UnitPriceentry.get(),
        StockQuantity = StockQuantityentry.get(),
        Producttable=Producttable
        )
        load_products_to_treeview(Producttable)  # làm mới bảng

    ManufactureButton = Button(ButtonFrame, text="Manufacture", font=("Times New Roman", 18, "bold"), fg="#521C0D", bg="#F1BA88", width=11, command=handle_manufacture_product)
    ManufactureButton.grid(row=0, column=1, padx=5, pady=5)

    DeleteButton = Button(ButtonFrame, text="Delete", font=("Times New Roman", 18, "bold"), fg="#521C0D", bg="#F1BA88", width=8, command = lambda: delete_product(Producttable))
    DeleteButton.grid(row=0, column=2, padx=5, pady=5)

    UpdateProductButton = Button(
        ButtonFrame,
        text="Update",
        font=("Times New Roman", 18, "bold"),
        fg="#521C0D",
        bg="#F1BA88",
        width=8,
        command=lambda: update_product(
            ProductIDentry,
            ProductNameentry,
            CategoryIDentry,
            Descriptionentry,
            UnitPriceentry,
            StockQuantityentry,
            Producttable
        )
    )
    UpdateProductButton.grid(row=0, column=3, padx=5, pady=5)

    # Load products into the Treeview after it is created
    load_products_to_treeview(Producttable)

def connect_database():
    # Replace with your actual database connection details
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="nguyenhue",
        database="manufacturing_process"
    )

def load_products_to_treeview(Producttable):
    # Xóa dữ liệu cũ (nếu có)
    for item in Producttable.get_children():
        Producttable.delete(item)

    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT ProductID, ProductName, CategoryID, Description, UnitPrice, StockQuantity FROM products")
        rows = cursor.fetchall()

        for row in rows:
            Producttable.insert("", "end", values=row)

        conn.close()
    except Exception as err:
        messagebox.showerror("Database Error", f"Failed to load data: {err}")

def manufacture_product(ProductID, ProductName, CategoryID, Description, UnitPrice, StockQuantity, Producttable):
    if ProductID == "" or ProductName == "" or CategoryID == "" or Description == "" or UnitPrice == "" or StockQuantity == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        stock_qty = int(StockQuantity)
        unit_price = float(UnitPrice)
    except ValueError:
        messagebox.showerror("Error", "Quantity and Unit Price must be numbers")
        return

    try:
        conn = connect_database()
        cursor = conn.cursor()

        # Check if product already exists
        cursor.execute("SELECT StockQuantity FROM products WHERE ProductID = %s", (ProductID,))
        result = cursor.fetchone()

        # Check raw materials availability via BOM
        cursor.execute("SELECT MaterialID, QuantityNeeded FROM bom WHERE ProductID = %s", (ProductID,))
        bom_rows = cursor.fetchall()

        if not bom_rows:
            messagebox.showerror("Error", f"No bill of materials found for product {ProductID}.")
            conn.close()
            return

        can_manufacture = True
        materials_needed = []
        for material_id, qty_needed in bom_rows:
            total_needed = qty_needed * stock_qty
            cursor.execute("SELECT quantity FROM material_with_suppliers WHERE MaterialID = %s", (material_id,))
            material_result = cursor.fetchone()
            if material_result and material_result[0] >= total_needed:
                materials_needed.append((material_id, total_needed))
            else:
                can_manufacture = False
                available = material_result[0] if material_result else 0
                messagebox.showwarning("Insufficient Materials", f"Not enough {material_id}. Available: {available}, Needed: {total_needed}.")
                break

        if can_manufacture:
            # Deduct raw materials
            for material_id, total_needed in materials_needed:
                cursor.execute("UPDATE material_with_suppliers SET quantity = quantity - %s WHERE MaterialID = %s", (total_needed, material_id))

            # Update or insert product
            if result:
                # Product exists, update stock
                new_stock = result[0] + stock_qty
                cursor.execute("""
                    UPDATE products
                    SET StockQuantity = %s, ProductName = %s, CategoryID = %s, Description = %s, UnitPrice = %s
                    WHERE ProductID = %s
                """, (new_stock, ProductName, CategoryID, Description, unit_price, ProductID))
            else:
                # Product does not exist, insert new
                cursor.execute("""
                    INSERT INTO products (ProductID, ProductName, CategoryID, Description, UnitPrice, StockQuantity)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (ProductID, ProductName, CategoryID, Description, unit_price, stock_qty))

            conn.commit()
            messagebox.showinfo("Success", f"Successfully manufactured {stock_qty} units of {ProductID}.")
            load_products_to_treeview(Producttable)
        else:
            messagebox.showinfo("Action Required", "Please purchase raw materials from the Raw Materials tab.")

        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Failed to manufacture product: {str(e)}")

def delete_product(treeview):
    selected_item = treeview.focus()
    if not selected_item:
        messagebox.showerror("Error", "Please select a product to delete.")
        return

    values = treeview.item(selected_item, "values")
    product_id = values[0]  # cột material ID

    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete this product with ID: {product_id}?")
    if not confirm:
        return

    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE ProductID = %s", (product_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Product {product_id} deleted successfully!")
        load_products_to_treeview(treeview)
    except Error as e:
        messagebox.showerror("Database Error", f"Failed to delete product: {str(e)}")

def update_product(ProductIDentry, ProductNameentry, CategoryIDentry, Descriptionentry, UnitPriceentry, StockQuantityentry, Producttable):
    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE products
            SET ProductName=%s, CategoryID=%s, Description=%s, UnitPrice=%s, StockQuantity=%s
            WHERE ProductID=%s
        """,(
            ProductNameentry.get(),
            CategoryIDentry.get(),
            Descriptionentry.get(),
            UnitPriceentry.get(),
            StockQuantityentry.get(),
            ProductIDentry.get()
            ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Product updated successfully!")
        load_products_to_treeview(Producttable)
    except Error as e:
        messagebox.showerror("Database Error", f"Failed to update product: {str(e)}")
