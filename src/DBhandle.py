import psycopg2
import psycopg2.extras
from flask import Flask, request, render_template, g, current_app, session
  
def connect_db():
    """Connects to the database."""
    #debug("Connecting to DB.")
    conn = psycopg2.connect(sslmode="verify-ca", sslrootcert="DB/server-ca.pem", sslcert="DB/client-cert.pem", sslkey="DB/client-key.pem", hostaddr="104.155.144.9", port="5432", user="sylly", dbname="sylly", password="Sylly2023")
    return conn
    
def get_db():
    """Retrieve the database connection or initialize it. The connection
    is unique for each request and will be reused if this is called again.
    """
    if "db" not in g:
        g.db = connect_db()
    return g.db

"""
Fetches the number of times the user is located in the data
'email' and 'key'(password) have to match to an existance user in database
returns True if a user exist
returns false if no user exist 
"""
def checkUser(email, key):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM users WHERE email=%s AND password=%s", [email, key]) 
    count=cursor.fetchone()
    print(count)
    if(count[0] == 1):
        return True
    return False

"""
Adds a non-existant user to the database 
creates the row and allocated the perspective data to corosponding column 
"""
def addUser(email, key, fname, lname):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email, password, lname, fname) VALUES (%s, %s, %s, %s)", [email, key, lname, fname])
    conn.commit()

"""
Adds a new calender object to the database
Users can have muttiple calendars 
Takes the new calendar's 'ID', and 'Name' and the users 'Email 
"""
def addCalendar(email, calID, calname):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO calendars (email, calID, calname) VALUES (%s, %s, %s)", [email, calID, calname])
    conn.commit()

"""
Fetches a users calendar form the database 
Takes the users email and name of the calendar
returns the ID of the calendar for Google API look up
"""
def getCalendar(email, name):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT calID FROM calendars WHERE email=%s AND name=%s ", [email, name])
    data = cursor.fetchall()
    return data

"""
Fetches ALL the calendars of the current User
Takes the email of the user 
returns a list of Objects 
Access each object in FOR LOOP
"""
def getListCalendars(email):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT calID FROM calendars WHERE email=%s ", [email])
    data = cursor.fetchall()
    return data

"""
Adds the users corresponding TOKEN after authentication with API
Takes the users email and the new constructed TOKEN for use 
"""
def addCreds(email, token): #could have an error
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO creds (email, token) VALUES (%s, %s)", [email, token])
    conn.commit()

"""
Fetches users Token credential for use to access Google API
Returns as a json object 
"""
def getCreds(email): #Could have an error 
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT token FROM creds WHERE email=%s ", [email])
    data = cursor.fetchall()
    return data

"""
Updates the User's credential if Token needs to be refreshed 
Takes the user's email and the New Tokne to be added 
"""
def updateCreds(email, newtoken): #Could have an error
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE creds SET token=%s WHERE email=%s", [newtoken,email])
    conn.commit()



