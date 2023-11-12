july={24:115,25:114,26:423,27:234}
print(july)
csm_b={"Hari":[95,95,83,23],
       "hari":[34,54,33,53]
}
print(csm_b)
f=csm_b.keys()
print(type(f))
print(f)
#About Keys
"""
are unique
are not having index
are case sensitive
unordered
can only be single
"""
#sec way
"""
use a dictionary constructor dict(zip(ds1,ds2)).
the ds1 should be a single valued data function.
ds2 can be anything.
the size of ds2 should match with the sixe of ds1.
"""
likes_icecream=dict(zip(csm_b.keys(),[True,False]))
m=likes_icecream.keys()
print(type(m))
print(m)
print(likes_icecream)
print(likes_icecream['hari'])
print(likes_icecream['Hari'])
for i in likes_icecream:
    if likes_icecream[i]==True:
        print(i)
l=likes_icecream.items()
print(type(l))
print(l)#List of Tuples
n=sorted(july)
print(n)