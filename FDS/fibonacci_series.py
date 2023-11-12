'''
# USING FOR LOOP
n=int(input("Enter number:"))
a=0
b=1
num=0
print(a,b,end=" ")
for i in range(0,n-2):
    num=a+b
    (a,b)=(b,num)
    print(num,end=" ")
'''
# USING WHILE LOOP
n=int(input("Enter number"))
a=0
b=1
i=0
while(i<n):
    print(a,end=" ")
    c=a+b
    (a,b)=(b,c)
    i+=1
