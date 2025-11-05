"""
flask
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return( 'Hello World')

@app.route("/me_urmat")
def about__me():
    return "me informate" 


if __name__ == '__main__':
    app.run(debug=True)
