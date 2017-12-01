#!/usr/bin/env python
import os
 
def get_keystone_creds():
    d = {}
    d['username'] = os.environ['demo']
    d['password'] = os.environ['coeadmin']
    d['auth_url'] = os.environ['http://10.207.231.120:5000/v3']
    d['tenant_name'] = os.environ['demo']
    return d
 
def get_nova_creds():
    d = {}
    d['username'] = os.environ['demo']
    d['api_key'] = os.environ['coeadmin']
    d['auth_url'] = os.environ['http://10.207.231.120:5000/v2.0']
    d['project_id'] = os.environ['demo']
    return d
