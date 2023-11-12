s=input("Enter String:")
k=s[0]
print(k,end="")
for x in s[1:]:
    if x==k:
        print('$',end="") 
    else:
        print(x,end="")       