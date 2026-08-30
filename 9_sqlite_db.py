import sqlite3

# connect/create sqlite Database
conn = sqlite3.connect("shop.db")

# create cursor
cursor = conn.cursor()
print('1. DB is ready!')

# create table
cursor.execute(""" 
  CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
    )
""")
print('2. Table created')

products = [
    ("masala chai", 10),
    ("kachodi", 15),
    ("maggii", 20)
  ]

# insert data
cursor.executemany(
  "INSERT INTO products (name, price) VALUES (?, ?)",
  products
)
print(f"3. Products Added: {len(products)}")

# select data
cursor.execute("SELECT * FROM products WHERE price = 15")
rows = cursor.fetchall()

print('4. Fetching Products')
for row in range(len(rows)):
  print(f" {row}: {rows[row]}")

conn.close()
print('5. Databse closed')
