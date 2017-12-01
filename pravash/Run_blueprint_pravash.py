#!/usr/bin/env python

import sys
import requests,json
from time import sleep

host="10.75.50.25"
auth=("wiprocoe","Coeadmin@123")
error_message = "calm script failed"

old_status = "PENDING"

status_msg_map = {
    "PENDING": "Preparing flow {}.",
    "RUNNING": "Running flow {}.",
    "APPROVAL": "Flow {} is waiting for human approval.",
    "SUCCESS": "Flow {} finished successfully.",
    "FAILURE": "Flow {} failed.",
}

def check_app_status(application_name, app_run_id):
    global old_status

    headers = {'Content-Type': 'application/json'}
    payload = {
    "application_name": "tomcat3-aws",
    }
    #http://10.75.50.25/public/api/1/default/blueprints/run
    url = "http://10.75.50.25/public/api/1/default/applications/search"
    #url = "http://10.75.50.25/public/api/1/default/applications"
    r = requests.post(url, auth=auth, json=payload, headers=headers)
    #r = requests.get(url, auth=auth, headers=headers)
    print r.status_code
    print "jumped"
    print r.text
    if not r.ok:
        print >> sys.stderr, error_message
        sys.exit(-1)
    print "crossed"
    print r.json()
    status = r.json()['data']['rows'][0]['state']
    print "-----------"
    print status
    return status


def start_flow_run(blueprint_name, application_name):

    url = "http://10.75.50.25/public/api/1/default/blueprints/run".format(host)
    headers = {'Content-Type': 'application/json'}

    payload = {
    "blueprint_name": blueprint_name,
    "application_name": application_name,
    "team_name": "Administrator Team",
    "budget_name": "Budget1"
    }
    print url
    #r = requests.post(url, auth=auth, data=json.dumps(payload), headers=headers)
    r = requests.post(url, auth=auth, json=payload, headers=headers)
    print r.status_code
    print r.json()
    app_run_id = r.json()['data']['row']['application_uid']
    print "Inside app\n"
    print app_run_id
    print "Inside app\n"
    sys.exit(0)
    if r.status_code != 200:
        print >> sys.stderr, r.status_code, error_message
        sys.exit(-1)

    return app_run_id


def main():
    global old_status

    blueprint_name = sys.argv[2]
    application_name = sys.argv[4]

    #app_run_id = start_flow_run(blueprint_name, application_name)
    app_run_id = "5735a0949526b50a7241e7f0" 
    while True:

        current_status = check_app_status(application_name, app_run_id)
        print "Main"+current_status
        if current_status == "SUCCESS":
            data=requests.get("http://10.75.50.25/public/api/1/default/applications/{}/machine_status".format(host,app_run_id),auth=auth)
	    print data.status_code
  	    if data.status_code != 200:
        	print "Error fetching data"
  		sys.exit(1)
	    print "HOST={}".format(data.json()['data']['rows'][0]['address'])
	    print "APP_ID={}".format(app_run_id)
            sys.exit(0)
        elif current_status == "FAILURE":
            sys.exit(-1)

        sleep(10)

if __name__ == "__main__":
    main()


