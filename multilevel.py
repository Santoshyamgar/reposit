class grandfather:
    def fun1(self):
        print("grand father name")


class father(grandfather):
    def fun2(self):
        print("father name")

class son(father):
    def fun3(self):
        #print("grandfather name")
        #print("father name")
        print("son name")
s1 = son()
s1.fun3()
s1.fun2()
s1.fun1()
grandfather()




