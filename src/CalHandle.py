import json
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import DBhandle

SCOPES = 'https://www.googleapis.com/auth/calendar'

def authToken(email): #

    creds = None

    if DBhandle.existCreds(email) == True: #TODO: throws Attribute error 'tuple/str' object has no attribute 'keys'
        creds = Credentials.from_authorized_user_info(DBhandle.getCreds(email), SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        DBhandle.addCreds(email, creds.to_json())

        # Save the credentials for the next run
        #with DBHandle.addcreds() to database:

    return creds 

"""
Checks the the users current credentials are valid
-> if true returns a build service to call Google Calendar API
"""
def buildService(email): #
    creds = authToken(email)
    service = build('calendar', 'v3', credentials=creds)
    return service 

"""
Creates a calendar on the users account 
Takes the users email, and the name of the new calendar 
Connects to the database and add date to table
"""
def createCalendar(email, calname):#
    #if calname already exist
   calendar = {
    'summary': calname,
    'timeZone': 'America/Chicago' #only time-zone we are doing as of now 
    }
   calendar = buildService(email).calendars().insert(body=calendar).execute()
   DBhandle.addCalendar(email, calendar['id'],calendar['summary'])

"""
returns calendar resource from users account
takes the users email and the calendar name to access 
"""
def getCal(email, calname):#
    calid = DBhandle.getCalendar(email,calname)
    service = buildService(email)
    calendar = service.calendars().get(calendarId=calid).execute()
    return calendar

"""
Creates a new event in the users calendar
Takes paramters: Users email, calendar name, event name, start date of event, and end date of event
"""
def createEvent(email, calname, eventname, start_date, end_date):#
    service = buildService(email)
    calendar = getCal(email, calname) ##implement function
    try:
        EVENT = formatEvent(eventname, start_date, end_date)
        EVENT = service.events().insert(calendarId=calendar['id'], body=EVENT).execute()
        print('Event created: %s' % (EVENT.get('htmlLink'))) 
    except HttpError as error:
        print('An error occurred: %s' % error)

"""
Sets the meta data to a JSON payload 
Returns the payload to be used
Some metadata is automatically set, parameter values used user input
"""
def formatEvent(name, start_date, end_date): #
    #Current events will be ver low level just  take requirements 
    EVENT = {
    'summary': name,
    'start': {
        'dateTime': start_date,
        'timeZone': 'America/Chicago',
    },
    'end': {
        'dateTime': end_date,
        'timeZone': 'America/Chicago',
    },
    }
    
    return EVENT


"""
Get the events from the calendar paramter
Only gets the upcoming 10 events 
Metadata return as a JSON Payload
"""
def getEvents(calendarID, email):#
    service = buildService(email)
    try:
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId=calendarID, timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute() #maxresults can be alters 
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)

    return events


def removeEvent(email,eventid, calendar):
    service = buildService(email)
    service.events().delete(calendarId=calendar['id'], eventId=eventid).execute()
