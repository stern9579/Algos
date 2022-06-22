import numpy

my_1D_array = numpy.array([1, 2, 3, 4, 5])
print(my_1D_array.shape)     #(5,) -> 1 row and 5 columns

my_2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print(my_2D_array.shape)     #(3, 2) -> 3 rows and 2 columns

change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print (change_array)      

#Output = [[1 2][3 4][5 6]]

#You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.

def shape(var):
    new_arr = []
    for v in range(len(var)):
        new_arr.append(int(var[v]))
        
    return (numpy.reshape(new_arr, (3,3)))
_newInput = input().strip().split(" ") 

reshaped_array = shape(_newInput)
print (reshaped_array)