

from types import NoneType


def miniMaxSum(arr):
    # One Liner
    # print(sum(arr)-max(arr), sum(arr)-min(arr))

    sum = 0
    min = None
    max = None


    for _ in range(0, len(arr)):
        # print(_)
        for n in range(0, len(arr)):

            if _ != n:
                sum = arr[n] + sum 
            elif sum == None:
                sum = arr[n]

        if min is None:
            min = sum
        elif sum <= min:
            min = sum

        if max is None:
            max = sum
        elif sum >= max:
            max = sum
        
        sum = 0
    
    return(min, max)


arr = [5,5,5,5,5]
arr2 = [3, 5, 7, 8, 10]

print(miniMaxSum(arr))
print(miniMaxSum(arr2))