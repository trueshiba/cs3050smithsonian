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

# Load data from CSV file
with open('smithbase.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Insert each row from the CSV file into the database
        cursor.execute('''
            INSERT INTO Smitbase (full_name, last_name, gender, nationality, occupation, birth_year, death_year, age, rating)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row['Full Name'],
            row['Last Name'],
            row['Gender'],
            row['Nationality'],
            row['Occupation'],
            int(row['Birth Year']),
            int(row['Death Year']),
            int(row['Age']),
            int(row['Rating'])
        ))




# Commit the transaction (save changes)
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()