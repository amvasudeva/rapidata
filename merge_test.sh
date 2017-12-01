#!/usr/bin/sh

#Getinto the git local repo
cd /root/gitproject/petclinic

#Checkout the feature branch
git checkout petclinic_feature_1.1 
git pull  #Pull the latest code

sleep 2 

#checkout the release branch
git checkout petclinic_release 
git pull #Pull the latest code


sleep 2 

#Steps to merge the code
#command to merge the feature branch into the release branch
git merge  petclinic_feature_1.1 -m "merge petclinic_feature_1.1 branch back into petclinic_release"
#Commit the code after the merge
git commit -m 'merged branches merge petclinic_feature_1.1 into petclinic_release'
#Push the code to github
git push
