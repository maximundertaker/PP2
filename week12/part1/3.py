import psycopg2
from config import load_config

def update_phonebook():
    """ Update Phonebook name based on the Phonebook id """
    
    id = input("Enter user ID: ")
    user_name = input("Enter new name: ")
    
    sql = """UPDATE phonebook SET user_name = %s WHERE id = %s"""
    
    try:
        config = load_config()
        connection = psycopg2.connect(**config)
        connection.autocommit = True
        
        with connection.cursor() as cursor:
            cursor.execute(sql, (user_name, id))
            updated_rows = cursor.rowcount
            
        if updated_rows > 0:
            print("User name updated successfully!")
        else:
            print("No user found with that ID.")
            
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

if __name__ == '__main__':
    update_phonebook()