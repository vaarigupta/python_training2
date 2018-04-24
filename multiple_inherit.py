
## it is multilevel inheritance
class father():
    def skill2(self):
        print(" father is accountant")

class mother():
    def skill3(self):
        print(" mother is housewife")

class child (father , mother):
    def skill4(self):
        print(" child is doctor")

c = child()
c.skill4()
c.skill2()
c.skill3()
