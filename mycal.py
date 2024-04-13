import pickle
from apiclient.discovery import  build
from google_auth_oauthlib.flow import InstalledAppFlow

from datetime import datetime, timedelta

import csv
import pandas as pd



def main():
    credentials = pickle.load(open("token.pkl", "rb"))
    service = build("calendar", "v3", credentials=credentials)
    result = service.calendarList().list().execute()
    calid=result = result['items'][0]['id']



    with open('projectData.csv','r') as csv_file:
        csv_reader=csv.reader(csv_file)

        for line in csv_reader:

            if line[0] == '1':
                sender=line[1]
                eventname=line[2]
                date=int(line[3])
                month=int(line[4])
                year=int(line[5])
                dur=int(line[9])
                h=int(line[6])
                m=int(line[7])
                s=int(line[8])
                loc=line[10]
                summ="EVENT ON " + eventname + " IS HELD AT  " + line[10] + "\n MAIL SENT BY " + line[1] + "."

                print("event set")
##                print(month)
##                print(year)


    start_time = datetime(year, month , date, h , m, s)
    end_time = start_time + timedelta(hours=2)
    timezone = 'Asia/Kolkata'

    event = {
      'summary': eventname,
      'location': loc,
      'description': summ,
      'start': {
        'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': timezone,
      },
      'end': {
        'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': timezone,
      },
      'reminders': {
        'useDefault': False,
      },
    }


    service.events().insert(calendarId=calid, body=event).execute()
