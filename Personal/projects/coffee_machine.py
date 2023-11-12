#This Machine is incomplete because machine data like milk,water,powder should update when used
import coffee_machine_database
from coffee_machine_database import total_balance
from coffee_machine_database import Rupees
from coffee_machine_database import data

profit=0
print("--- COFFEE MACHINE ---")
cof=input("Select which coffee do you want Latte/Expresso/Cappucino: ")
if cof=='Latte' or cof=='Expresso' or cof=='Cappucino':
    five=int(input("Enter Number of 5 Rupees: "))
    ten=int(input("Enter Number of 10 Rupees: "))
    twenty=int(input("Enter Number of 20 Rupees: "))
    for i in Rupees:
        if i=='5 Rs':
            Rupees[i]=five
        elif i=='10 Rs':
            Rupees[i]=ten
        elif i=='20 Rs':
            Rupees[i]=twenty
    balance=total_balance()
    for i in data:
        if cof=='Latte'and i=='Latte':
            for j in data[i]:
                if j=='Cost':
                    balance-=data[i][j]
                    if balance<0:
                        print(f"Money was not enough ! You need {-balance}, Your money is refunded")
                    elif balance<data[i][j]:
                        if data[i][j]==270:
                            print("Here's Your Latte ! Enjoy")
                            profit+=270
                        else:
                            print(f"Enjoy Your Latte! Here's Your Change {balance}.")
                            profit+=270
            break
        elif cof=='Expresso' and i=='Expresso':
            for j in data[i]:
                if j=='Cost':
                    balance-=data[i][j]
                    if balance<0:
                        print(f"Money was not enough ! You need {-balance} more, Your money is refunded")
                    elif balance<data[i][j]:
                        if data[i][j]==220:
                            print("Here's Your Expresso ! Enjoy")
                            profit+=220
                        else:
                            print(f"Enjoy Your Expresso! Here's Your Change {balance}.")
                            profit+=220
            break
        elif cof=='Cappucino' and i=='Cappucino':
            for j in data[i]:
                if j=='Cost':
                    balance-=data[i][j]
                    if balance<0:
                        print(f"Money was not enough ! You need {-balance}, Your money is refunded")
                    elif data[i][j]>balance:
                        if data[i][j]==190:
                            print("Here's Your Cappucino ! Enjoy")
                            profit+=190
                        else:
                            print(f"Enjoy Your Cappucino! Here's Your Change {balance}.")
                            profit+=190
            break 
elif cof=='Report':
    print(coffee_machine_database.machine_data) 
print(f"Profit={profit}")      
   