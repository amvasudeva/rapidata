#!/usr/bin/bash

rm -rf /root/gitproject/petclinic
git clone http://10.75.50.26/root/Petclinic_reuse.git /root/gitproject/petclinic
cd /root/gitproject/petclinic
git checkout petclinic_feature_1.1  
git checkout petclinic_release  

cd /root/gitproject/petclinic
git remote set-url origin  http://10.75.50.26/root/Petclinic.git
git push -u origin master
git push -u origin petclinic_feature_1.1
git push -u origin petclinic_release

