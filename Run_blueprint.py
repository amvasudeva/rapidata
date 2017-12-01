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

    url = "http://{}/api/1/default/applications/{}".format(host,app_run_id)
    r = requests.get(url, auth=auth)
    print r
    if not r.ok:
        print >> sys.stderr, error_message
        sys.exit(-1)

    status = r.json()['data']['row']['state']

    return status


def start_flow_run(blueprint_name, application_name):

    url = "http://{}/public/api/1/default/blueprints/run".format(host)
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

    print "\nInside Function\n"
    print url

    payload = {
    "blueprint_name": blueprint_name,
    "application_name": application_name,
    "team_name": "Administrator Team"
    }
    print payload
    print auth
    #r = requests.post(url, params=auth, data=json.dumps(payload), headers=headers)
    ###r = requests.post(url, auth=auth, data=json.dumps(payload), headers=headers)
    #r = requests.post(url, auth=auth,  headers=headers, data=json.dumps(payload))
    r = requests.post(url, auth=("wiprocoe","Coeadmin@123"))
    print r.url
    print r.status_code, r.reason
    print r
    exit

    app_run_id = r.json()['data']['row']['application_uid']
    print app_run_id 
    exit 

    if not r.ok:
        print >> sys.stderr, error_message
        sys.exit(-1)

    return app_run_id


def main():
    global old_status

    blueprint_name = sys.argv[2]
    application_name = sys.argv[4]
    blueprint_name = blueprint_name.strip('\n\r')
    application_name = application_name.strip('\n\r')
    print(blueprint_name+application_name)

    app_run_id = start_flow_run(blueprint_name, application_name)
    print app_run_id

    while True:

        current_status = check_app_status(application_name, app_run_id)
        if current_status == "SUCCESS":
            data=requests.get("http://{}/api/1/default/applications/{}/machine_status".format(host,app_run_id),auth=auth)
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


