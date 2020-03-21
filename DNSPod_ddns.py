#!/usr/bin/env python
#-*- coding: utf-8 -*-

#first install requests module, run
# pip install requests

import socket
import requests


config = {
          'login_token':'tokenid,token', #add your own token
          'format':'json'
          'domain_id':'id',              #add your own domain_id
          'record_id':'id',              #add your own record_id
          'record_line_id':'0'
         }

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

def updateDNS(config,sub_domain,ip,record_type):
    config['sub_domain']=sub_domain
    config['value']=ip
    config['record_type']=record_type
    res = requests.post(url = 'https://dnsapi.cn/Record.Modify',data=config)
    print(res.text)
    
def ipv6DDNS(sub_domain):
    updateDNS(config,sub_domain,get_ipv6(),'AAAA')
    
def ipv4DDNS(sub_domain):
    updateDNS(config,sub_domain,get_ip(),'A')

ipv6DDNS('@') 
ipv6DDNS('www')
ipv4DDNS('abc')
    
