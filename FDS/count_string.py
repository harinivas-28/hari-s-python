s=input("Enter String:")
c=0
d=0
for x in s:
    if(x.isalpha()):
        c+=1
for x in s:
    if(x.isdigit()):
        d+=1
print(f"No.of Characters:{c}")
print(f"No.of Digits:{d}")
print(f"No.of Symbols:{len(s)-(c+d)}")
