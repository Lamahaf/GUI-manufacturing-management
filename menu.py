from tkinter import *
from Raw_materials import rawmaterials_form
from Manufacturing_orders import manufacturing_orders
from Products_catalog import productscatalog_form
from Suppliers import suppliers_form
from BOM import bom_form
from mysql.connector import Error
import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from datetime import datetime
import io
import uuid

# Initialize Tkinter application
app = Tk()
app.title("Manufacturing Interface")
app.geometry("1270x668+0+0")
app.configure(bg="white")
app.resizable(False, False)

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nguyenhue",
    database="manufacturing_process"
)
cursor = mydb.cursor()

menu_frame = Frame(app, width=1070, height=800, bg="#F0B899")
menu_frame.place(x=250, y=110)

heading_label = Label(menu_frame,
                          text="Main Menu",
                          font=("Times New Roman", 20, "bold"),
                          bg="#F1BA88",
                          fg = "#521C0D")
heading_label.place(x=0, y=0, relwidth=1)

infographicImage = PhotoImage(file="images/infographic.png")
imagelabel = Label(menu_frame, image = infographicImage)
imagelabel.place(x=40, y=60)

# UI elements
titlelabel = Label(app, compound="right", text="Manufacturing management", font=("Times New Roman", 50, "bold"), bg="#d5451b", fg="white", anchor="center", padx=0)
titlelabel.place(x=0, y=0, relwidth=1, height=110)

leftFrame = Frame(app, bg="#F4E7E1")
leftFrame.place(x=0, y=110, width=250, height=560)

logoImage = PhotoImage(file="images/logo.png")
imagelabel = Label(leftFrame, image=logoImage)
imagelabel.pack()

Dashboard_button = Button(leftFrame, text="Dashboard report", font=("Times New Roman", 20, "bold"), fg="#FFFFFF", bg="#d5451b", pady=8, command=lambda: dashboard_form(app))
Dashboard_button.pack(fill=X)

ManufacturingOrders_button = Button(leftFrame, text="Manufacturing Orders", compound="left", font=("Times New Roman", 18, "bold"), fg="#521C0D", bg="#F1BA88", pady=8, command=lambda: manufacturing_orders(app))
ManufacturingOrders_button.pack(fill=X)

ProductsCatalog_button = Button(leftFrame, text="Products Catalog", compound="left", font=("Times New Roman", 18, "bold"), fg="#521C0D", bg="#F1BA88", pady=8, command=lambda: productscatalog_form(app))
ProductsCatalog_button.pack(fill=X)

Rawmaterial_button = Button(leftFrame, text="Raw materials", compound="left", font=("Times New Roman", 18, "bold"), fg="#521C0D", bg="#F1BA88", pady=8, command=lambda: rawmaterials_form(app))
Rawmaterial_button.pack(fill=X)

Suppliers_button = Button(leftFrame, text="Suppliers", compound="left", font=("Times New Roman", 18, "bold"), fg="#521C0D", bg="#F1BA88", pady=8, command=lambda: suppliers_form(app))
Suppliers_button.pack(fill=X)

bom_button = Button(app, text="BOM", compound="bottom", font=("Times New Roman", 18, "bold"), fg="#521C0D", bg="#F1BA88", command=lambda: bom_form(app))
bom_button.place(x=1150, y=600, width=100, height=50)


def dashboard_form(app):
    # Clear previous content
    for widget in app.winfo_children():
        if widget != titlelabel and widget != leftFrame and widget != bom_button:
            widget.destroy()

    # Create dashboard frame
    dashboard_frame = Frame(app, bg="white")
    dashboard_frame.place(x=250, y=110, width=1020, height=558)

    # Load CSV files
    orders_df = pd.read_csv("orders.csv")
    products_df = pd.read_csv("products.csv")
    materials_df = pd.read_csv("material_with_suppliers.csv")

    # Parse dates in orders_df using pandas.to_datetime
    orders_df['StartDate'] = pd.to_datetime(orders_df['StartDate'], format='%m/%d/%Y %H:%M', errors='coerce')
    orders_df['Real_EndDate'] = pd.to_datetime(orders_df['Real_EndDate'], format='%m/%d/%Y %H:%M', errors='coerce')

    # Set Seaborn style
    sns.set_style("whitegrid")

    # Plot 1: Monthly Production (Completed Orders)
    completed_orders = orders_df[orders_df['Status'] == 'Done'].copy()
    completed_orders['Month'] = completed_orders['Real_EndDate'].apply(lambda x: x.strftime('%Y-%m') if pd.notnull(x) else None)
    monthly_counts = completed_orders.groupby('Month').size().reset_index(name='OrderCount')

    plt.figure(figsize=(8, 4))
    sns.barplot(data=monthly_counts, x='Month', y='OrderCount', palette='viridis')
    plt.title('Monthly Completed Orders')
    plt.xlabel('Month')
    plt.ylabel('Number of Orders')
    plt.xticks(rotation=45)
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    img1 = Image.open(buf)
    img1 = ImageTk.PhotoImage(img1.resize((450, 250)))
    label1 = Label(dashboard_frame, image=img1, bg="white")
    label1.image = img1  # Keep a reference
    label1.place(x=20, y=20)

    # Plot 2: Stock Quantity by Category
    stock_by_category = products_df.groupby('CategoryID')['StockQuantity'].sum().reset_index()
    plt.figure(figsize=(8, 4))
    sns.barplot(data=stock_by_category, x='CategoryID', y='StockQuantity', palette='magma')
    plt.title('Stock Quantity by Product Category')
    plt.xlabel('Category ID')
    plt.ylabel('Total Stock Quantity')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    img2 = Image.open(buf)
    img2 = ImageTk.PhotoImage(img2.resize((450, 250)))
    label2 = Label(dashboard_frame, image=img2, bg="white")
    label2.image = img2  # Keep a reference
    label2.place(x=550, y=20)

    # Plot 3: Material Cost Distribution
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=materials_df, y='Unit_Cost', palette='coolwarm')
    plt.title('Material Unit Cost Distribution')
    plt.ylabel('Unit Cost ($)')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    img3 = Image.open(buf)
    img3 = ImageTk.PhotoImage(img3.resize((450, 250)))
    label3 = Label(dashboard_frame, image=img3, bg="white")
    label3.image = img3  # Keep a reference
    label3.place(x=20, y=300)

    # Plot 4: Order Status Distribution
    status_counts = orders_df['Status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']
    plt.figure(figsize=(8, 4))
    sns.set_palette('Set2')
    plt.pie(status_counts['Count'], labels=status_counts['Status'], autopct='%1.1f%%', startangle=140)
    plt.title('Order Status Distribution')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    img4 = Image.open(buf)
    img4 = ImageTk.PhotoImage(img4.resize((450, 250)))
    label4 = Label(dashboard_frame, image=img4, bg="white")
    label4.image = img4  # Keep a reference
    label4.place(x=550, y=300)

app.mainloop()