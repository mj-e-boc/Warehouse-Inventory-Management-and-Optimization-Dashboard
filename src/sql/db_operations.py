import sqlite3
import pandas as pd

# Ensure db_path points to the SQLite database file
db_path = "/Users/mjay/Desktop/Data science and Business Analytics/Python/Final project plan/Warehouse-Inventory-Management-and-Optimization-Dashboard/data/inventory.db"

def create_tables(db_path, columns):
    """
    Create a table in the SQLite database with the specified columns.

    Parameters:
    - db_path (str): Path to the SQLite database file.
    - columns (list of tuples): List of column names and types (e.g., [("id", "INTEGER"), ("name", "TEXT")]).
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS inventory (
        {", ".join([f"{col} {dtype}" for col, dtype in columns])}
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def insert_data_to_db(db_path, data):
    """
    Insert a pandas DataFrame into the SQLite database.

    Parameters:
    - db_path (str): Path to the SQLite database file.
    - data (pd.DataFrame): The data to be inserted into the database.
    """
    conn = sqlite3.connect(db_path)
    data.to_sql("inventory", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

def execute_query(db_path, query):
    """
    Execute a SQL query and return the result as a pandas DataFrame.

    Parameters:
    - db_path (str): Path to the SQLite database file.
    - query (str): The SQL query to execute.

    Returns:
    - pd.DataFrame: Query results.
    """
    conn = sqlite3.connect(db_path)
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result
