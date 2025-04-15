import psycopg2
import csv

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        phone VARCHAR(20) UNIQUE NOT NULL
    )
""")
conn.commit()

# --- 2.1 Insert from CSV file ---
def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
            except psycopg2.errors.UniqueViolation:
                conn.rollback()
                print(f"Phone number {row[1]} already exists.")
            else:
                conn.commit()

# --- 2.2 Insert from console ---
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print("This phone number already exists.")

# --- 3. Update data ---
def update_user(old_value, new_value, field='first_name'):
    if field not in ['first_name', 'phone']:
        print("Invalid field. Must be 'first_name' or 'phone'.")
        return
    cur.execute(f"UPDATE phonebook SET {field} = %s WHERE {field} = %s", (new_value, old_value))
    conn.commit()
    print(f"{cur.rowcount} record(s) updated.")

# --- 4. Querying data with filters ---
def search_user(name=None, phone=None):
    if name:
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", ('%' + name + '%',))
    elif phone:
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", ('%' + phone + '%',))
    else:
        cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# --- 5. Delete user by name or phone ---
def delete_user(value):
    cur.execute("DELETE FROM phonebook WHERE first_name = %s OR phone = %s", (value, value))
    conn.commit()
    print(f"{cur.rowcount} record(s) deleted.")

# --- Cleanup ---
def close():
    cur.close()
    conn.close()
