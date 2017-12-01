#!/usr/bin/python

import re

file_obj = open("/root/pravash/ashwin/temptest","r")
data = file_obj.read()

print re.findall(r"\texport OS_PASSWORD", data)
file_obj.close()
