-- Fetch low stock items
SELECT * FROM inventory WHERE stock < 100;

-- Calculate total inventory value
SELECT SUM(stock * price_per_unit) AS total_value FROM inventory;

-- Count items by category
SELECT category, COUNT(*) AS total_items FROM inventory GROUP BY category;
