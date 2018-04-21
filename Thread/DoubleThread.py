# -*- conding:utf-8 -*-
import _thread
import time

def Clock(name,timePass):
    count = 0
    while 1:
         time.sleep(1)
         count += 1
         if count%timePass == 0 :
             print(name,"bling!!")
             count = 0
    pass

_thread.start_new_thread(Clock,("time is",1))
_thread.start_new_thread(Clock,("thread1",5))
_thread.start_new_thread(Clock,("thread2",3))

while 1:
    pass
