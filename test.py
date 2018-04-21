# -*- conding:utf-8 -*-
import os
import sys
import math

print(2 ** 2)
print("hello 沃德")

print(os.getcwd())
print(sys.argv)

num_list = {"aa":123,"bb":3}

num_list["aa"] = 223
print(num_list.__getitem__("aa"))