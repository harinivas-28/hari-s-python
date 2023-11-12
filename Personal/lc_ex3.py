'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
#CODE

l1=[]
l2=[]
l3=[]
a=int(input("Enter length of List 1: "))
b=int(input("Enter length of List 2: "))
for i in range(a):
    m=int(input())
    l1.append(m)
print(l1)
for i in range(b):
    n=int(input())
    l2.append(n)
print(l2)
for i in range(0,a):
    k=l1[a-i-1]+l2[a-i-1]
    l3.append(k)
print(l3)
l4=[]
for i in range(len(l3)):
    r=l3[len(l3)-i-1]
    l4.append(r)
print(l4)