# Blog Flask application
import os
from flask import Flask, render_template
import psycopg2
import psycopg2.extras
from flask import Flask, request, render_template, g, current_app, session
from flask.cli import with_appcontext
import click
from src import DBhandle


app = Flask(__name__)
app.secret_key = "SyllyCalendar2023"
####################################################
# Routes


@app.route("/", methods= ['get','post'])
def signin():
    if "step" not in request.form:     
        return render_template('signin.html', step="signin")
    elif request.form["step"] == "auth":
        if(DBhandle.checkUser(request.form["email"],request.form["password"]) == True):
            email = request.form["email"]
            session["email"] = email
            return render_template("home.html", step = "true")
        else:
             return render_template("signin.html", step = "false")


@app.route("/signup", methods=['get','post'])
def signup():
    if "step" not in request.form:     
        return render_template('signup.html', step="signup")
    elif request.form["step"] == "createuser":
        DBhandle.addUser(request.form["email"], request.form["password"], request.form["fname"], request.form["lname"])
        return render_template('signin.html', step="signin")

    
@app.teardown_appcontext
def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()
        debug("Closing DB")
    
#####################################################
#####################################################
# Debugging

def debug(s):
    """Prints a message to the screen (not web browser) 
    if debugging is turned on."""
    if app.config['DEBUG']:
        print(s)

#####################################################

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)  # can turn off debugging with False
