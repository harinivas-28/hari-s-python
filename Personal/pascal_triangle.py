'''n=int(input())
for i in range(n):
    for j in range(n-i):
        print(end=" ")
    coef=1
    for j in range(i+1):
        print(coef,end=" ")
        coef*=(i-j)//(j+1)
    print()
'''
from math import factorial
n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
    print()