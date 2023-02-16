from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from httplib2 import Http

def test():
    createEvents()



def createEvents():
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
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

    try:
        http = creds.authorize(Http())
        service = build('calendar', 'v3', http=http)
        file = open("/Users/luisgallegos/Desktop/Programming-Projects/SeniorProject/MockData.csv","r")
        num = 0 #number of events being uploaded
        file.readline()
        for line in file:
            if(num == 30):
                file.close()
            eventname, start_date, end_date = line.split(',')
            #print('{} {} {}'.format(eventname,start_date, end_date))
            event = formatEvent(eventname, start_date, end_date)
            #print(event)
            event = service.events().insert(calendarId='test', body=event).execute()
            print('Event created: %s' % (event.get('htmlLink')))

    except HttpError as error:
        print("Error occured: %s" %error)



"""
Sets the meta data to a JSON payload 
Returns the payload to be used
Some metadata is automatically set, parameter values used from file data 
"""
def formatEvent(name, start, end):
    event = {
    'summary': name,
    'location': '800 Howard St., San Francisco, CA 94103',
    'description': 'This is a test event. Hope it works correclty',
    'start': {
        'dateTime': start,
        'timeZone': 'America/Chicago',
    },
    'end': {
        'dateTime': end,
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
    return event; 


def getEvents():
    SCOPES = ['https://www.googleapis.com/auth/calendar/readonly']
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
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

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='test', timeMin=now,
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

if __name__ == '__main__':
    test()