from __future__ import print_function
import datetime
import os.path
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = 'https://www.googleapis.com/auth/calendar'

def test():
    createEvents()
    


"""
Reads MockData.csv file
Reads file line by line -> creates events using data and add them to calendar
Validates credientials to write/read form AP
"""
def createEvents():
      
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
   
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    calendar = createCalendar(service)
    

    file = open("/Users/luisgallegos/Desktop/Programming-Projects/SeniorProject/MockData.csv","r")
    num = 0 #number of events being uploaded
    file.readline()
    for line in file:
        if(num < 30): # Can be changed to number of events needed
            num += 1  # Does not stop at num = 30
            eventname, start_date, end_date, test = line.split(',')
            EVENT = formatEvent(eventname, start_date, end_date)
            EVENT = service.events().insert(calendarId=calendar['id'], body=EVENT).execute()
            print('Event created: %s' % (EVENT.get('htmlLink')))
        else:
            break    
    file.close()
    getEvents(service,calendar['id'])



"""
Sets the meta data to a JSON payload 
Returns the payload to be used
Some metadata is automatically set for testing, parameter values used from file data 
"""
def formatEvent(name, start_date, end_date):
    EVENT = {
    'summary': name,
    'location': '800 Howard St., San Francisco, CA 94103',
    'description': 'This is a test event. Hope it works correclty',
    'start': {
        'dateTime': start_date,
        'timeZone': 'America/Los_Angeles',
    },
    'end': {
        'dateTime': end_date,
        'timeZone': 'America/Los_Angeles',
    },
    'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
        ],
    },
    }
    
    return EVENT

"""
Creates a calendar on the users account 
Creates ID for use 
Returns ID for use 
TO DO: Check if calendar already exist 
"""

def createCalendar(service):
   calendar = {
    'summary': 'Sylly Test',
    'timeZone': 'America/Chicago'
    }
   calendar = service.calendars().insert(body=calendar).execute()
   return calendar
   
"""
Get the events from the calendar paramter
Only gets the upcoming 10 events 
Metadata return as a JSON Payload
"""

def getEvents(service, calendar):
    try:
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId=calendar, timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
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

"""
Used for testing -> only function that allows to create event
"""

def formatEvent2(service, calendar):
    EVENT = {
    'summary': 'test',
    'location': '800 Howard St., San Francisco, CA 94103',
    'description': 'This is a test event. Hope it works correclty',
    'start': {
        'dateTime': '2023-02-20T09:00:00-07:00',
        'timeZone': 'America/Chicago',
    },
    'end': {
        'dateTime': '2023-02-20T17:00:00-07:00',
        'timeZone': 'America/Chicago',
    },
    'recurrence': [
        'RRULE:FREQ=DAILY;COUNT=1'
    ],
    'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
        ],
    },
    }
    EVENT = service.events().insert(calendarId=calendar, body=EVENT).execute()
    return EVENT

if __name__ == '__main__':
    test()