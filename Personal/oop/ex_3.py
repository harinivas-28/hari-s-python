'''
OOP Exercise 3: Class Inheritance
Given:

Create a Bus child class that inherits from the Vehicle class. 
The default fare charge of any vehicle is seating capacity * 100. 
If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
'''
class Vehicle:
    def __init__(self,name,capacity,mileage):
        self.name=name
        self.capacity=capacity
        self.mileage=mileage
    def fare(self):
        return self.capacity*100
class Bus(Vehicle):
    def fare(self):
        amount=super().fare()
        amount+=10*amount/100
        return amount
v1=Vehicle("BMW",5,12)
print(f"name={v1.name} capacity={v1.capacity} mileage={v1.mileage}")
print(f"Fare={v1.fare()}")
b1=Bus("Volvo",50,16)
print(f"name={b1.name} capacity={b1.capacity} mileage={b1.mileage}")
print(f"Fare={b1.fare()}")

    