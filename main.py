# Blog Flask application
import os
from flask import Flask, render_template

app = Flask(__name__)
####################################################
# Routes


@app.route('/')
def homepage():
    return render_template("home.html")  


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)  # can turn off debugging with False
