#!/usr/bin/python
from sys import exit
from time import sleep
import requests
for i in range(30):
    try:
        resp = requests.get('http://server:8000/ping')
        if resp.status_code == 200:
            print "Smoketest Successful!"
            exit(0)
        else:
            print "Bad status on attempt %i: %i" % (i, resp.status_code)
    except Exception as e:
        print "Fail on attempt %i: %s" % (i, e)
    sleep(1)

exit(1)
