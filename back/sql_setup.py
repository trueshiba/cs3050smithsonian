import sqlite3, csv

conn = sqlite3.connect('Smithbase.db')


# Create a cursor object to execute SQL commands
cursor = conn.cursor()


# Create a cursor object
cursor = conn.cursor()

# Execute an SQL CREATE TABLE statement to create a new table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS smithbase (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
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

"""file = open('../smithbase.csv')

contents = csv.reader(file)

insert_records = "INSERT INTO smithbase (name, last_name, gender, nationality, occupation, birth_year, death_year, age, rating) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_records, contents)
"""

select_all = "SELECT * FROM smithbase" 
rows = cursor.execute(select_all).fetchall()
 
# Output to the console screen
for r in rows:
    print(r)


# Close the cursor and connection
cursor.close()
conn.close()