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


def start_flow_run(blueprint_name, application_name):

    url = "http://{}/public/api/1/default/blueprints/run".format(host)
    headers = {'content-type': 'application/json'}

    payload = {
    "blueprint_name": blueprint_name,
    "application_name": application_name,
    "team_name": "Administrator Team",
    "budget_name":"Budget1"
    }
    r = requests.post(url, auth=auth, data=json.dumps(payload), headers=headers)
    app_run_id = r.json()['data']['row']['application_uid']

    if not r.ok:
        print >> sys.stderr, error_message
        sys.exit(-1)

    return app_run_id

def infrafile():
        is_file_exits = os.path.exists('/root/pravash/infra.conf')   #Check if file exists
        if is_file_exits:
	    os.remove('/root/pravash/infra.conf')

        os.system( 'wget https://raw.githubusercontent.com/pravashchoubey/Petclinic/master/infra.conf  > /dev/null 2>&1' )
        config = ConfigParser.ConfigParser()
        config.read('/root/pravash/infra.conf')
        return config


def main():
    global old_status

    configuration = infrafile()

    blueprint_name1 = configuration.get('DEFAULT','CLOUD') + configuration.get('DEFAULT','FLAVOUR') + configuration.get('DEFAULT','OS') + configuration.get('DEFAULT','OS_VERSION') + 'JDK' + configuration.get('DEFAULT','JDK_VERSION') + configuration.get('DEFAULT','WEB_SERVER') + configuration.get('DEFAULT','WEB_SERVER_VERSION')  
    blueprint_name = blueprint_name1.replace('.', '')
    timestr = time.strftime("%Y-%m-%d %H-%M-%S")
    from datetime import datetime
    application_name = configuration.get('DEFAULT','APPLICATION_NAME')  + '_' + configuration.get('DEFAULT','REQUESTER') + '_' + datetime.now().strftime("%a%d%b%Y %H-%M-%S") 

    #blueprint_name = sys.argv[2]
    #blueprint_name = vm_name 
    #application_name = sys.argv[4]
    #application_name = app_name

    app_run_id = start_flow_run(blueprint_name, application_name)

    while True:

        current_status = check_app_status(application_name, app_run_id)
        if current_status == "SUCCESS":
            data=requests.get("http://{}/api/1/default/applications/{}/machine_status".format(host,app_run_id),auth=auth)
  	    if data.status_code != 200:
        	print "Error fetching data"
  		sys.exit(1)
	    print format(data.json()['data']['rows'][0]['address'])
	    #hostip=format(data.json()['data']['rows'][0]['address'])
	    #print hostip	
	   # print "APP_ID={}".format(app_run_id)
            sys.exit(0)
        elif current_status == "FAILURE":
            sys.exit(-1)

        sleep(10)

if __name__ == "__main__":
    main()


