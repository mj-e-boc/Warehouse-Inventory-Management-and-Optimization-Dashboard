from datawrangling import clean_data
from sql.db_operations import create_tables, insert_data_to_db, execute_query
import matplotlib.pyplot as plt
import pandas as pd
import os

# File paths
RAW_DATA_PATH = "/Users/mjay/Desktop/Data science and Business Analytics/Python/Final project plan/Warehouse-Inventory-Management-and-Optimization-Dashboard/src/data/Warehouse_Inventory_Data.csv"
DB_PATH = "data/inventory.db"

# Step 1: Clean the dataset
print("Cleaning the dataset...")
cleaned_data = clean_data(RAW_DATA_PATH)
if cleaned_data is None or cleaned_data.empty:
    print("Error: No data found after cleaning. Exiting.")
    exit()
print(cleaned_data.head())

# Define column names and types for SQLite table
columns = [
    ("Product_ID", "INTEGER PRIMARY KEY"),
    ("Product_Name", "TEXT"),
    ("Category", "TEXT"),
    ("Current_Stock_Level", "INTEGER"),
    ("Reorder_Point", "INTEGER"),
    ("Lead_Time_Days", "INTEGER"),
    ("Storage_Location", "TEXT")
]

# Step 2: Set up SQLite database
print("Setting up the database...")
if not os.path.exists("data"):
    os.makedirs("data")  # Create the data directory if it doesn't exist
create_tables(DB_PATH, columns)

# Step 3: Insert cleaned data into the database
print("Inserting data into the database...")
insert_data_to_db(DB_PATH, cleaned_data)

# Step 4: Run SQL queries to fetch insights
print("Fetching insights...")
query = "SELECT * FROM inventory WHERE Current_Stock_Level < Reorder_Point;"
low_stock_items = execute_query(DB_PATH, query)

if low_stock_items.empty:
    print("No low stock items found.")
    exit()

print("Low stock items:")
print(low_stock_items)

# Data adjustments
low_stock_items["Product_Name"] = low_stock_items["Product_Name"].str.strip()
low_stock_items["Product_Name"].fillna("Unknown", inplace=True)

# Bar chart for low stock items
plt.figure(figsize=(12, 6))
plt.bar(low_stock_items["Product_Name"], low_stock_items["Current_Stock_Level"], color="blue")
plt.title("Low Stock Items")
plt.xlabel("Product Name")
plt.ylabel("Current Stock Level")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie chart for category distribution
category_counts = low_stock_items["Category"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(
    category_counts,
    labels=category_counts.index,
    autopct="%1.1f%%",
    colors=["red", "green", "blue", "orange", "purple"]
)
plt.title("Category Distribution")
plt.show()
