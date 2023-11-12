l=[]
l_dup=[]
r=int(input("Enter length of list:"))
for x in range(0,r):
    m=int(input())
    l.append(m)
for i in l:#looping through list
    n=l.count(i)#number of times the number is repeating
    if n>1:
        for a in range(0,n-1):#looping 1 time less than the repeating
            l.remove(i)#removing the number 1 time less than its repeating
print(l)