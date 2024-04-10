import sqlite3, csv, os

conn = sqlite3.connect('./smithbase.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

def main():

    # Delete current (and presumably out of date) table
    cursor.execute('DROP TABLE IF EXISTS smithbase')
    cursor.execute('DROP TABLE IF EXISTS reviews')

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
            rating FLOAT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            review_id INTEGER PRIMARY KEY,
            smith_id INTEGER NOT NULL,
            rating INTEGER,
            review TEXT
        )
    ''')

    conn.commit()

    current_working_directory = os.getcwd()

    # print output to the console
    print(current_working_directory)

    # Load data from CSV file
    """with open('smithbase.csv', 'r', newline='', encoding='utf-8') as csvfile:
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
            ))"""

    populate('smithbase',"(name, last_name, gender, nationality, occupation, birth_year, death_year, age, rating) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)")

    populate('reviews', "(smith_id, rating, review) VALUES(?, ?, ?)")



def populate(tableName, parameter):

    fileName = tableName + '.csv'
    file = open(fileName)

    contents = csv.reader(file)

    insert_records = "INSERT INTO " + tableName + " " + parameter
    print(insert_records)

    cursor.executemany(insert_records, contents)

    conn.commit()

    select_all = "SELECT * FROM " + tableName 
    rows = cursor.execute(select_all).fetchall()
    
    # Output to the console screen
    for r in rows:
        print(r)


main()