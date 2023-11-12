"""
3.Take two functions code and decode and change the input by
using particular way below.
"""
#a position 1 then sq 1 returns a
#b position 2 then sq 4 returns d
#if square is more than 26 then modulo by 26 like x%26
"""
ex:abc
output:adi
ex:aabbff
output:aaddjj
"""
a=input()
r=[]
def code():
    for x in a:
        r.append((ord(x)-96)**2)
    for x in r:
        if(x>26):
            x=x%26
            print(chr(x+96),end="")
        else:
            print(chr(x+96),end="")
code()