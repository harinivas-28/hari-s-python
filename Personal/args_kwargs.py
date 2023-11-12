# *args are the arguments which take any number of arguments and store in a tuple
# **kwargs are also the arguments which take specific keyword arguments and store in a dictionary
def add(*numbers):
    sum=0
    for i in numbers:
        sum += i
    print(f"sum = {sum}")
add(2,3)
add(4,5,2,45,2)
add(4.5,6.124,9.75,5)
def greet(**names):
    print(names)
greet(name="Hari",age=18,branch="AIML")
#when using them as an arguments *args are used first and then **kwargs otherwise it will give error
def combine(*numbers,**names):
    for i in numbers:
        print(f"roll no : {i}")
    print(names)
combine(79,7136,name1="hari",name2="LifeLine")
