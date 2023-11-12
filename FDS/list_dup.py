l=[]
l_dup=[]
r=int(input("Enter length of list:"))
for x in range(0,r):
    m=int(input())
    l.append(m)
for i in l:
    if i not in l_dup:
        l_dup.append(i)
print(l_dup)