from config import load_config
import psycopg2

name = input("Enter user name: ")
phone = input("Enter phone number: ")

config = load_config()

with psycopg2.connect(**config) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM phonebook WHERE user_name = %s", (name,))
        exists = cur.fetchone()
        if exists:
            cur.execute("UPDATE phonebook SET phone_number = %s WHERE user_name = %s", (phone, name))
            print("Updated existing user")
        else:
            cur.execute("INSERT INTO phonebook (user_name, phone_number) VALUES (%s, %s)", (name, phone))
            print("Inserted new user")