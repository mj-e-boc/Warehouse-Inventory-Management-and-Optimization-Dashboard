import pandas as pd

def clean_data(file_path):
    """Cleans the raw dataset."""
    # Read CSV file
    df = pd.read_csv(file_path)

    # Check for missing columns
    if "Product_ID" not in df.columns:
        print("Error: Missing Product_ID column")
        return None

    # Fill empty values
    if "Current_Stock_Level" in df.columns:
        df["Current_Stock_Level"].fillna(0, inplace=True)
    else:
        print("Error: Missing Current_Stock_Level column")
        return None

    # Fix Product_ID to integers
    df["Product_ID"] = pd.to_numeric(df["Product_ID"], errors="coerce").fillna(0).astype(int)

    # Handle NaN values
    df.fillna("Unknown", inplace=True)

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    return df