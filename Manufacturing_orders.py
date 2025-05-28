from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from mysql.connector import Error

def manufacturing_orders(app):
    manufacturing_orders_frame = Frame(app, width=1070, height=800, bg="white")
    manufacturing_orders_frame.place(x=250, y=110)

    ordersframe = Frame(manufacturing_orders_frame, bd=5, relief="groove", bg="#FFFFFF")
    ordersframe.place(x=20, y=20, width=980, height=250)  

    createorders_label = Label(ordersframe, text="Create Manufacturing Orders", font=("Times New Roman", 20, "bold"), fg="#521C0D", bg = "#ffffff", anchor = "w")
    createorders_label.place(x=0, y=0, relwidth=1)

    OrderIDlabel = Label(ordersframe, text="Order ID", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    OrderIDlabel.place(x=10, y=40)
    OrderIDEntry = Entry(ordersframe, font=("Times New Roman", 16, "bold"), width=15, bg="#F4E7E1", fg="#521C0D")
    OrderIDEntry.place(x=150, y=40)

    ProductIDlabel = Label(ordersframe, text="Product ID", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    ProductIDlabel.place(x=10, y=80)
    ProductIDEntry = Entry(ordersframe, font=("Times New Roman", 16, "bold"), width=15, bg="#F4E7E1", fg="#521C0D")
    ProductIDEntry.place(x=150, y=80)

    CategoryIDlabel = Label(ordersframe, text="Category ID", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    CategoryIDlabel.place(x=10, y=120)
    CategoryIDEntry = Entry(ordersframe, font=("Times New Roman", 16, "bold"), width=15, bg="#F4E7E1", fg="#521C0D")
    CategoryIDEntry.place(x=150, y=120)

    Quantitylabel = Label(ordersframe, text="Quantity", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    Quantitylabel.place(x=330, y=40)
    QuantityEntry = Entry(ordersframe, font=("Times New Roman", 16, "bold"), width=15, bg="#F4E7E1", fg="#521C0D")
    QuantityEntry.place(x=425, y=40)

    Statuslabel = Label(ordersframe, text="Status", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    Statuslabel.place(x=330, y=80)
    StatusEntry = Entry(ordersframe, font=("Times New Roman", 16, "bold"), width=15, bg="#F4E7E1", fg="#521C0D")
    StatusEntry.place(x=425, y=80)

    PlantIDlabel = Label(ordersframe, text="Plant ID", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    PlantIDlabel.place(x=330, y=120)
    PlantIDEntry = Entry(ordersframe, font=("Times New Roman", 16, "bold"), width=15, bg="#F4E7E1", fg="#521C0D")
    PlantIDEntry.place(x=425, y=120)

    StartDateLabel = Label(ordersframe, text="Start Date", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    StartDateLabel.place(x=600, y=40)
    StartDateEntry = Entry(ordersframe, font=("Times New Roman", 16, "bold"), width=15, bg="#F4E7E1", fg="#521C0D")
    StartDateEntry.place(x=780, y=40)

    Expected_EndDateLabel = Label(ordersframe, text="Expected End Date", font=("Times New Roman", 16, "bold"), bg="#FFFFFF", fg="#521C0D")
    Expected_EndDateLabel.place(x=600, y=80)
    Expected_EndDateEntry = Entry(ordersframe, font=("Times New Roman", 16, "bold"), width=15, bg="#F4E7E1", fg="#521C0D")
    Expected_EndDateEntry.place(x=780, y=80)

    def handle_create_order():
        create_order(
        OrderID = OrderIDEntry.get(),
        ProductID = ProductIDEntry.get(),
        CategoryID = CategoryIDEntry.get(),
        PlantID = PlantIDEntry.get(),
        Quantity = QuantityEntry.get(),
        StartDate = StartDateEntry.get(),
        Expected_EndDate = Expected_EndDateEntry.get(),
        Status = StatusEntry.get(),
        OrdersTable=OrdersTable
        )
        load_products_to_treeview(OrdersTable)  # làm mới bảng

    CreateOrderButton = Button(ordersframe, text="Create", font=("Times New Roman", 16, "bold"), fg="#521C0D", bg="#F1BA88", width=10, command = handle_create_order)
    CreateOrderButton.place(x=20, y=170)

    UpdateOrderButton = Button(
        ordersframe,
        text="Update",
        font=("Times New Roman", 16, "bold"),
        fg="#521C0D",
        bg="#F1BA88",
        width=10,
        command=lambda: update_order(
            OrderIDEntry,
            ProductIDEntry,
            CategoryIDEntry,
            PlantIDEntry,
            QuantityEntry,
            StartDateEntry,
            Expected_EndDateEntry,
            StatusEntry,
            OrdersTable
        )
    )
    UpdateOrderButton.place(x=220, y=170)

    SearchOrderButton = Button(ordersframe, text="Search", font=("Times New Roman", 16, "bold"), fg="#521C0D", bg="#F1BA88", width=10, command=lambda: search_orders(OrderIDEntry, ProductIDEntry, CategoryIDEntry, PlantIDEntry, QuantityEntry, StartDateEntry, Expected_EndDateEntry, StatusEntry, OrdersTable))
    SearchOrderButton.place(x=400, y=170)
    SearchOrderButton.place(x=400, y=170)

    DeleteOrderButton = Button(ordersframe, text="Delete", font=("Times New Roman", 16, "bold"), fg="#521C0D", bg="#F1BA88", width=10, command = lambda:delete_order(OrdersTable))
    DeleteOrderButton.place(x=580, y=170)

    ShowAllButton = Button(ordersframe, text="Show All", font=("Times New Roman", 16, "bold"), fg="#521C0D", bg="#F1BA88", width=10, command=lambda: load_products_to_treeview(OrdersTable))
    ShowAllButton.place(x=790, y=120)

    ProcessOrderButton = Button(ordersframe, text="Process Order", font=("Times New Roman", 16, "bold"), fg="#521C0D", bg="#F1BA88", width=15, command=lambda: process_order(OrdersTable))
    ProcessOrderButton.place(x=760, y=170)
#====================================================================Tạo Treeview cho Orders====================================================================
    Orderlist_frame = Frame(manufacturing_orders_frame, bd=5, relief="ridge", bg="#FFFFFF")
    Orderlist_frame.place(x=20, y=300, width=980, height=250)  # Giả sử frame này là "trống"
    
    Scroll_x = ttk.Scrollbar(Orderlist_frame, orient="horizontal")
    Scroll_y = ttk.Scrollbar(Orderlist_frame, orient="vertical")
    
    OrdersTable = ttk.Treeview(Orderlist_frame, columns=("OrderID", "ProductID", "CategoryID", "PlantID", "Quantity", "StartDate", "Expected_EndDate", "Status"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
    Scroll_x.pack(side=BOTTOM, fill=X)
    Scroll_y.pack(side=RIGHT, fill=Y)
    
    Scroll_x.config(command=OrdersTable.xview)
    Scroll_y.config(command=OrdersTable.yview)

    OrdersTable.heading("OrderID", text="Order ID")
    OrdersTable.heading("ProductID", text="Product ID")
    OrdersTable.heading("CategoryID", text="Category ID")
    OrdersTable.heading("PlantID", text="Plant ID")
    OrdersTable.heading("Quantity", text="Quantity")
    OrdersTable.heading("StartDate", text="Start Date")
    OrdersTable.heading("Expected_EndDate", text="Expected End Date")
    OrdersTable.heading("Status", text="Status")
    OrdersTable["show"] = "headings"  # Hiển thị tiêu đề cột
    OrdersTable.pack(fill=BOTH, expand=True)  # Đặt Treeview vào frame trống

    load_products_to_treeview(OrdersTable)

def connect_database():
    # Replace with your actual database connection details
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="nguyenhue",
        database="manufacturing_process"
    )

def load_products_to_treeview(OrdersTable):
    # Xóa dữ liệu cũ (nếu có)
    for item in OrdersTable.get_children():
        OrdersTable.delete(item)

    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT OrderID, ProductID, CategoryID, PlantID, Quantity, StartDate, Expected_EndDate, Status FROM orders")
        rows = cursor.fetchall()

        for row in rows:
            OrdersTable.insert("", "end", values=row)

        conn.close()
    except Exception as err:
        messagebox.showerror("Database Error", f"Failed to load data: {err}")

def create_order(OrderID, ProductID, CategoryID, PlantID, Quantity, StartDate, Expected_EndDate, Status, OrdersTable):
    if OrderID == "" or ProductID == "" or CategoryID == "" or PlantID == "" or Quantity == "" or StartDate == "" or Expected_EndDate == "" or Status == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        qty = int(Quantity)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be a number")
        return

    # Force status to "In Progress" when creating an order
    Status = "In Progress"

    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO orders (OrderID, ProductID, CategoryID, PlantID, Quantity, StartDate, Expected_EndDate, Status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (OrderID, ProductID, CategoryID, PlantID, qty, StartDate, Expected_EndDate, Status))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Manufacturing order created successfully!")
        load_products_to_treeview(OrdersTable)  # Refresh Treeview to show the new order
    except Exception as e:
        messagebox.showerror("Database Error", f"Failed to create manufacturing order: {str(e)}")

def process_order(treeview):
    selected_item = treeview.focus()
    if not selected_item:
        messagebox.showerror("Error", "Please select an order to process.")
        return

    values = treeview.item(selected_item, "values")
    order_id = values[0]
    product_id = values[1]
    quantity = int(values[4])

    try:
        conn = connect_database()
        cursor = conn.cursor()
        # Check current stock
        cursor.execute("SELECT StockQuantity FROM products WHERE ProductID = %s", (product_id,))
        result = cursor.fetchone()
        if result and result[0] >= quantity:
            # Deduct stock and update order status
            cursor.execute("UPDATE products SET StockQuantity = StockQuantity - %s WHERE ProductID = %s", (quantity, product_id))
            cursor.execute("UPDATE orders SET Status = %s WHERE OrderID = %s", ("Done", order_id))
            conn.commit()
            messagebox.showinfo("Success", f"Order {order_id} processed successfully. Stock updated.")
        else:
            # Insufficient stock, prompt to manufacture more
            stock_available = result[0] if result else 0
            messagebox.showwarning(
                "Insufficient Stock", f"Not enough {product_id} in stock. Current stock: {stock_available}. Required: {quantity}. Please manufacture more products in the Products Catalog tab.")
        
        conn.close()
        load_products_to_treeview(treeview)
    except Exception as e:
        messagebox.showerror("Database Error", f"Failed to process order: {str(e)}")

def delete_order(treeview):
    selected_item = treeview.focus()
    if not selected_item:
        messagebox.showerror("Error", "Please select a manufacturing order to delete.")
        return

    values = treeview.item(selected_item, "values")
    order_id = values[0]

    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete this order with ID: {order_id}?")
    if not confirm:
        return

    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM orders WHERE OrderID = %s", (order_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Manufacturing order {order_id} deleted successfully!")
        load_products_to_treeview(treeview)
    except Error as e:
        messagebox.showerror("Database Error", f"Failed to delete manufacturing order: {str(e)}")

def update_order(OrderIDEntry, ProductIDEntry, CategoryIDEntry, PlantIDEntry, QuantityEntry, StartDateEntry, Expected_EndDateEntry, StatusEntry, OrdersTable):
    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE orders
            SET ProductID=%s, CategoryID=%s, PlantID=%s, Quantity=%s, StartDate=%s, Expected_EndDate=%s, Status=%s
            WHERE OrderID = %s
        """, (
            ProductIDEntry.get(),
            CategoryIDEntry.get(),
            PlantIDEntry.get(),
            QuantityEntry.get(),
            StartDateEntry.get(),
            Expected_EndDateEntry.get(),
            StatusEntry.get(),
            OrderIDEntry.get(),
            ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Order updated successfully!")
        load_products_to_treeview(OrdersTable)
    except Error as e:
        messagebox.showerror("Database Error", f"Failed to update order: {str(e)}")

def search_orders(OrderIDEntry, ProductIDEntry, CategoryIDEntry, PlantIDEntry, QuantityEntry, StartDateEntry, Expected_EndDateEntry, StatusEntry, OrdersTable):
    """Search for orders based on the values entered in the fields"""
    
    # Get search criteria from entry fields
    search_criteria = {
        'OrderID': OrderIDEntry.get().strip(),
        'ProductID': ProductIDEntry.get().strip(),
        'CategoryID': CategoryIDEntry.get().strip(),
        'PlantID': PlantIDEntry.get().strip(),
        'Quantity': QuantityEntry.get().strip(),
        'StartDate': StartDateEntry.get().strip(),
        'Expected_EndDate': Expected_EndDateEntry.get().strip(),
        'Status': StatusEntry.get().strip()
    }
    
    # Remove empty search criteria
    active_criteria = {key: value for key, value in search_criteria.items() if value}
    
    if not active_criteria:
        messagebox.showinfo("Search", "Please enter at least one search criterion.")
        return
    
    try:
        conn = connect_database()
        cursor = conn.cursor()
        
        # Build dynamic WHERE clause
        where_conditions = []
        search_values = []
        
        for field, value in active_criteria.items():
            if field in ['StartDate', 'Expected_EndDate']:
                # For date fields, use exact match or partial match
                where_conditions.append(f"{field} LIKE %s")
                search_values.append(f"%{value}%")
            else:
                # For other fields, use LIKE for partial matching
                where_conditions.append(f"{field} LIKE %s")
                search_values.append(f"%{value}%")
        
        where_clause = " AND ".join(where_conditions)
        
        query = f"""
            SELECT OrderID, ProductID, CategoryID, PlantID, Quantity, StartDate, Expected_EndDate, Status 
            FROM orders 
            WHERE {where_clause}
        """
        
        print(f"Search query: {query}")
        print(f"Search values: {search_values}")
        
        cursor.execute(query, search_values)
        rows = cursor.fetchall()
        
        # Clear existing data in treeview
        for item in OrdersTable.get_children():
            OrdersTable.delete(item)
        
        # Insert search results
        for row in rows:
            OrdersTable.insert("", "end", values=row)
        
        conn.close()
        
        # Show search results count
        result_count = len(rows)
        if result_count == 0:
            messagebox.showinfo("Search Results", "No orders found matching the search criteria.")
        else:
            messagebox.showinfo("Search Results", f"Found {result_count} order(s) matching the search criteria.")
            
    except Error as e:
        messagebox.showerror("Database Error", f"Failed to search orders: {str(e)}")
    except Exception as e:
        messagebox.showerror("Unexpected Error", f"An unexpected error occurred during search: {str(e)}")