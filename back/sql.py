import sqlite3
import csv

conn = sqlite3.connect('Smithbase.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

cursor.execute('DROP TABLE Smithbase')

# Execute an SQL CREATE TABLE statement to create a new table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Smithbase (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        gender TEXT,
        nationality TEXT,
        occupation TEXT,
        birth_year INTEGER,
        death_year INTEGER,
        age INTEGER,
        rating FLOAT
    )
''')

conn.commit()

# Load data from CSV file
with open('smithbase.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Insert each row from the CSV file into the database
        cursor.execute('''
            INSERT INTO Smithbase (name, last_name, gender, nationality, occupation, birth_year, death_year, age, rating)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row['Name'],
            row['Last Name'],
            row['Gender'],
            row['Nationality'],
            row['Occupation'],
            int(row['Birth Year']),
            int(row['Death Year']),
            int(row['Age']),
            float(row['Rating'])
        ))


# Commit the transaction (save changes)
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()