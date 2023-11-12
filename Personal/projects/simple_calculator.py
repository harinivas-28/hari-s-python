import os
def calci():
    def add():
        return n1+n2
    def subtract():
        return n1-n2
    def multi():
        return n1*n2
    def div():
        return n1/n2
    operations={
        '+':add,
        '-':subtract,
        '*':multi,
        '/':div
    }
    n1=int(input("Enter First Number: "))
    end=True
    while end:
        op=input("Enter Operator: + - * / -->")
        n2=int(input("Enter Next Number: "))
        for i in operations:
            if i==op:
                z=operations[i]
                break
        result=z()
        print(f"{n1}{op}{n2}={result}")
        a=True
        while a:
            ask=input("Enter\n'y' to continue calculation\n'n' for new caliculation\n'x' to exit\n").lower()
            if ask=='y':
                n1=result
                a=False
            elif ask=='n':
                end=False
                a=False
                os.system('cls')
                calci()
            elif ask=='x':
                exit()
            else:
                print("InValid Operator")
calci()