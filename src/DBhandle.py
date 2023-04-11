import psycopg2
import psycopg2.extras
from flask import g

"""Connects to the database."""  
def connect_db():
    #debug("Connecting to DB.")
    conn = psycopg2.connect(sslmode="verify-ca", sslrootcert="DB/server-ca.pem", sslcert="DB/client-cert.pem", sslkey="DB/client-key.pem", hostaddr="104.155.144.9", port="5432", user="sylly", dbname="sylly", password="Sylly2023") #remove ../ after testing
    return conn

"""
Retrieve the database connection or initialize it. The connection
is unique for each request and will be reused if this is called again.
"""    
def get_db(): 
    if "db" not in g: # Mark for test
        g.db = connect_db() # Mark for test
    return g.db #Replace with connect_db() for test

  
"""
Fetches the number of times the user is located in the data
'email' and 'key'(password) have to match to an existance user in database
returns True if a user exist
returns false if no user exist 
"""
def checkUser(email, key):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM users WHERE email=%s AND password=%s", [email, key]) 
        count=cursor.fetchone()
        conn.close()
        if(count[0] == 1):
            return True
        return False
    
    except(Exception, psycopg2.Error) as error:
        print("Error authenticating user with PosgresSQL Database ", error)

"""
Adds a non-existant user to the database 
creates the row and allocated the perspective data to corosponding column 
"""
def addUser(email, key, fname, lname):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (email, password, lname, fname) VALUES (%s, %s, %s, %s)", [email, key, lname, fname])
        conn.commit()
        conn.close()
    
    except(Exception, psycopg2.Error) as error:
        print("Error adding user to PostgresSQL database", error)

"""
Adds a new calender object to the database
Users can have muttiple calendars 
Takes the new calendar's 'ID', and 'Name' and the users 'Email 
"""
def addCalendar(email, calID, calname):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO calendars (email, calID, calname) VALUES (%s, %s, %s)", [email, calID, calname])
        conn.commit()
        conn.close()

    except(Exception, psycopg2.Error) as error:
        print("Error adding calendar to PostgresSQL database", error)    

"""
Fetches a users calendar form the database 
Takes the users email and name of the calendar
returns the ID of the calendar for Google API look up
"""
def getCalendar(email, name):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT calID FROM calendars WHERE email=%s AND calname=%s ", [email, name])
        data = cursor.fetchone()[0]
        conn.close()
        return data
    
    except(Exception, psycopg2.Error) as error:
        print("Error fetching data from PostgresSQL database", error)


def existCal(email, calname):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM calendars WHERE email=%s and calname=%s", [email, calname]) 
        count=cursor.fetchone()
        conn.close()
        if(count[0] == 1):
            return True
        return False

    except(Exception, psycopg2.Error) as error:
        print("Error checking Calendar existence in PostgresSQL database", error)

"""
Fetches ALL the calendars of the current User
Takes the email of the user 
returns a list of Objects 
Access each object in FOR LOOP
"""
def getListCalendars(email):#TODO: Test
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT calID FROM calendars WHERE email=%s ", [email])
        data = cursor.fetchall()
        conn.close()
        return data
    
    except(Exception, psycopg2.Error) as error:
        print("Error fetching Calendars from PostgresSQL database", error)

"""
Adds the users corresponding TOKEN after authentication with API
Takes the users email and the new constructed TOKEN for use 
"""
def addCreds(email, token):#
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO creds (email, token) VALUES (%s, %s)", [email, token])
        conn.commit()
        conn.close()

    except(Exception, psycopg2.Error) as error:
        print("Error adding token to PostgresSQL database", error)

"""
Fetches users Token credential for use to access Google API
Returns as a json object 
"""
def getCreds(email): 
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT token FROM creds WHERE email=%s ", [email])
        data = cursor.fetchone()[0]
        conn.close()
        return data
    
    except(Exception, psycopg2.Error) as error:
        print("Error fetching token from PostgresSQL database", error)

"""
Updates the User's credential if Token needs to be refreshed 
Takes the user's email and the New Tokne to be added 
"""
def updateCreds(email, newtoken): #Could have an error #TODO: Test
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE creds SET token=%s WHERE email=%s", [newtoken,email])
        conn.commit()
        conn.close()
    
    except(Exception, psycopg2.Error) as error:
        print("Error updating token to PostgresSQL database", error)



def existCreds(email): #
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM creds WHERE email=%s ", [email]) 
        count=cursor.fetchone()
        conn.close()
        if(count[0] == 1):
            return True
        return False
    
    except(Exception, psycopg2.Error) as error:
        print("Error checking for token existence in PostgresSQL database", error)

