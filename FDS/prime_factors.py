n=int(input())
def factors(n):
    f=[]
    for x in range(1,n+1): 
        if(n%x==0):
            f.append(x)
    return f
def prime_factors():
    l=[]
    k=factors(n)
    for x in k:
        t=factors(x)
        if(len(t)==2):
            l.append(x)
        else: pass
    print(l)
prime_factors()
    

