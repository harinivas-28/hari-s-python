l=[]
n=int(input("Enter length:"))
for i in range(n):
        r=int(input())
        l.append(i)
k=int(input("Enter number you want:"))
for i in range(n):
        if(k==l[i]): print(f"{k} found at index {i}")
        else: print("Element not found.")