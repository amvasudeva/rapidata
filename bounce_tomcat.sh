#!/bin/bash
sshpass -p "coeadmin" ssh  -o "StrictHostKeyChecking no" root@$1 'sudo echo "JAVA_OPTS=-Djava.security.egd=file:/dev/./urandom" >> /usr/share/tomcat/conf/tomcat.conf'
sshpass -p "coeadmin" ssh  -o "StrictHostKeyChecking no" centos@$1 sudo systemctl restart tomcat
sshpass -p "coeadmin" ssh  -o "StrictHostKeyChecking no" root@$1 'nohup java -jar /usr/local/appdynamics_machine_agent/machineagent.jar > /dev/null &'
#sed -i "/8080/c\\\t server $1:8080\;" /etc/nginx/nginx.conf
#systemctl reload nginx
