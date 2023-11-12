n=int(input("Enter Range:"))#10
i=2
j=2
if n>0:#10>0
    while i<=n:#2<10
        if n%i==0:#10%2==0
            continue
        else:
            print(i)
            i+=1
else:
    print("Enter valid number")