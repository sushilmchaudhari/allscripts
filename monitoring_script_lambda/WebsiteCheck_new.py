#!/usr/bin/python

import httplib2
import socket

#websiteurl='https://www.msri.org/web/cms' #enter your site url
websiteurl='staging' #enter your site url
socketurl=websiteurl.split("/")[2]
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socketurl, 80))
except socket.error, e:
    if 'Connection refused' in e:
	print "Connection refused by server"

h = httplib2.Http(".cache")
#resp, content = h.request("https://www.google.com", "GET")
h.force_exception_to_status_code = True
resp, content = h.request(websiteurl, "GET")

STAT=resp.status
REASON = resp.reason

print REASON

print STAT
if STAT == 200 or STAT == 304:
    print "Website is up and running"

else:
    print "Website is down or not reachable"
