print("Choose from the menu below")
print("1. Convert Dollar to Rupee")
print("2. Convert Rupee to Dollar")
print("Please enter your choice.")
choice=int(input())
if choice==1:
    print("Enter Dollars:")
    Dollar=float(input())
    Rupee=82.45*Dollar
    print("Rupees=",Rupee)
else:
    print("Enter Rupees:")
    Rupee=float(input())
    Dollar=Rupee/82.45
    print("Dollars=",Dollar)