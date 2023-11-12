'''
    *
   * *
  * * *
'''
n=int(input("Enter range: "))
for i in range(n):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i+1):
        print("* ",end="")
    print()
