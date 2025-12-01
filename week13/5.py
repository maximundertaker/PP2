from config import load_config
import psycopg2

value = input("Enter username or phone to delete: ")

config = load_config()

with psycopg2.connect(**config) as conn:
    with conn.cursor() as cur:
        cur.execute("DELETE FROM phonebook WHERE user_name = %s OR phone_number = %s", (value, value))
        print("Deleted (if existed)")