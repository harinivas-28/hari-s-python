l1=[]
l2=[]
common=[]
r=int(input("Enter length of list 1:"))
for x in range(0,r):
    m=int(input())
    l1.append(m)
p=int(input("Enter length of list 2:"))
for q in range(0,p):
    s=int(input())
    l2.append(s)
for i in l1:
    if i in l2 and i not in common:
        common.append(i)
print(common)

