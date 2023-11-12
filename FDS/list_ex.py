#1 Create a list from 1 to 10 print only odd index
#2 Add all the elements of even index
#3 Create a list with 5,10,15 elements and merge then print
#1A
a=[1,2,3,4,5,6,7,8,9,10]
print(a[1::2])
#2A
b=[1,2,3,4,5,6,7,8,9,10]

sum=0
x=0
for x in range(0,len(b),2):
    sum+=b[x]
print(f"Sum of all even indexes={sum}")

#3A
l1=[5,10,15]
print(a+l1)


