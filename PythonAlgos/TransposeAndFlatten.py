import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print(numpy.transpose(my_array))

#Output = [[1 4] [2 5] [3 6]]

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print(my_array.flatten())

#Output = [1 2 3 4 5 6]


# Task

# You are given a NxM integer array matrix with space separated elements (N = rows and M = columns).
# Your task is to print the transpose and flatten results.

# Input Format

# The first line contains the space separated values of N and M.
# The next N lines contains the space separated elements ofM  columns.

# Output Format

# First, print the transpose array and then print the flatten.

n, m = map(int, input().split())        # Remember that input() takes the first input, then when called again, takes the next.
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())