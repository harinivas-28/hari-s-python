""" Write a program to concatenate two dictionaries

Sample input:

3                                                                                                                       
1:a                                                                                                                     
2:e                                                                                                                     
3:f                                                                                                                     
2                                                                                                                       
a:1                                                                                                                     
e:2

Sample output:
{'1': 'a', '2': 'e', '3': 'f', 'a': '1', 'e': '2'} """

# Write your code here
d1={}
d2={}
a=int(input())
for i in range(a):
    keys=input()
    values=input()
    d1[keys]=values
b=int(input())
for i in range(b):
    keys=input()
    values=input()
    d2[keys]=values
d3={**d1,**d2}
print(d3)

    