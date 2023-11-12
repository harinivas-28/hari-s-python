""" Python program to print prime numbers between the given two numbers

Sample input:
2                                                                                                                       
100

Sample output=
Prime numbers between 2 and 100 are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] 

Sample input=50                                                                                                                      
15                                                                                                                      

Sample output=Invalid range. The starting number should be less than the ending number and both should be positive.   """

# Write your code here
a=int(input())
b=int(input())
t=a
primes=[]
if a<b and a>=0 and b>=0:
    if a==1 or a==0:
        a=2
        for n in range(a,b):
            for i in range(2,n):
                if n%i==0:
                    break
            else:
                primes.append(n)
        print(f"Prime numbers betweeen {t} and {b} are: {primes}")
else:
    print("Invalid range. The starting number should be less than the ending number and both should be positive.   ")