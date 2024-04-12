from flask import Flask, render_template, request, jsonify, url_for, redirect
import traceback
import sqlite3


# Creates link to database that we can use in our other app routes
def get_db_connection():
    conn = sqlite3.connect('back\smithbase.db')
    return conn


# Defines flask app and specifys where to look for html and static resources
app = Flask(__name__, template_folder='front', static_folder='front/static')


# Base app route
@app.route('/')
def start():
    # Auto redirects to .../home with code 302: 'redirect'
    return redirect(url_for("home"), code=302)


# Home page for app. Gets all entries within database to display
@app.route('/home')
def home():
    conn = get_db_connection()
    # Get all entries from database
    rows = conn.execute("SELECT * FROM smithbase").fetchall()
    conn.close()

    # Debugging statement
    if (app.debug == True): print(rows)

    return render_template('index.html', rows=rows)


# Search route used after entering in search bar/ submitting on button to display the user query
@app.route('/search', methods=['POST'])
def searchFunction():
    try:
        data = request.get_json()
        search_query = data.get('searchQuery')
        sort_method = data.get('sortMethod')
        rows2 = []

        print(search_query, sort_method)

        conn = get_db_connection()

        if len(sort_method) == 0:
            query = "SELECT * FROM smithbase WHERE name LIKE ? OR last_name LIKE ? OR gender LIKE ? OR nationality LIKE ? OR occupation LIKE ? ORDER BY name ASC"
            rows2 = conn.execute(query, ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%')).fetchall()
        else:
            query = "SELECT * FROM smithbase WHERE name LIKE ? OR last_name LIKE ? OR gender LIKE ? OR nationality LIKE ? OR occupation LIKE ? ORDER BY {} ASC".format(sort_method)
            rows2 = conn.execute(query, ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%')).fetchall()

        conn.close()

        
        #return render_template('index.html', rows=rows2)
        
        # Debugging statement
        if (app.debug == True): print(rows2)

        return jsonify(rows2)

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)})


# Individual 'Smith' profile page route
# Uses the pmk_id of a given smith to query the datbase and fill in template page with correct values
@app.route('/<int:id>', methods=['GET', 'POST'])
def profile(id):
    conn = get_db_connection()
    
    # Initial query to get smith profile info
    sqlQueryProfile = "SELECT * FROM smithbase WHERE id=" + str(id) ## <----------------- Easy sql injection attack here by changing what ID is!!!!
    # Secondary INNER JOIN query to get corresponding reviews of chosen smith
    sqlQueryReviews = "SELECT rating, review FROM reviews INNER JOIN smithbase ON smithbase.id=reviews.smith_id WHERE smithbase.id=" + str(id)

    profileRow = conn.execute(sqlQueryProfile).fetchall()
    reviewRows = conn.execute(sqlQueryReviews).fetchall()

    # Debugging statement
    if (app.debug == True): print(reviewRows)
    
    conn.close()
    return render_template('smith_template.html', 
                            name=profileRow[0][1], lastname=profileRow[0][2], sex=profileRow[0][3], nat=profileRow[0][4], occ=profileRow[0][5], age=profileRow[0][8], rate=profileRow[0][9],
                            reviews=reviewRows
                            )



@app.route('/rate/<int:id>', methods=['POST'])
def rateFunction(id):
    try:
        data = request.get_json()
        rating = data.get('rating5')
        review = data.get('reviewWritten')

        print(id, rating, review)

        conn = get_db_connection()

        query = "UPDATE smithbase SET rating = ?, review = ? WHERE CustomerID = ?;"
        conn.execute(query, (rating, review, id))
        conn.commit() 

        conn.close()

        return render_template('smith_template.html', id=id)
        
        #return jsonify(rows2)

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)})




if __name__ == '__main__':
    app.debug = False

    try:
        # Change debug=app.debug -> debug=True for auto reloading while coding and saving
        app.run(debug=app.debug, host='localhost', port=8097)
    except Exception as err:
        traceback.print_exc()