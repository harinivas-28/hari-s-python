import string
a=list(string.ascii_letters)
j = False
n=input("Enter String: ")
for i in n:
    if n.count(i)<1:
        j = True
        break
if j == True:
    print("String is Panagram.")
else:
    print("String is not Panagram.")

    