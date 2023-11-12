l=[]
r=int(input("Enter length of list:"))
for x in range(0,r):
     b=int(input())
     l.append(b)
unsorted=0
for i in range(1,len(l)):
    if l[i] >= l[i-1]:
        pass
    else:
        print("List is not sorted")
        unsorted=1
        break
if unsorted ==0:
        print("List is sorted")
