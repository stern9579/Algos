# Given an array of integers, where all elements but one occur twice, find the unique element

def lonelyinteger(a):
    b = []
    
    for i in range(0, len(a)):
        if a[i] not in b:
            b.append(a[i])
        elif a[i] in b:
            b.remove(a[i])
            
    return b[0]

