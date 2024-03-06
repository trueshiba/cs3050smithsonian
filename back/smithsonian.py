from flask import Flask
import traceback

app = Flask(__name__)

@app.route('/')
def hello():
    return "<p>Hello, World!</p>"



if __name__ == '__main__':

    # pylint: disable=W0703
    try:
        app.run(debug=app.debug, host='localhost', port=8097)
    except Exception as err:
        traceback.print_exc()