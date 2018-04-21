# -*- conding:utf-8 -*-

class person :
    def __init__(self,name):
        self.name = name
    def say(self):
        print(self.__class__)
    def saywhat(self,do1,do2):
        dowhat = self.name + do1+do2
        print(dowhat)
p = person("hjh ")
speak1 = "Just do "
speak2 = "IT"
person.say(p)
p.saywhat(speak1,speak2)