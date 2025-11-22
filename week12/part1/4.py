import psycopg2
from config import load_config

def get_phonebook():
    """ Retrieve data from the phonebook table with interactive filters """
    config = load_config()
    
    print("\n=== Query Phonebook with Filters ===")
    print("1. Filter by name")
    print("2. Filter by phone number") 
    print("3. Filter by ID range")
    
    choice = input("Enter your choice (1-3): ").strip()
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if choice == '1':
                    name = input("Enter name to search: ").strip()
                    cur.execute("SELECT id, user_name, phone_number FROM phonebook WHERE user_name = %s", (name,))
                    
                elif choice == '2':
                    phone = input("Enter phone number to search: ").strip()
                    cur.execute("SELECT id, user_name, phone_number FROM phonebook WHERE phone_number = %s", (phone,))
                    
                elif choice == '3':
                    min_id = input("Enter minimum ID: ").strip()
                    max_id = input("Enter maximum ID: ").strip()
                    cur.execute("SELECT id, user_name, phone_number FROM phonebook WHERE id BETWEEN %s AND %s", (min_id, max_id))
                    
                else:
                    print("Invalid choice!")
                    return

                rows = cur.fetchall()
                print(f"\nFound {len(rows)} users:")
                for row in rows:
                    print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
                    
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

if __name__ == '__main__':
    get_phonebook()