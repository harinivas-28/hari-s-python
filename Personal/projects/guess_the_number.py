import random
comp=random.randint(1,100)
level=input("Select Level easy/hard: ").lower()
print("-- Computer: Let Me Guess --")
number=0
if level=='easy':number=10
else:number=5
for i in range(number):
    print(f"You have {number-i} attempts left")
    guess=int(input("Guess the Number: "))
    if comp>guess:
        print("Too Low !")
    elif comp<guess:
        print("Too High !")
    else:
        print(f"Yes the number is {comp}")
        break
    if i==number-1:
        print("You have out of Guesses !!!")
