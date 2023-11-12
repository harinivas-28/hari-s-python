""" Write a program to map two lists into a dictionary

Sample input:

3                                                                                                                       
a                                                                                                                       
b                                                                                                                       
c                                                                                                                       
1                                                                                                                       
32                                                                                                                      
6 

Sample output:

{'a': '1', 'b': '32', 'c': '6'}  """

# Write your code here
d={}
l1=[]
l2=[]
x=int(input())
for i in range(x):
    a=input()
    l1.append(a)
print(l1)
for i in range(x):
        b=input()
        l2.append(b)
print(l2)
for i in range(x):
      d[l1[i]]=l2[i]
print(d)
    