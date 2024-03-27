from flask import Flask, render_template, request, jsonify 
import traceback
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('back/Smithbase.db')
    return conn


app = Flask(__name__, template_folder='front', static_folder='front/static')
app.config['TEMPLATES_AUTO_RELOAD'] = True

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

        print("Number of rows found:", len(rows2))
        print("Rows:", rows2)

        return render_template('index.html', rows=rows2)

        #return jsonify(rows2)
    
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)})


if __name__ == '__main__':

    try:
        app.run(debug=app.debug, host='localhost', port=8097)
    except Exception as err:
        traceback.print_exc()