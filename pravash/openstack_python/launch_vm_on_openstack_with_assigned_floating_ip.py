#!/usr/bin/python
import time    #used to add sleep before assigning floating ip

#requests against the nova-api endpoint by instantiating a novaclient.v1_1.client.Client object
from novaclient.v1_1 import client

#Creating the nova object after connecting to the NOVA API EndPoint
ncreds = client.Client(auth_url="http://10.207.231.120:5000/v2.0", username="demo",api_key="coeadmin", project_id="demo")

#Pick a floating ip from the list of floating ips and create the object
floating_ip =  ncreds.floating_ips.create( ncreds.floating_ip_pools.list()[0].name)

#Create a new vm using the nova object created above by passing required type of VM
server = ncreds.servers.create(name = "Puppet-Machine", image = "4d962fac-49a1-4dcb-82a0-c6f1f3053739", flavor = 3, nics = [{'net-id':'d85ffdf1-4000-42ed-bbb9-d5b396df71da'}])

#Sleep for some time until VM is created 
time.sleep(20)

#Assign floating ip to the newly spawned vm
server.add_floating_ip(floating_ip)

#Print the floating ip assigned to the vm
print floating_ip.ip
