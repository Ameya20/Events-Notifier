from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

import pandas as pd

import datetime
import time

import datefile
import addrfile
import mycal



def main():
    
    df=pd.read_csv('projectData.csv')

    credentials = pickle.load(open("tokennew.pkl", "rb"))
    service = build("gmail", "v1", credentials=credentials)

    response = service.users().messages().list(userId='me',q='').execute()

    currentDT = datetime.datetime.now().time()
    new = datetime.datetime.now() - datetime.timedelta(hours=1)
    newdt=new.time()

    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])

    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId='me', q='',pageToken=page_token).execute
        messages.extend(response['messages'])


    for i in messages:
        message = service.users().messages().get(userId='me', id=i['id'],
                                                 format='full').execute()

        headers=message["payload"]["headers"]

        subject= [i['value'] for i in headers if i["name"]=="Date"]
        z= datetime.datetime.strptime(subject[0],'%a, %d %b %Y %H:%M:%S %z')
        t=z.time()

        getstatus=message["labelIds"]
##        print(getstatus)
        if(t < currentDT and t  > newdt):
            #service.users().messages().modify(userId='me', id=i['id'], body="READ").execute()
            mail = message['snippet']
            print(mail)


            headers=message["payload"]["headers"]
            subject= [i['value'] for i in headers if i["name"]=="Subject"]
       #     print(subject[0])
            df.iat[0,2]=subject[0]

            


##            print("___________________")
            mailid= [i['value'] for i in headers if i["name"]=="From"]
       #     print(mailid[0])
            df.iat[0,1]=mailid[0]

            df.to_csv('projectData.csv', index=False)
         ##   print('Message snippet: %s' % message['snippet'])

        ##    print("msg,mailid,subject done")


            datefile.main(mail)
            addrfile.main(mail)
            mycal.main()

        else:
            break
##    print("msg,mailid,subject done")
##    return mail
##        print('Message snippet: %s' % message['snippet'])
##        print("___________________")
    # Query the service object to get User Profile
    #userInfo = service.users().getProfile(userId='me').execute()
    #print("UserInfo is \n %s" % (userInfo))
main()
