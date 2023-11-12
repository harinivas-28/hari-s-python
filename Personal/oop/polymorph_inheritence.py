class Car:
    def __init__(self,brand,name) -> None:
        self.brand=brand
        self.name=name
    def drive(self):
        return f"{self.name} is to Drive !"
class Boat(Car):
    def sail(self):
        return f"{self.name} is to Sail !"
class Plane(Car):
    def flight(self):
        return f"{self.name} is to Fly !"
c1=Car("Toyota","Innova")
b1=Boat("SpeedBoat","Titan")
p1=Plane("Airlines","SpiceJet")
for i in (c1,b1,p1):
    print(i.brand+'-'+ i.name,end="-->")
    if i==c1:
        print(i.drive())
    elif i==b1:
        print(i.sail())
    else:
        print(i.flight())
