class box:
    def __init__(self , l ,b):
        self.l=0
        self.b=0
    def area(self, l,b):
        return l*b

a = box(10,20)
print(a.area(10,20))
