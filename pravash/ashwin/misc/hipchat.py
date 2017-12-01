#!/usr/bin/python

import requests, json

amessage = 'Hello World!'
room = 'https://api.hipchat.com/v2/room/18REPLACE35/notification'
headers = {'Authorization':'Bearer YourHipChatToken', 'Content-type':'application/json'}
requests.post(url = room, data = json.dumps({'message':amessage}), headers = headers)
