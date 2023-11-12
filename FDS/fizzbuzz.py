a=int(input("Enter lower limit:"))
b=int(input("Enter upper limit:"))
for i in range(a,b+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)