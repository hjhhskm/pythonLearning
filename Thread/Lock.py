# -*- conding:utf-8 -*-
#condition 条件变量,lock = threading.Condition()
#wait使线程进入等待池
#notify唤醒线程
import _thread
import threading
import time

global count
count = 0

class yourThread(threading.Thread):
    def __init__(self,lock,name):
        threading.Thread.__init__(self)
        self.lock = lock
        self.name  = name
        pass
    def doSomeThing(self,something):
        print(self.name+"do something at",something)
        pass
    def run(self):
        while 1:
            global count
            count += 1
            if self.lock.acquire():
                self.doSomeThing(count)
                self.lock.release()
            time.sleep(1)
            pass

    pass
lock=threading.Lock()

t1 = yourThread(lock,"t3")
t1.start()

t2 = yourThread(lock,"t2")
t2.start()

t1.join()
t2.join()