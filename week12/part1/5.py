import psycopg2
from config import load_config

def delete_phonebook():
    """ Delete data from phonebook table by username or phone """
    config = load_config()
    
    print("\n=== Delete from Phonebook ===")
    print("1. Delete by username")
    print("2. Delete by phone number")
    
    choice = input("Enter your choice (1-2): ").strip()
    rows_deleted = 0
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if choice == '1':
                    username = input("Enter username to delete: ").strip()
                    sql = 'DELETE FROM phonebook WHERE user_name = %s'
                    cur.execute(sql, (username,))
                    rows_deleted = cur.rowcount
                    
                elif choice == '2':
                    phone = input("Enter phone number to delete: ").strip()
                    sql = 'DELETE FROM phonebook WHERE phone_number = %s'
                    cur.execute(sql, (phone,))
                    rows_deleted = cur.rowcount
                    
                else:
                    print("Invalid choice!")
                    return
                    
                conn.commit()
                
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print(f'The number of deleted rows: {rows_deleted}')
        return rows_deleted

if __name__ == '__main__':
    delete_phonebook()