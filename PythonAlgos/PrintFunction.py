
def PrintFunction(n):
    output = ""
    for num in range(1,n+1):
        output += str(num)
    return output

print(PrintFunction(4))
print(PrintFunction(10))
print(PrintFunction(0))