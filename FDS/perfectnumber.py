a=int(input("Enter number:"))
i=1
sum=0
while(a>i):
    if(a%i==0):
        sum=sum+i
    i+=1
if(sum==a):
    print(f"{a} is a Perfect number")        
else:
    print(f"{a} is not a Perfect number")