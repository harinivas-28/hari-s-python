l1=[]
l2=[]
n1=int(input("Enter no.of lists: "))
n2=int(input("Enter no.of elements in a list: "))
for i in range(n1):
    l2.clear()
    for i in range(n2):
        r2=int(input("Enter element: "))
        l2.append(r2)
    l1.append(l2)
print(l1)
