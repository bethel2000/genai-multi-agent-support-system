import sqlite3

conn = sqlite3.connect("support.db")
cursor = conn.cursor()

# Create customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    account_type TEXT
)
""")

# Create tickets table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    issue TEXT,
    status TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
)
""")

# Insert dummy customers
customers = [
    ("Ema Johnson", "ema@gmail.com", "Premium"),
    ("Daniel Lee", "daniel@gmail.com", "Standard"),
    ("Sarah Ahmed", "sarah@gmail.com", "Premium"),
]

cursor.executemany("INSERT INTO customers (name, email, account_type) VALUES (?, ?, ?)", customers)

# Insert dummy tickets
tickets = [
    (1, "Refund not processed", "Resolved"),
    (1, "Login issue", "Open"),
    (2, "Account suspended", "Resolved"),
    (3, "Payment failure", "Open"),
]

cursor.executemany("INSERT INTO tickets (customer_id, issue, status) VALUES (?, ?, ?)", tickets)

conn.commit()
conn.close()

print("Database created successfully.")
