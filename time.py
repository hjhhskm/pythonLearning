# -*- conding:utf-8 -*-

import time

nowtime = time.localtime()
def func() :
    list = [1,2,3]
    # list[1] = 10
    # list[2] = 20
    return list
a_list = func();
print(a_list[1])

def bi():
    zhangjb = 10
    def bao():
        dong = 20
        return zhangjb + dong
    return bao
print(bi()())

