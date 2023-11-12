class Operations:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        a=self.x+other.x
        b=self.y+other.y
        return a,b
    def __sub__(self,other):
        a=self.x-other.x
        b=self.y-other.y
        return a,b
    def __mul__(self,other):
        a=self.x*other.x
        b=self.y*other.y
        return a,b
    def __pow__(self,other):
        a=self.x**other.x
        b=self.y**other.y
        return a,b
o1=Operations(12,16)
o2=Operations(18,14)
print(o1+o2)
print(o1-o2)
print(o1*o2)
print(o1**o2)
