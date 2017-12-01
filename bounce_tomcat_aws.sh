#!/bin/bash
ssh  -o "StrictHostKeyChecking no" -i /root/wiprodublin.pem centos@$1 sudo systemctl restart tomcat
