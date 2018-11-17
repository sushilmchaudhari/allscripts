#!/usr/bin/python

import httplib
import socket

#websiteurl='https://www.msri.org/web/cms' #enter your site url
websiteurl='www.msri.org'
path='/web/msri/about-msri1' #enter your site url
socketurl=websiteurl.split("/")[0]
print socketurl
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socketurl, 80))
except socket.error, e:
    if 'Connection refused' in e:
	print "Connection refused by server"

c=httplib.HTTPSConnection(websiteurl) #for ssl use httplib.HTTPSConnection.
c.request("HEAD", path)
STAT=c.getresponse().status
#REASON = c.getresponse().reason

#print REASON

print STAT
if STAT == 200 or STAT == 304:
    print "Website is up and running"

else:
    print "Website is down or not reachable"
