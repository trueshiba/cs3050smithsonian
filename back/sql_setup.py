import sqlite3, csv, os

conn = sqlite3.connect('./smithbase.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

def main():

    # Delete current (and presumably out of date) tables
    cursor.execute('DROP TABLE IF EXISTS smithbase')
    cursor.execute('DROP TABLE IF EXISTS reviews')

    # Execute SQL CREATE TABLE statements to create new empty tables
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
            overall_rating FLOAT
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

    # Janky function for filling up the tables with data from their .csv files
    populate('smithbase',"(name, last_name, gender, nationality, occupation, birth_year, death_year, age, overall_rating) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)")

    populate('reviews', "(smith_id, rating, review) VALUES(?, ?, ?)")



def populate(tableName, parameter):

    # string concat to have correct form of filename before opening
    fileName = tableName + '.csv'
    file = open(fileName)

    # load file into csv reader
    contents = csv.reader(file)

    # sql statement setup
    insert_records = "INSERT INTO " + tableName + " " + parameter
    print(insert_records)

    cursor.executemany(insert_records, contents)

    conn.commit()

    select_all = "SELECT * FROM " + tableName 
    rows = cursor.execute(select_all).fetchall()
    
    # Output to the console screen
    for r in rows:
        print(r)


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)