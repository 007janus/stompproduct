#!/usr/bin/python
#coding:utf-8

"""
    自己重写Thread类，注意在继承的时候，需要继承超类(threading.Thread)的构造方法
    需要完成的任务在run方法中去实现，比较灵活
    当start()的时候，开始执行
"""
import threading
from time import sleep, ctime

loops = (4, 2)

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