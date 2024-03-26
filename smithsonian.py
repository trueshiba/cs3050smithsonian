from flask import Flask, render_template, request
import traceback
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('back/smithbase.db')
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
    row = conn.execute("SELECT * FROM smithbase WHERE id=2").fetchall()
    conn.close()
    return render_template('smith_template.html', name=row[0][1], lastname=row[0][2], sex=row[0][3],
                           nat=row[0][4], occ=row[0][5], age=row[0][8], rate=row[0][9])

@app.route('/search')
def search():
    query = request.args.get('q')
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM smithbase WHERE name LIKE ?", ('%' + query + '%',)).fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    
    try:
        app.run(debug=app.debug, host='localhost', port=8097)
    except Exception as err:
        traceback.print_exc()