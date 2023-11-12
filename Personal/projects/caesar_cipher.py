import string
l=list(string.ascii_letters)
for i in range(50):
    case=input("\nDo you want to Encrypt or Decrypt or exit:\n")
    if(case=="encrypt"):
        msg=input("Enter message to encrypt: ")
        level=int(input("Enter level: "))
        for i in msg:
            for j in range(len(l)):
                if(l[j]==i):
                    pos=j
            if i==" ":
                print("$",end="")
            else:
                encryption=(pos+level)%26
                print(f"{l[encryption]}",end="")
    elif(case=="decrypt"):
        msg=input("Enter message to decrypt: ")
        level=int(input("Enter level: "))
        for i in msg:
            for j in range(len(l)):
                if(l[j]==i):
                    pos=j
            if i=="$":
                print(" ",end="")
            else:
                decryption=(pos-level)%26
                print(f"{l[decryption]}",end="")
    elif(case=="exit"):exit()
    else:print("Enter valid input i.e encrypt/decrypt")




