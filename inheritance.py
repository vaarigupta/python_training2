class parent:
    def __init__(self , shape):
        
    def name(self, shape):
        print("shape :%s " % shape )


class square(shape):
    def area(self , side):
        return side**2

a = parent.name("square")   
