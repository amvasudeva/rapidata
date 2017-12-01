#! /usr/bin/python
#Need to install requests package for python
#sudo easy_install requests
import requests
 
 # Set the request parameters
url = 'https://wiprodemo.service-now.com/api/now/table/incident'
user = 'Default'
pwd = 'Default@123'
 
 # Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}
 
 # Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers ,data="{'short_description':'Jenkins: Build Failed'}")
 
 # Check for HTTP codes other than 200
if response.status_code != 201: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()
 
 # Decode the JSON response into a dictionary and use the data
 
#print('Status:',response.status_code,'Headers:',response.headers,'Response:',response.json())
json_data = response.json()
print json_data['result']['number']
