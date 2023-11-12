#2.Define a function which prints the sum if a square of a number
"""
eg:1897
1+64+81+49=???
"""
n=int(input("Enter number:"))
def squaresSum(n):
    z=0
    while(n!=0):
        r=n%10
        z=z+(r**2)
        n=n//10
    return z
z=squaresSum(n)
print(z)


