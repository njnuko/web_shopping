#!/usr/bin/env python
import urllib
import urllib.request


LOGIN = 'name'
PASSWD = "passwd"
URL = 'https://account.xiaomi.com/pass/serviceLogin?'
REALM = 'Secure Archive'


def handler_version(url):
    from urllib import parse as urlparse
    hdlr = urllib.request.HTTPBasicAuthHandler()
    hdlr.add_password(REALM,urllib.parse.urlparse(url)[1],LOGIN,PASSWD)
    opener = urllib.request.build_opener(hdlr)
    urllib.request.install_opener(opener)
    return url

def request_version(url):
    from base64 import encodestring
    req = urllib.request.Request(url)
    print('--------------------------------')
    ko = ('%s:%s' % (LOGIN,PASSWD))
    print(ko)
    ko = bytes(ko, encoding = "utf8")  
    #b64str = encodestring('%s:%s' % (LOGIN,PASSWD))[:-1]
    b64str = encodestring(ko)[:-1]
    print('--------------------------------')
    req.add_header("Authorization","Basic %s" % b64str)
    return req

for funcType in ('handler','request'):
    print('*** Using %s:' % funcType.upper())
    url = eval('%s_version' % funcType)(URL)
    print(url)
    print('xxxxxx')
    f = urllib.request.urlopen(url)
    for line in f.readlines():
        print(line.decode('utf8'))
    f.close()
