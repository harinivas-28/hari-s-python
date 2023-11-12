"""
input=[1,2,3]
l2=[3,2,1]
output=[4,4,4]
"""
l=[]
t=l.copy()
l2=[]
n=int(input())
for i in range(n):
    x=int(input())
    l.append(x)
l.reverse()
print(l)
while i<=len(l):
    y=t[i]+l[i]
    l2.append(y)
    i+=1
print(l2)
