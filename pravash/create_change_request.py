#! /usr/bin/python
#Need to install requests package for python
#sudo easy_install requests
import requests

 # Set the request parameters
#url = 'https://wiprodemo.service-now.com/api/now/table/change_request'
url = 'https://wiprodemo2.service-now.com/api/now/table/change_request'
#user = 'Default'
user = 'tali'
pwd = 'tali@123'

 # Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

 # Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers ,data="{'short_description':'Approval requested to promote the build', 'type': 'DevOps', 'u_requesttype': 'Promote and Merge request', 'state': '0','assignment_group':'Wipro Technologies Ltd', 'close_code':'successful', 'close_notes':'Reviewed, ready for merge. Reviewed all changes, good to merge.'}")

 # Check for HTTP codes other than 200
if response.status_code != 201:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

 # Decode the JSON response into a dictionary and use the data

#print('Status:',response.status_code,'Headers:',response.headers,'Response:',response.json())
json_data = response.json()
print json_data['result']['sys_id']
#print json_data['result']['number']
