
#!/usr/bin/env python

import sys
import requests, json
import subprocess


url = 'http://10.75.50.23:8080/job/petclinic/lastBuild/api/json'
r = requests.get(url)


out_str = r.text
data = json.loads(out_str)
status = data['result']

if status != 'SUCCESS' :
	process = subprocess.Popen(['/root/pravash/build_email_bugzilla.sh'])



