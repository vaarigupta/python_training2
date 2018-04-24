class test:
    pass
class demo(test):
    pass
class bla():
    pass
b = bla()
c =test()
ob = demo()
p= isinstance(ob , demo) # ob is object and demo is class
q=isinstance(ob , test)
r = isinstance(ob , bla)
print(p ,q , r)
