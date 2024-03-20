from flask import Flask, render_template, request, jsonify 
import traceback
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('back/Smithbase.db')
    return conn


app = Flask(__name__, template_folder='front', static_folder='front/static')


@app.route('/')
def hello():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM smithbase").fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

@app.route('/test')
def washingsmith():
    conn = get_db_connection()
    row = conn.execute("SELECT 1 FROM smithbase").fetchone()
    conn.close()
    return render_template('smith_template.html', name=row[1], lastname=row[2])

@app.route('/search')
def searchFunction():

    search_query = request.get_json().get('searchQuery')
    sort_method = request.get_json().get('sortMethod')

    conn = get_db_connection()

    query = ""
    rows = conn.execute(query, (f'%{search_query}%', sort_method)).fetchall()
    conn.close()
    return render_template('smith_template.html', name=row[1], lastname=row[2])


if __name__ == '__main__':

    try:
        app.run(debug=app.debug, host='localhost', port=8097)
    except Exception as err:
        traceback.print_exc()