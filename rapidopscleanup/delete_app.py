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


def start_flow_run():
    url_app_list = "http://{}/public/api/1/default/applications".format(host)
    headers = {'content-type': 'application/json'}
    r = requests.get(url_app_list, auth=auth,  )
    results = []
    for i in range(len(r.json()['data']['rows'])):
        instance_name = r.json()['data']['rows'][i]['name'] 
	headers = {'content-type': 'application/json'}
	payload = {
            "application_name": instance_name,
        }
	url_del_app = "http://{}/public/api/1/default/applications/delete".format(host,instance_name)
	data=requests.post(url_del_app, auth=auth, data=json.dumps(payload), headers=headers)
	print "Instance "+ instance_name + " deleted"
	results.append(instance_name);
	if data.status_code != 200:
	    print "Error fetching data"
	    sys.exit(1)

    if not r.ok:
        print >> sys.stderr, error_message
        sys.exit(-1)

    return results;


def main():
    print "Ready to delete all spawned instances"
    app_name = start_flow_run()
	
if __name__ == "__main__":
    main()
