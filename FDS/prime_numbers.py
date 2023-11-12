n=int(input("Enter range:"))
i=2
if n>0:
    while(i<=n):
        j=2
        while(j<=i):
            if(i%j==0):
                if(i==j):
                    print(i,end=" ")
                    j+=1
                else:
                    break
            else:
                j+=1
        i+=1
else:
    print("Enter Valid Number")