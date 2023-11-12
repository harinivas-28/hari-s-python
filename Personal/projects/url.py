import random 
u="http://"
title=input("Enter Title:")
t=['.com','.in','.org','.ac.in','.in','.edu','.co.in']
def url_generator(title):
    for i in title:
        if i==" ":
            title=title.replace(" ","-")
        else: pass
    return (f"{u}{title}{random.choice(t)}")
k=url_generator(title)
print(k)
"""
k=i.split(" ")
for i in k:
    if i==" ":
        k.remove(i)
    
"""

