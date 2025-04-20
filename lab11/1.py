import psycopg2
import csv
from psycopg2.extras import register_composite



conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

user_entry = register_composite('user_entry', conn, globally=True)
UserEntry = user_entry.type  


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

#6 show all users
def show_all_users():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    print("\n📞 PhoneBook:")
    print("ID | Name     | Phone")
    print("--------------------------")
    for row in rows:
        print(f"{row[0]:<2} | {row[1]:<8} | {row[2]}")

#7 export to csv
def export_to_csv(filename="phonebook.csv"):
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "phone"])  # заголовки
        writer.writerows(rows)

    print(f"✅ Exported to {filename}")
#8 search by pattern
def search_by_pattern():
    pattern = input("Enter pattern to search (name or phone part): ")
    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
    results = cur.fetchall()
    
    if results:
        print("\n🔍 Search results:")
        print("ID | Name     | Phone")
        print("--------------------------")
        for row in results:
            print(f"{row[0]:<2} | {row[1]:<8} | {row[2]}")
    else:
        print("No matching records found.")
#9 insert or update user by name
def insert_or_update_user(name, phone):
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print("User inserted or updated.")
#10 insert many users
from psycopg2.extras import register_composite

user_entry_caster = register_composite('user_entry', conn, globally=True)
UserEntry = user_entry_caster.type

def insert_many_users_py():
    print("Введите список пользователей. Для завершения введите пустую строку.")
    users = []
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        phone = input("Phone: ").strip()
        users.append(UserEntry(name, phone))

    cur.execute("SELECT * FROM insert_many_users(%s::user_entry[])", (users,))

    incorrect = cur.fetchall()

    if incorrect:
        print("\n❌ Incorrect entries:")
        for row in incorrect:
            print(f"Name: {row[0]}, Phone: {row[1]}")
    else:
        print("✅ All users added successfully.")\
#11 paginated quert
def get_users_by_pagination():
    try:
        limit = int(input("Enter limit (how many users to show): "))
        offset = int(input("Enter offset (how many users to skip): "))

        cur.execute("SELECT * FROM get_users_by_page(%s::integer, %s::integer)", (limit, offset))

        rows = cur.fetchall()

        if rows:
            print("\n📄 Paginated Users:")
            print("ID | Name     | Phone")
            print("--------------------------")
            for row in rows:
                print(f"{row[0]:<2} | {row[1]:<8} | {row[2]}")
        else:
            print("No users found on this page.")
    except Exception as e:
        print("❌ Error during pagination:", e)
#12 delete by name
def delete_by_procedure():
    keyword = input("Enter name or phone to delete: ")
    try:
        cur.execute("CALL delete_user_by_name_or_phone(%s)", (keyword,))
        conn.commit()
        print("✅ Deletion done via procedure.")
    except Exception as e:
        conn.rollback()
        print("❌ Error during deletion:", e)



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
        print("8. Search by pattern (via SQL function)")
        print("9. Insert or update user (by name)")
        print("10. Insert many users (with phone check)")
        print("11. Paginated query")
        print("12. Delete by name or phone (via procedure)")




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
        elif choice == "8":
            search_by_pattern()
        elif choice == "9":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            insert_or_update_user(name, phone)
        elif choice == "10":
            insert_many_users_py()
        elif choice == "11":
            get_users_by_pagination()
        elif choice == "12":
            delete_by_procedure()



        elif choice == "0":
            break
        else:
            print("Invalid option.")

    close()

menu()