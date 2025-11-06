"""
flask
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/about_me")
def about_me():
    return "my name is Islam"

@app.route("/boxing")
def boxing():
    return "im train boxing every single day"     


@app.route("/ABV")
def ABV():
    return "права алыш крк"    


@app.route("/profil")
def profil():
    return "G30" 


@app.route("/BMW")
def BMW():
    return "M5 f90"
    

if __name__ == "__main__":
    app.run(
        debug=True,
    )


