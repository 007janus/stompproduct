#!/usr/bin/python
from logging.handlers import TimedRotatingFileHandler   
import logging   
import os   
import stomp
import sys
import time
  
class MyListener(object):   
    def on_error(self, headers, message):   
        print('received an error %s' % message)   
    def on_message(self, headers, message):
        print('----->received a message %s and header is %s' % (message,headers)) 
  
def main():            
    dest = '/queue/inbox'  
       
    conn = stomp.Connection(host_and_ports=[('127.0.0.1', 61612) ])   
    conn.set_listener('listen1', MyListener())   
    conn.start()   
    conn.connect()   
    conn.subscribe(destination=dest, id=1, ack='auto')
    print "waiting for a message"

    while 1:
        time.sleep(10)       
  
if __name__ == '__main__':   
    main()  
