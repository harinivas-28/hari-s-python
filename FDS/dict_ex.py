july={26:112,27:113,28:78,29:170,30:189}
s=sorted(july.items(),key=lambda x:x[1])
print (s)
print(f"{s[0]} is having the lowest rainfall")
print(f"{s[-1]} is having the highest rainfall")
