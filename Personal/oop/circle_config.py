class Circle:
    pi=3.141592
    def __init__(self,radius):
        self.radius=radius
    def circum(radius):
        return 2* Circle.pi* radius
    def area(radius):
        return Circle.pi * radius* radius
radius=int(input("Enter Radius: "))
print(f"Area={Circle.circum(radius)}\nPerimeter={Circle.area(radius)}")
