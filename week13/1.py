from config import load_config
import psycopg2

pattern = input("Enter pattern to search: ")

config = load_config()

with psycopg2.connect(**config) as conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT * FROM phonebook
            WHERE user_name ILIKE %s OR phone_number ILIKE %s""", (f"%{pattern}%", f"%{pattern}%"))
        results = cur.fetchall()
        for row in results:
            print(row)