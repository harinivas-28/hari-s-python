print("******** WELCOME TO HARI ATM *********")
n=int(input("Enter value to Withdarw:"))
l=[2000,500,200,100,50,20,10]
for i in range(len(l)):
    if(n>=l[i]):
        print(f"{l[i]}*",n//l[i])
        n=n%l[i]
    elif(n<l[i]):
        print(f"{l[i]}*",n//l[i])
        n=n%l[i]
    elif(n<10): break
print("******* Thank you !********")
