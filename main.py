# Blog Flask application
import os
from flask import Flask, render_template
import psycopg2
import psycopg2.extras
from flask import Flask, request, render_template, g, current_app, session
from flask.cli import with_appcontext
import os
from src import CalHandle
from src import DBhandle
import json


app = Flask(__name__)
app.secret_key = "SyllyCalendar2023"
####################################################
# Routes


@app.route("/", methods= ['get','post'])
def signin():
    if "step" not in request.form:     
        return render_template('signin.html', step="signin", visibility="none" )
    elif request.form["step"] == "auth":
        if(DBhandle.checkUser(request.form["email"],request.form["password"]) == True):
            email = request.form["email"]
            session["email"] = email
            return render_template("home.html")
        else:
             return render_template("signin.html", step = "signin", visibility="block" )


@app.route("/signup", methods=['get','post'])
def signup():
    if "step" not in request.form:     
        return render_template('signup.html', step="signup", visibility="none")
    elif request.form["step"] == "createuser":
        if(DBhandle.checkUserExist(request.form["email"]) == True):
            return render_template("signup.html", step = "signup", visibility="block")
        else:
            DBhandle.addUser(request.form["email"], request.form["password"], request.form["fname"], request.form["lname"])
            CalHandle.authToken(request.form["email"])
            return render_template('signin.html', step="signin", visibility="none")

@app.route("/uploadevents", methods=['get', 'post'])
def uploadevents():
    data =  CalHandle.getEvents("toc8bngrdtnj2rrlfnhcb3v7l4@group.calendar.google.com",session["email"])
    return render_template("uploadevents.html", data = json.dumps(data))
    
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
    app.run(host='0.0.0.0', port=8080, debug=True)  # can turn off debugging with False
