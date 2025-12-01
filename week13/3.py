import csv
import psycopg2
from config import load_config

def insert_from_csv(filename="data.csv"):
    """Insert data from CSV into phonebook table"""
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(filename, mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                        # row[0] = first_name, row[1] = last_name, row[2] = phone_number
                        full_name = f"{row[0]} {row[1]}"
                        phone = row[2]
                        cur.execute(
                            "INSERT INTO phonebook (user_name, phone_number) VALUES (%s, %s)",
                            (full_name, phone)
                        )
            print("Data inserted from CSV successfully!")

    except Exception as ex:
        print("[ERROR] Failed to insert data:", ex)


if __name__ == "__main__":
    filename = input("Enter filename: ")
    insert_from_csv(filename)