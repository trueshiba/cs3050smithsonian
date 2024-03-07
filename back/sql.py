import sqlite3

conn = sqlite3.connect('Smithbase.db')


# Create a cursor object to execute SQL commands
cursor = conn.cursor()


# Create a cursor object
cursor = conn.cursor()

# Execute an SQL CREATE TABLE statement to create a new table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS famous_people (
        id INTEGER PRIMARY KEY,
        full_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        gender TEXT,
        nationality TEXT,
        occupation TEXT,
        birth_year INTEGER,
        death_year INTEGER,
        age INTEGER,
        rating INTEGER
    )
''')

# Commit the transaction (save changes)
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()