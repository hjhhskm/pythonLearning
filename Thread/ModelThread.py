# -*- conding:utf-8 -*-

import _thread
import threading

class myThread(threading.Thread):

    def __init__(self,threadName,threadCount):
        threading.Thread.__init__(self)
        self.name = threadName
        self.count = threadCount
        pass

    def outtime(self,info):
        print(info)
        pass
    def run(self):
        print("启动线程")
        info = (self.name+"do",self.count)
        self.outtime(info)
        print("结束线程")
        pass

myThread("honey",999).start()
