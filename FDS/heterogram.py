""" Write a progam to check whether the given string is heterogram or not

Explanation:

we use a set char_set to keep track of the characters encountered in the input string. 
We iterate through each character of the input string and check if it is an alphabet letter. 
If it is, we convert it to lowercase and check if it already exists in the char_set. If it does, 
it means the letter is repeated, and the string is not a heterogram. Otherwise, we add the lowercase letter to the set. 
If we go through the entire string without finding any repeated letters, the string is a heterogram.


Sample input:
abCdeFg                                                                                                 

Sample output:
The given string is a heterogram.

Sample input:
abBcCdeDfE                                                                                                              

Sample output:
The given string is not a heterogram.  """

# Write your code here
a=list(input())
for i in range(len(a)):
    a[i]=a[i].lower()
b=set(a)
if len(a)==len(b):
    print("The given string is a heterogram.")
else:
    print("The given string is not a heterogram.")