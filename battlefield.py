# -*- conding:utf-8 -*-

class Member():
    def __init__(self,name,sex,num):
        self.name = name
        self.sex = sex
        self.power = num

    def Battle(self,kill):
        if self.power + kill <= 0:
            return "over"
        else :
            self.power += kill
            return self.power
    def BattleInfo(self,info) :
        print("[" + self.name + "]"+info)
        if(self.power <= 0):
            print("阵亡")
    def MemberStatus(self):
        print("[" + self.name + "]")
        print("姓名:"+" "+ self.name)
        print("性别:"+" "+self.sex)
        print("战斗力:" + " d",self.power)

mb = Member("李涛","男",600)
mb.MemberStatus()
mb.BattleInfo("进入丛林作战，消耗战斗力200")
mb.Battle(-200)
mb.BattleInfo("修炼，增长战斗力100")
mb.Battle(100)
mb.BattleInfo("多人团战，消耗战斗力500")
mb.Battle(-500)
mb.MemberStatus()