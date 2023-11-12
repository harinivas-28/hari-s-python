n=int(input())
l=[]
for i in range(n):
    k=input()
    l.append(k)
w=input()
o=int(input())
c=0
x=-1
for i in l:
    x=x+1
    if(i==w):
        c=c+1
        if(c==o):
            j=i
    else: pass
l.pop(j)
print(l)
