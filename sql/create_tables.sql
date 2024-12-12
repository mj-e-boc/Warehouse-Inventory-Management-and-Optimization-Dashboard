CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL,
    stock INTEGER NOT NULL,
    price_per_unit REAL NOT NULL,
    category TEXT,
    restock_date TEXT
);
