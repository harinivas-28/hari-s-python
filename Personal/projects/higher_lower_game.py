#This game is incomplete because using random for 2 options, sometimes its taking both the same options
import hl_game_database
import random
import os
print("-- Let's Start the Game --")
print("** Option 1 **")
op1=random.choice(hl_game_database.data)
check=True
same=True
while check:
    while same:
        op2=random.choice(hl_game_database.data)
        if op1!=op2:
            same=False
    for i in op1:
        if i=='followers':
            pass
        else:
            print(f"{i} - {op1[i]}")
    print("** Option 2 **")
    for i in op2:
        if i=='followers':
            pass
        else:
            print(f"{i} - {op2[i]}")
    ip=input("\nGuess Which one has Higher number of followers option 1/option 2 ").lower()
    if ip=='option 1' or ip=='1':
        for i in op1 and op2:
            if i=='followers':
                if op1[i]>op2[i]:
                    print("You are Correct")
                    op3=random.choice(hl_game_database.data)
                    op2=op3
                    os.system('cls')
                elif op1[i]<op2[i]:
                    print("You Lose")
                    check=False
            else:
                pass
    elif ip=='option 2' or ip=='2':
        for i in op1 and op2:
            if i=='followers':
                if op1[i]<op2[i]:
                    print("You Won")
                    op3=random.choice(hl_game_database.data)
                    op1=op2
                    op2=op3
                    os.system('cls')
                elif op1[i]>op2[i]:
                    print("You Lose")
                    check=False
                elif op1[i]==op2[i]:
                    pass
            else:
                pass