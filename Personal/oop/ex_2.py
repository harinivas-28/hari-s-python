'''
OOP Exercise 2: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
GIVEN-->
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
'''
class Vehicle:
    def __init__(self,name,max_speed,mileage) -> None:
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def drive(self):
        print(f"The {self.name} is Driving.")
    def stop(self):
        print(f"The {self.name} is Stopped.")
    def capacity(self,capacity):
        return f"This {self.name} has capacity of {capacity} people"
class Bus(Vehicle):
    pass
v1=Vehicle("Breeza",260,25)
b1=Bus("Volvo",290,16)
print(v1.name, v1.max_speed, v1.mileage)
print(v1.capacity(5))
v1.drive()
print(b1.name, b1.max_speed, b1.mileage)
print(b1.capacity(50))
b1.drive()
v1.stop()
b1.stop()

        