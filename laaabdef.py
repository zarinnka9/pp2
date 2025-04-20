

conn = psycorg2.connect(
    dbname = "postgres"
    user = " postgres"
    password = "12345678"
    host = "localhost"
    port = "5432"
)
cur = conn.cursor()

def create_table():
    cur.execute("drop ")
    cur.execute("""
        CREATE TABLE PHONEBOOK (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone VARCHAR(20) UNIQUE
        )
    """)
    conn.commit()
