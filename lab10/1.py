import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("SELECT version();")

version = cur.fetchone()
print("PostgreSQL version:", version)

cur.close()
conn.close()
