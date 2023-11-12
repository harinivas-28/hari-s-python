csmB={"Hari":[99,98,99,98],"lalit":[70,82,65,74],"Bhargav":[64,86,92,67],"Chandu":[92,94,93,95]}
k=list(csmB)
l=[]
for i in k:
    sum=0
    for j in csmB[i]:
        sum+=j
    avg=sum/4
    l.append(avg)
new=dict(zip(k,l))
print(new)
