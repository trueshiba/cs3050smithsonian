from flask import Flask, render_template, request, jsonify, url_for, redirect
import traceback
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('back\smithbase.db')
    return conn


app = Flask(__name__, template_folder='front', static_folder='front/static')


@app.route('/')
def start():
    return redirect(url_for("home"), code=302)


@app.route('/home')
def home():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM smithbase").fetchall()
    conn.close()
    return render_template('index.html', rows=rows)


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
        
        print(rows2)
        return jsonify(rows2)

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)})


@app.route('/<string:id>')
def profile(id):
    conn = get_db_connection()
    sqlQueryProfile = "SELECT * FROM smithbase WHERE id=" + id ## Easy sql injection attack here by changing what ID is!!!!
    sqlQueryReviews = "SELECT rating, review FROM reviews INNER JOIN smithbase ON smithbase.id=reviews.smith_id WHERE smithbase.id=" + id
    profileRow = conn.execute(sqlQueryProfile).fetchall()
    reviewRows = conn.execute(sqlQueryReviews).fetchall()
    print(reviewRows)
    conn.close()
    return render_template('smith_template.html', 
                            name=profileRow[0][1], lastname=profileRow[0][2], sex=profileRow[0][3], nat=profileRow[0][4], occ=profileRow[0][5], age=profileRow[0][8], rate=profileRow[0][9],
                            reviews=reviewRows
                            )


if __name__ == '__main__':
    app.debug = True

    try:
        # Change debug=app.debug -> debug=True for auto reloading while coding and saving
        app.run(debug=False, host='localhost', port=8097)
    except Exception as err:
        traceback.print_exc()