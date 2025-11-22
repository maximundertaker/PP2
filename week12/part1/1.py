import psycopg2
from config import load_config

def create_phonebook_table():
    """1. Design tables for PhoneBook"""
    try:
        config = load_config()
        
        connection = psycopg2.connect(**config)
        connection.autocommit = True
        
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS Phonebook (id SERIAL PRIMARY KEY, User_name VARCHAR(64) NOT NULL, Phone_number VARCHAR(20) NOT NULL);")
            print("Table created successfully!")
            
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if 'connection' in locals():
            connection.close()
            print("[INFO] PostgreSQL connection closed")

if __name__ == '__main__':
    create_phonebook_table()