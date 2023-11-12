#1.Define a function which prints all the factors of a number.
"""
eg:12
1,2,3,4,6,12
"""
l=[]
def factors():
    for i in range(1,n+1):
        if(n%i==0):
            l.append(i)
n=int(input("Enter number:"))
def plist():
    for i in l:
        print(i,end=" ")
factors()
plist()