#!/usr/bin/python

import subprocess

cmd_out = subprocess.check_output(['ps','-ef'])
users = {}

for line in cmd_out.splitlines()[1:]:
	user = line.split()[0]
	users[user] = users.get(user,0)+1
print users
z = { 'aaa':'', 'bbb':6 }
#users.update(z)
#print users
y=users.get('aa3',10)
print users.items() 

c = users.copy()

#c.update(z)
#print 151 in users.values()
dict = {}
file_object = open('../openstack_env',"r" )
data = file_object.read()
for line in data.splitlines()[1:]:
    (em, line) = line.split(' ')
    (key,val) = line.split('=')
    dict.update({key:val})

print dict
file_object.close()


file_object = open('/root/pravash/ashwin/temptest',"a+" )
file_object1 = open('../openstack_env',"r" )
file_object.write(file_object1.read());
file_object1.close()
file_object.close()


