from config import load_config
import psycopg2

limit = int(input("Enter limit: "))
offset = int(input("Enter offset: "))

config = load_config()

with psycopg2.connect(**config) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM phonebook ORDER BY id ASC LIMIT %s OFFSET %s", (limit, offset))
        rows = cur.fetchall()
        print(f"Found {len(rows)} rows")
        for row in rows:
            print(row)