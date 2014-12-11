#!/usr/bin/python
#coding:utf-8
import threading
from time import sleep, ctime
import os

loops = (4,2)

class MyThread(threading.Thread):
    """docstring for MyThread"""
    def __init__(self, func, args, name=""):
        super(MyThread, self).__init__()
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print "start loop", nloop, 'at:', ctime()
    os.system('telnet 127.0.0.1 22')
    sleep(nsec)
    print "loop", nloop, "done at:", ctime()

def main():
    print "starting at:", ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

if __name__ == '__main__':
    main()
