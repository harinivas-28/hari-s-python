'''
OOP Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
'''
class Vehicle:
    def __init__(self,brand,max_speed,mileage) -> None:
        self.speed=max_speed
        self.mileage=mileage
        self.brand=brand
        print(brand, max_speed, mileage)
v1=Vehicle("Buggati",324,12)
v2=Vehicle("Chevorlet",315,13)
