class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def drive(self):
        print(f"{self.model} is Driving.")
    def stop(self):
        print(f"{self.model} is Stopped.")
#Class are similar to Structures in C Programming
car_1=Car('Toyota','Supra')
print(car_1.brand,end=" ")
print(car_1.model)
car_1.drive()
car_2=Car('Nissan','GTR Skyline')
print(car_2.brand,end=" ")
print(car_2.model)
car_2.drive()
car_1.stop()
car_2.stop()
#Class is like Stuct Structure name in C programming
#__init__ is a function used to declare variables(attributes)
# self is used when a member is called to access its variables


