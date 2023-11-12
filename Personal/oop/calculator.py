class Calculator:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b
    def multi(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sqr(self):
        return f"Square of A = {self.a**2}\nSquare of B = {self.b**2}"
x=int(input("Enter 1st number: "))
y=int(input("enter 2nd number: "))
work=Calculator(x,y)
op=input("Enter Operation: ")
if op=='add' or op=='+':
    print(f"Addition={work.add()}")
elif op=='subtract' or op=='-':
    print(f"Subtraction={work.subtract()}")
elif op=='multi' or op=='*':
    print(f"Multiplication={work.multi()}")
elif op=='div' or op=='/':
    print(f"Division={work.div()}")
elif op=='sqr' or op=='2':
    print(work.sqr())