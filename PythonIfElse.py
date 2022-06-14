import random

'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.
'''

x = random.randint(1, 100)
print(x)
if x % 2 > 0:
    print("Weird")
elif x % 2 == 0 and x in range(2,6):
    print("Not Weird")
elif x % 2 == 0 and x in range(6, 21):
    print("Weird")
elif x % 2 == 0 and x > 20:
    print("Not Weird")
else: 
    print("Not Weird")