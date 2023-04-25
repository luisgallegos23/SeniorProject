# Blog Flask application
from flask import Flask, render_template
import psycopg2
import psycopg2.extras
from flask import Flask, request, render_template, g, flash, session
import os
from src import CalHandle
from src import DBhandle
from werkzeug.utils import secure_filename
import json
import os
from src import keywordfinder

app = Flask(__name__)
app.secret_key = "SyllyCalendar2023"
UPLOAD_FOLDER ='uploads' #path for uploaded folders
ALLOWED_EXTENSIONS = {'pdf','txt'}  #allowed extensions -> can be added to 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
####################################################
# Routes

#Allows the user to singin with the Required Credentials (Email and Password)
#Returns an error message if the information is wrong
#If credentials match user data in the Database allows user to move to next page
@app.route("/", methods= ['get','post'])
def signin():
    if "step" not in request.form:     
        return render_template('signin.html', step="signin", visibility="none" )
    
    elif request.form["step"] == "auth":
        if(DBhandle.checkUser(request.form["email"],request.form["password"]) == True):
            email = request.form["email"]
            session["email"] = email
            #TODO: when return the template add other paramater for data to create calendar
            return render_template("CalendarSplit.html")
        
        else:
             return render_template("signin.html", step = "signin", visibility="block" )


#Allows user to sign up to use our service
#creaets credentials and other information
#REQUIRED: User needs to have a Google account 
@app.route("/signup", methods=['get','post'])
def signup():
    if "step" not in request.form:     
        return render_template('signup.html', step="signup", visibility="none")
    
    elif request.form["step"] == "createuser":
        if(DBhandle.checkUserExist(request.form["email"]) == True):
            return render_template("signup.html", step = "signup", visibility="block")
        
        else:
            DBhandle.addUser(request.form["email"], request.form["password"], request.form["fname"], request.form["lname"])
            #Redirects user to Google for conformation to use our service 
            CalHandle.authToken(request.form["email"])
            return render_template('signin.html', step="signin", visibility="none")


#Allows users to authenticate the new events that will be created 
#Creates the events from the PDF that is read
@app.route("/uploadevents", methods=['get', 'post'])
def uploadevents():
    if "step" not in request.form:
        #TODO: Change data to match the information from PDF-> Next line is only for test 
        return render_template("uploadevents.html")
    
    #After sumbit will create the Events 
    elif request.form["step"] == "create":
        num = int(request.form["numelements"])
        calname = request.form["calname"]
        CalHandle.createCalendar(session["email"], calname)
        for y in range(1, num+1):
            x = str(y)
            title = request.form["event-title"+x]
            startdate = request.form["start-date"+x]
            starttime = request.form["start-time"+x]
            enddate = request.form["end-date"+x]
            endtime = request.form["end-time"+x]
            des = request.form["description"+x]
            start = CalHandle.formateTimeStap(startdate,starttime)
            end = CalHandle.formateTimeStap(enddate, endtime)
            CalHandle.createEvent(session["email"], calname, title, start, end, des);
        return 'executed'; #TODO: return a template that informs the user of creation


#Makes sure the file being submited is a correct TYPE
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Allows for the upload of a document to the server
@app.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return render_template("uploadform.html", empty="none", tag="block")
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return render_template("uploadform.html", empty="block", tag="none")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            data = keywordfinder.generateevents(filename);
            calname= request.form["class-title"];
            return render_template("uploadevents.html", data = json.dumps(data), name = calname)
    return render_template("uploadform.html", empty="none", tag="none")


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
