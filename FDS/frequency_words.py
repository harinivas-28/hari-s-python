n=input("")
k=n.split(" ")
l=list(set(k))
l.sort()
for x in l:
    print(f"{x}:{k.count(x)}")