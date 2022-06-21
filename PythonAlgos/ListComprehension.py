fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in fruits]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# 2 Dimensional
a = [[x for x in range(5)] for y in range(5)]
print(a)

a = [list(x for x in range(10)) for y in range(10)]
print(a)

# MULTI-DIMENSIONAL
x, y, z, n = [1, 1, 2, 2]
output = [[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i+j+k != n]
print(output)