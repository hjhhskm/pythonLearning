# -*- conding:utf-8 -*-

class Car():
    def Drive(self):
        print("开车")
        pass
    def Close(self):
        print("下车")
        pass

class Honda(Car):
    pass

civic = Honda()
civic.Drive()