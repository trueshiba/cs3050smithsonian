from flask import Flask, render_template, request, jsonify
import traceback
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('back\smithbase.db')
    return conn


app = Flask(__name__, template_folder='front', static_folder='front/static')


@app.route('/')
def hello():
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

        return jsonify(rows2)

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)})


@app.route('/<string:id>')
def washingsmith(id):
    conn = get_db_connection()
    sqlQuery = "SELECT * FROM smithbase WHERE id=" + id
    row = conn.execute(sqlQuery).fetchall()
    conn.close()
    return render_template('smith_template.html', name=row[0][1], lastname=row[0][2], sex=row[0][3],
                           nat=row[0][4], occ=row[0][5], age=row[0][8], rate=row[0][9])

if __name__ == '__main__':
    app.debug = True

    try:
        # Change debug=app.debug -> debug=True for auto reloading while coding and saving
        app.run(debug=app.debug, host='localhost', port=8097)
    except Exception as err:
        traceback.print_exc()