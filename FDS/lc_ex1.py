nums=[]
n=int(input("Enter Length of the array: "))
for i in range(n):
    k=int(input())
    nums.append(k)
target=int(input("Input Target: "))
ind=[]
for i in range(1,len(nums)):
    if nums[i-1]+nums[i]==target:
        ind.append(i-1)
        ind.append(i)
        break
print(ind)