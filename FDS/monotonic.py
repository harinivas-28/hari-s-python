n=int(input("Enter length of Array:"))
l=[]
print("Enter values into the Array")
for i in range(n):
    k=int(input())
    l.append(k)
def increasing():
    for i in range(len(l)-1):
        if(l[i]<=l[i+1]):
            pass
        else: return False
    return True
def decreasing():
    for i in range(len(l)-1):
        if(l[i]>=l[i+1]): pass
        else: return False
    return True
if(increasing()==True or decreasing()==True):
    print("Array is monotonic")
else: print("Array is not monotonic")