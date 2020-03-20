#!/usr/bin/env python
#-*- coding: utf-8 -*-

#first install requests module, run
# pip install requests

import socket
import requests

def get_ipv6():
    sock = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
    sock.connect(('2001:4860:4860::8888',80))
    ip = sock.getsockname()[0]
    sock.close()
    return ip
    
def get_ip():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.connect(('8.8.8.8',80))
    ip = sock.getsockname()[0]
    sock.close()
    return ip

url = 'https://dnsapi.cn/Record.Modify'

data = {'login_token':'tokenid,token', #add your own token
        'format':'json',
        'domain_id':'id',              #add your own domain_id
        'record_id':'id',              #add your own record_id
        'sub_domain':'www',            #change your intended sub_domain
        'value':get_ip(),              #use get_ipv6() for ipv6
        'record_type':'A',             #AAAA for ipv6
        'record_line_id':'0'}
        
res = requests.post(url=url,data=data)
print(res.text)
