import csv
import psycopg2
from config import load_config

def insert_data_from_csv():
    connection = None
    try:
        config = load_config()
        connection = psycopg2.connect(**config)
        connection.autocommit = True

        with connection.cursor() as cursor:
            with open("data.csv", mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row[0].strip() and row[1].strip():
                        cursor.execute("INSERT INTO phonebook (user_name, phone_number) VALUES (%s, %s)", (row[0].strip(), row[1].strip()))
            print("Data inserted from CSV")

    except Exception as ex:
        print("[INFO] Error:", ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")

def insert_data_from_console():
    connection = None
    user_name = input("Enter name: ").strip()
    phone_number = input("Enter phone number: ").strip()
    
    if not user_name or not phone_number:
        print("Error: Name and phone cannot be empty!")
        return
    
    try:
        config = load_config()
        connection = psycopg2.connect(**config)
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO phonebook (user_name, phone_number) VALUES (%s, %s)", (user_name, phone_number))
        print("Data inserted from console")

    except Exception as ex:
        print("[INFO] Error:", ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")

insert_data_from_csv() 
insert_data_from_console()