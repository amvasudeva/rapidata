#!/bin/bash

curl -v -H "Content-Type: application/xml" -X PUT --data  "@status.xml" -u root:coeadmin http://10.75.50.39/issues/8.xml
curl -v -H "Content-Type: application/xml" -X PUT --data  "@status.xml" -u root:coeadmin http://10.75.50.39/issues/5.xml

JOB_URL=http://10.75.50.23:8080/job/petclinic
JOB_STATUS_URL=http://10.75.50.23:8080/job/petclinic/lastBuild/api/json

# Set a variable to true
GREP_RETURN_CODE="True"

# Start the build
curl --user admin:coeadmin http://10.75.50.23:8080/job/petclinic/build

# Poll every thirty seconds until the build is finished
while [ $GREP_RETURN_CODE == "True" ]
do
    sleep 20 
    # curl will return the json string and python part will parse the json string and return only the value for the key building(true/false)
    GREP_RETURN_CODE=`curl --silent http://10.75.50.23:8080/job/petclinic/lastBuild/api/json | python -c "import sys, json; print json.load(sys.stdin)['building']"`
done


STATUS_CODE=`curl --silent http://10.75.50.23:8080/job/petclinic/lastBuild/api/json | python -c "import sys, json; print json.load(sys.stdin)['result']"`
#echo $STATUS_CODE

if [ $STATUS_CODE == "FAILURE" ] 
then

#python /root/pravash/createincident.py
curl -v -H "Content-Type: application/xml" -X POST --data-binary "@issue.xml" -u root:coeadmin http://10.75.50.39/issues.xml
exit 1;

else

BUILD_NUMBER=`curl --silent http://10.75.50.23:8080/job/petclinic/lastBuild/api/json | python -c "import sys, json; print json.load(sys.stdin)['number']"`
echo $BUILD_NUMBER

fi
