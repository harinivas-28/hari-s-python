import random
name=input("Enter name:")
age=int(input("Enter age:"))
if age>=18:
    aadhar_no=int(input("Enter Aadhar number:"))
    add=input("Enter address:")
    acc_no=random.randint(1000000000,9999999999)
    print(f"Your Account Number is :{acc_no}")
else:
    print("YOU ARE BELOW AGE")