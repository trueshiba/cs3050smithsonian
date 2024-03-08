from flask import Flask, render_template 
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


if __name__ == '__main__':

    try:
        app.run(debug=app.debug, host='localhost', port=8097)
    except Exception as err:
        traceback.print_exc()