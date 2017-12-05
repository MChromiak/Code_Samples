import numpy as np

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
t = np.vstack([a, b, c])
print(t.shape)  # (3, 3)
print(t)  # 2D array of 3 elements each of size 3
#       [[1 2 3]
#        [4 5 6]
#        [7 8 9]]
print(t[0])  # index on 1D array; take first element
#       [1 2 3]
print(t[0:])  # index on 1D array; form elem 0 to the end are three elements:
#       [[1 2 3]
#        [4 5 6]
#        [7 8 9]]
print(t[0, :])  # index on 2D array; take first row
#       [1 2 3]

print(t[1])  # index on 1D array; take second element
#       [4 5 6]
print(t[1:])  # index on 1D array; form elem 1 to the end are two elements:
#       [[4 5 6]
#        [7 8 9]]
print(t[1, :])  # index on 2D array; take second row
#       [4 5 6]
print(t[2])  # index on 1D array; take third element
#       [7 8 9]
print(t[2:])  # index on 1D array; form elem 2 to the end is 1 element:
#       [[7 8 9]]
print(t[2, :])  # index on 2D array; take third row
#       [7 8 9]
# Columns
print(t[:0])  # index on 1D array; take elements before element 0 (0 is first)
#       [] - so no elements before 0 element
print(t[:, 0])  # index on 2D array; take first column
#       [1 4 7]
print(t[:1])  # index on 1D array; take elements before element 1 (0 is first)
#       [[1 2 3]]   - first (zero) element
print(t[:, 1])  # index on 2D array; take second column
#       [2 5 8]
print(t[:2])  # index on 1D array; take elements before element 2 (0 is first)
#       [[1 2 3]    - zero elem.
#        [4 5 6]]   - one elem
print(t[:, 2])  # index on 2D array; take third column
#       [3 6 9]
print(t[:3])  # index on 1D array; take elements before element 3 (0 is first)
#       [[1 2 3]
#        [4 5 6]
#        [7 8 9]]

print(t[:, 3])  # index on 2D array; take fourth column; only 3 columns so:
# IndexError: index 3 is out of bounds for axis 1 with size 3
print(t[:4])  # index on 1D array; take elements before element 4 (0 is first)
#       [[1 2 3]    - every elem in 1D array is before 4
#        [4 5 6]
#        [7 8 9]]

u = np.array([[6, 7, 8], [9, 10, 11]])
print(u)  # 2D array of 2 elements each of size 3
u.shape == t.shape

z = np.array(1)
print('z=', z.shape, z, z.dtype, z.strides)  # z= () 1 int64 ()

z1 = np.array([1])
print('z1=', z1.shape, z1, z1.dtype, z1.strides)  # z1= (1,) [1] int64 (8,)

x = np.array([1, 2, 3])
print('x=', x.shape, x, x.dtype, x.strides)  # x= (3,) [1 2 3] int64 (8,)

x1 = np.array([1, 2, 3], ndmin=2)  # array([[1, 2, 3]])
print('x1=', x1.shape, x1)  # x1= (1, 3) [[1 2 3]]

x2 = np.array(
    [[1, 2, 3], 7, 8, 9])  # array([list([1, 2, 3]), 7, 8, 9], dtype=object)
print('x2=', x2.shape, x2)  # x2= (4,) [list([1, 2, 3]) 7 8 9]

x21 = np.array([[1, 2, 3], [7, 8, 9]])  # array([[1, 2, 3],
#        [7, 8, 9]])
print('x21=', x21.shape, x21)  # x21= (2, 3) [ [1 2 3]
#               [7 8 9] ]

x22 = np.array([[1, 2, 3], [
    [7, 8, 9]]])  # array([list([1, 2, 3]), list([[7, 8, 9]])], dtype=object)
print('x22=', x22.shape, x22)  # x22= (2,) [list([1, 2, 3]) list([[7, 8, 9]])]

x23 = np.array([[1, 2, 3], [[4, 5, 6]], [7, 8, 9]])
print('x23=', x23.shape,
      x23)  # x23= (3,) [list([1, 2, 3]) list([[4, 5, 6]]) list([7, 8, 9])]

x3 = np.array([[[1, 2, 3]], [[7, 8, 9]]])
print('x3=', x3.shape, x3)  # x3= (2, 1, 3) [ [[1 2 3]]
#                 [[7 8 9]] ]

x4 = np.array([[[[1, 2, 3]]], [[[4, 5, 6]]], [[[7, 8, 9]]]])
print('x4=', x4.shape, x4)  # x4= (3, 1, 1, 3) [ [[[1 2 3]]]
#                    [[[4 5 6]]]
#                    [[[7 8 9]]] ]
# See http://cs231n.github.io/python-numpy-tutorial/#python-containers
# Slicing
# Indexing

a = np.array([[1, 2], [3, 4], [5, 6]])
# An example of integer array indexing.
# The returned array will have shape (3,) and
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"
# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"
# When using integer array indexing, you can reuse the same
# element from the source array:
print(a[[0, 0], [1, 1]])  # Prints "[2 2]"
# Equivalent to the previous integer array indexing example
print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"
