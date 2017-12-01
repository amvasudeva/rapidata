#!/usr/bin/python

import gitlab
from time import sleep


# or username/password authentication
gl = gitlab.Gitlab('http://10.75.50.26', email='root', password='coeadmin')

# make an API request to create the gl.user object. This is mandatory if you
# use the username/password authentication.
gl.auth()

projects = gl.projects.list()
for project in projects:
    if(project.name == "Petclinic"):
        print "About to delete"+project.name
	project.delete()


sleep(5) # Time in seconds
p = gl.projects.create({'name': 'Petclinic'}, sudo='root')
