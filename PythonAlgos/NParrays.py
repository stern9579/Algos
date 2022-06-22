import numpy
# needed to pip install numpy
#A NumPy array is a grid of values. They are similar to lists, except that every element of an array must be the same type.


a = numpy.array([1,2,3,4,5])
print(a[1])          #2

b = numpy.array([1,2,3,4,5],float)
print(b[1])          #2.0

def arrays(arr):
    # complete this function
    # use numpy.array
    a = numpy.array(arr, float)
    return numpy.flipud(a)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)