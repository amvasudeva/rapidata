#!/usr/bin/env python

import sys
import requests,json
from time import sleep
import time

import random
import string

import os.path   #Check if file exists - has function exists
import ConfigParser

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

    if not r.ok:
        print >> sys.stderr, error_message
        sys.exit(-1)

    status = r.json()['data']['row']['state']

    return status


def start_flow_run():

    url = "http://{}/public/api/1/default/applications".format(host)
    headers = {'content-type': 'application/json'}

    r = requests.get(url, auth=auth,  )
    results = []
    for i in range(len(r.json()['data']['rows'])):
        results.append( r.json()['data']['rows'][i]['name'] )


    if not r.ok:
        print >> sys.stderr, error_message
        sys.exit(-1)

    return results;



def main():
    global old_status


    app_name = start_flow_run()

    headers = {'content-type': 'application/json'}

    payload = {
    "application_name": name,
    }

    url = "http://{}/public/api/1/default/applications/delete".format(host,name)

    for name in range(len(app_name)):
        data=requests.post(url, auth=auth,data=json.dumps(payload), headers=headers)
        if data.status_code != 200:
            print "Error fetching data"
            sys.exit(1)

    #data=requests.post(url, auth=auth,data=json.dumps(payload), headers=headers)


if __name__ == "__main__":
    main()


