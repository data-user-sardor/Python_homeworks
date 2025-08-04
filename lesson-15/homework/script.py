import sqlite3
# 1-task   Create a new database with a table named Roster that has three fields: Name, Species, and Age. 
# The Name and Species columns should be text fields, and the Age column should be an integer field.
DB_NAME = "Roster.db"

def create_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except sqlite3.Error as e:
        print(f" Database connection error: {e}")
        return None

def create_table(conn):
    try:
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS Roster (
                    Name TEXT,
                    Species TEXT,
                    Age INTEGER
                );
            """)
    except sqlite3.Error as e:
        print(f" Failed to create table: {e}")
# 2-task Populate your new table with the following values:
# Name 	           Species 	Age
# Benjamin Sisko 	 Human 	40
# Jadzia Dax 	     Trill 	300
# Kira Nerys 	   Bajoran 	29
def insert_data(conn):
    values = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]
    try:
        with conn:
            conn.execute("DELETE FROM Roster;")  # Optional: Clear existing data
            conn.executemany("INSERT INTO Roster VALUES (?, ?, ?);", values)
    except sqlite3.Error as e:
        print(f" Data insertion failed: {e}")
# 3-task Update the Name of Jadzia Dax to be Ezri Dax
def update_record(conn):
    try:
        with conn:
            conn.execute("""
                UPDATE Roster
                SET Name = 'Ezri Dax'
                WHERE Name = 'Jadzia Dax';
            """)
    except sqlite3.Error as e:
        print(f" Update failed: {e}")

# 4-task Display the Name and Age of everyone in the table classified as Bajoran
def query_bajoran(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT Name, Age FROM Roster WHERE Species = 'Bajoran';
        """)
        results = cursor.fetchall()
        print("\n Bajoran Members:")
        for name, age in results:
            print(f"- {name}, Age: {age}")
    except sqlite3.Error as e:
        print(f" Query failed: {e}")

def main():
    conn = create_connection()
    if conn:
        create_table(conn)
        insert_data(conn)
        update_record(conn)
        query_bajoran(conn)
        conn.close()
    else:
        print(" Could not run script due to DB connection failure.")

if __name__ == "__main__":
    main()
