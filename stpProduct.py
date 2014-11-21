#!/usr/bin/python
from logging.handlers import TimedRotatingFileHandler   
import logging   
import os   
import stomp
import sys
import time
from socket import *
import struct
def main(msg):            
    dest = '/queue/inbox'  
       
    conn = stomp.Connection(host_and_ports=[('127.0.0.1', 61612)])
    conn.start()   
    conn.connect()   
    conn.send(body=msg, destination=dest)
    print 'send message ', msg
def TcpClient(ip,port):
    client=socket(AF_INET, SOCK_STREAM)
    client.connect((ip,port))

    while True:
        dataheader=client.recv(12)
        if len(dataheader) >= 12:
            dataheader=struct.unpack('IIf',dataheader[:12])
            data=[str(dataheader[0]),str(dataheader[1]),str(dataheader[2])]
            print data
            if dataheader[1] == 0:
                print 'alive'
#                main(''.join(data))
            else:
                data=client.recv(dataheader[1])
		main(data)
		print len(data)
                print data

TcpClient('10.9.0.104',41900)
  
  
