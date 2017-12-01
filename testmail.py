#! /usr/bin/python

import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

# me == the sender's email address
# you == the recipient's email address
Subject = 'The contents of mail'
From = 'root@localhost'
To = 'admin@devops.com'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail('root@localhost', 'otrs@ec5otrs.devops.local,admin@devops.com', 'TEST MAIL')
s.quit()
