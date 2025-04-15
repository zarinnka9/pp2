import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 1. Создаём таблицу
def create_table():
    cur.execute("DROP TABLE IF EXISTS phonebook")  # удаляем старую таблицу, если была
    cur.execute("""
        CREATE TABLE phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone VARCHAR(20) UNIQUE
        )
    """)
    conn.commit()
    print("Table 'phonebook' created.")

# 2а. Добавление из CSV
def insert_from_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
                conn.commit()
            except psycopg2.errors.UniqueViolation:
                conn.rollback()
                print(f"Phone {row[1]} already exists.")
    print("CSV data inserted.")

# 2б. Добавление с консоли
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("Inserted.")
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print("This phone number already exists.")

# 3. Обновление данных
def update_user():
    phone = input("Enter phone of user to update: ")
    new_name = input("Enter new name (leave blank to skip): ")
    new_phone = input("Enter new phone (leave blank to skip): ")

    if new_name:
        cur.execute("UPDATE phonebook SET name = %s WHERE phone = %s", (new_name, phone))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (new_phone, phone))
    conn.commit()
    print("Updated.")

# 4. Поиск по фильтрам
def search():
    keyword = input("Enter name or phone to search: ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", ('%' + keyword + '%', '%' + keyword + '%'))
    results = cur.fetchall()
    for row in results:
        print(row)

# 5. Удаление по имени или номеру
def delete_user():
    keyword = input("Enter name or phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (keyword, keyword))
    conn.commit()
    print(f"Deleted {cur.rowcount} record(s).")


def show_all_users():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    print("\n📞 PhoneBook:")
    print("ID | Name     | Phone")
    print("--------------------------")
    for row in rows:
        print(f"{row[0]:<2} | {row[1]:<8} | {row[2]}")

def export_to_csv(filename="phonebook.csv"):
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "phone"])  # заголовки
        writer.writerows(rows)

    print(f"✅ Exported to {filename}")


def close():
    cur.close()
    conn.close()


def menu():
    create_table()
    while True:
        print("\n1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update user")
        print("4. Search")
        print("5. Delete")
        print("6. Show all users")
        print("7. Export to CSV")
        print("0. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            insert_from_csv("phonebook.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_user()
        elif choice == "4":
            search()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            show_all_users()
        elif choice == "7":
            export_to_csv()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

    close()

menu()
