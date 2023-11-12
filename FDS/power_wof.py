n=int(input("Enter Number:"))
p=int(input("Enter Power:"))
def power(p):
    while p>0:
        if p==0:
            return 1
        else:
            return n*power(p-1)
print(f"{n} raised to the power of {p} is {power(p)}")