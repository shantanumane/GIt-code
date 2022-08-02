import json
from datetime import date
import requests
URL="http://127.0.0.1:8000/deleteUser/"

#res=requests.post(url=URL,data=jsonData)
#data=res.json()
#rint(data)

def update():
    data={
        'id':'4',
        'username': 'newsm-updated',
        'password':'sm01',
        'email':'sm01@gmail.com',
        'dateOfBirth':str(date.today()),
    }

    jsonData=json.dumps(data)
    res=requests.put(url=URL,data=jsonData)
    data=res.json()
    print(data)


def deleteData():
    data={
        'id':'4'
    }

    jsonData=json.dumps(data)
    res=requests.delete(url=URL,data=jsonData)
    data=res.json()
    print(data)

deleteData()