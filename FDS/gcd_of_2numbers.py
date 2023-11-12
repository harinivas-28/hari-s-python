""" Write a program to find the GCD of given two numbers

Sample input:
input=12                                                                                                                      
16

Sample output=The GCD of 12 and 16 is: 4 

Sample input=2                                                                                                                       
18

Sample output=The GCD of 2 and 18 is: 2   """

# Write your code here
import math
a=int(input())
b=int(input())
c=math.gcd(a,b)
print(f"The GCD of {a} and {b} is: {c}")