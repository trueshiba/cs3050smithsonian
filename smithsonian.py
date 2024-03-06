from flask import Flask, render_template 
import traceback

app = Flask(__name__, template_folder='front', static_folder='front/css')


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':

    try:
        app.run(debug=app.debug, host='localhost', port=8097)
    except Exception as err:
        traceback.print_exc()