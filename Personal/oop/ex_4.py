from datetime import date
class Person:
    def __init__(self,name,country,dob) -> None:
        self.name=name
        self.country=country
        self.dob=dob
    def age(self):
        today = date.today()
        age = today.year - self.dob.year
        if today < date(today.year, self.dob.month, self.dob.day):
            age -= 1
        return age
p1=Person("Jhonny","India",date(1990,12,12))
print(p1.name, p1.country, p1.dob)
print(p1.age())
