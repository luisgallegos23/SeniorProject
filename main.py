# Blog Flask application
import os
from flask import Flask, render_template
import psycopg2
import psycopg2.extras
from flask import Flask, request, render_template, g, current_app, session
from flask.cli import with_appcontext
import click


app = Flask(__name__)
####################################################
# Routes


@app.route("/", methods= ['get','post'])
def signin():
 if "step" not in request.form:     
  return render_template('signin.html', step="signin")
 elif request.form["step"] == "auth":
   conn = get_db()
   cursor = conn.cursor()
   cursor.execute("select count(*) from users where email=%s and password=%s", [request.form["email"], request.form["password"]])
   count=cursor.fetchone();
   if(count == [1]):
     email = request.form["email"]
     session["email"] = email
     return render_template("home.html", step = "true")
   else:
    return render_template("home.html", step = "false")
   
##@app.route('/')
##def homepage():
    ##if "step"
    ##return render_template("home.html")  

#####################################################
# Database handling 
  
def connect_db():
    """Connects to the database."""
    debug("Connecting to DB.")
    conn = psycopg2.connect(host="", user="", password="", dbname="",  #NEEDS TO FIX
        cursor_factory=psycopg2.extras.DictCursor)
    return conn
    
def get_db():
    """Retrieve the database connection or initialize it. The connection
    is unique for each request and will be reused if this is called again.
    """
    if "db" not in g:
        g.db = connect_db()
    return g.db
    
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
