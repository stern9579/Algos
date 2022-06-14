"""
Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.

Example
a = 3
b = 5

The result of the integer division 3//5=0
The result of the float division is 3/5 = 0.6
"""
import random

a = random.randint(0, 100)
b = random.randint(0, 100)
c = [a//b, a/b]

for answer in c:
    print(answer)
