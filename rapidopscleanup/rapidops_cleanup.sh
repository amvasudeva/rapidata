#!/usr/bin/bash

mysql -uwp -pwipro < db_cleanup.sql
echo "Database cleanup done."
sleep 5


python clean_git.py
echo "Cleanup git project."
sleep 5

sh create_petclinic_project.sh
echo "Create new git project."
sleep 5

#python delete_app.py
echo "Cleanup all the spawned instances."
