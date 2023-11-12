x=int(input("Enter a number:"))
y=int(input("Enter another number:"))
gcd = 1   
if x % y == 0:
      print(y)  
for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           gcd = k
           break
print(f"GCD of {x} and {y} is {gcd}")