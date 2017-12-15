import tensorflow as tf

# Enable TF Eager execution to get the tensor results
from tensorflow.contrib.eager.python import tfe

tfe.enable_eager_execution()

# Slice
t = [[[1, 1, 1], [2, 2, 2]],
     [[3, 3, 3], [4, 4, 4]],
     [[5, 5, 5], [6, 6, 6]]]

# To see results use the good old python print() when using tf.Eager
print(t)
# or tf.Print, otherwise.

tf.Print(t, [t])

# slice(input, start, size):
#   start - offest index where to start slicing
#   size[i] - nr of elements of the i'th dimension of `input`,
#             starting form 1! not zero;  select individual columns in the rows

tf.slice(t, [1, 0, 0], [1, 1, 3])  # [[[3, 3, 3]]]
tf.slice(t, [1, 0, 0], [1, 2, 3])  # [[[3, 3, 3],
#   [4, 4, 4]]]
tf.slice(t, [1, 0, 0], [2, 1, 3])  # [[[3, 3, 3]],
#  [[5, 5, 5]]]
tf.slice(t, [1, 0, 0], [2, 1, 2])  # [[[3, 3]],
#  [[5, 5]]]


input = [
    [[11, 12, 13], [14, 15, 16]],
    [[21, 22, 23], [24, 25, 26]],
    [[31, 32, 33], [34, 35, 36]],
    [[41, 42, 43], [44, 45, 46]],
    [[51, 52, 53], [54, 55, 56]],
]
s1 = tf.slice(input, [1, 0, 0], [1, 1, 3])  # [[[21 22 23]]]

s2 = tf.slice(input, [2, 0, 0], [3, 1, 2])  # [[[31 32]]
                                            #  [[41 42]]
                                            #  [[51 52]]]

s3 = tf.slice(input, [0, 0, 1], [4, 1, 1])  # [[[12]]
                                            #  [[22]]
                                            #  [[32]]
                                            #  [[42]]]

# Any zero in 'size' parameter always gives empty result tensor:
tf.slice(input, [0, 0, 1], [1, 0, 1])  # []
tf.slice(input, [0, 0, 1], [1, 1, 0])  # []
tf.slice(input, [0, 0, 1], [0, 1, 1])  # []
tf.slice(input, [0, 0, 1], [1, 1, 1])  # [[[12]]]

# negative value means the function cutting tensors automatically
# '-1' here is equivalent to "*" or "take all in that dimension"
tf.slice(input, [2, 0, 2], [-1, -1, -1])    # [[[33]
                                            #   [36]]
                                            #  [[43]
                                            #   [46]]
                                            #  [[53]
                                            #   [56]]]

#   argmax
# -----------------
# Since x[3] is the largest number(4), argmax(x) is 3
x = [1, 2, 3, 4, 3, 2, 1]
tf.argmax(x, axis=0)  # 3

# Axis 1 will apply argmax to the rows
# Axis 0 will apply argmax to the columns
x = [[1, 2, 3, 4, 3, 2, 1],
     [2, 3, 4, 3, 2, 1, 0]]

tf.argmax(x, axis=0)  # [3,2]
tf.argmax(x, axis=1)  # [1,1,1,0,0,0,0]

# Gather:
# -----------------
# A scalar index of a vector is a scalar.
# 3 is the index of 4, so gathering 3 is 4.
x = [1, 2, 3, 4, 3, 2, 1]
tf.gather(x, 3)  # 4

# A scalar index of a matrix x is a vector.
# Row 0 of x is [1,2,3,4,3,2,1], so gathering 0 returns it.
x = [[1, 2, 3, 4, 3, 2, 1],
     [2, 3, 4, 3, 2, 1, 0]]
tf.gather(x, 0)  # [1, 2, 3, 4, 3, 2, 1]

# Gathering a vector index produces a scalar index for each element of the
# vector, and then concatenates them.
# Gathering [1,0] produces row 1 and row 0. Concatenating them flips the rows
# in the original matrix.
tf.gather(x, [1, 0])    # [[2,3,4,3,2,1,0],
                        #  [1,2,3,4,3,2,1]]

# In general, each scalar index within the index tensor will produce an
# entire row in x.
tf.gather(x, [[[1]], [[0]]])    # [ [[2,3,4,3,2,1,0]],
                                #   [[1,2,3,4,3,2,1]] ]

# `indices` defines slices into the first dimension of `params`
# index describe which slice gather from input array, not which element
params_g = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

idx = [[1, 0], [2, 0]]

tf.gather(params_g, idx)    # [ [[4 5 6],
                            #   [1 2 3]],
                            # [ [7 8 9],
                            #   [1 2 3]] ], shape=(2, 2, 3), dtype=int32

# Gather_nd (n-dimentional; multidimention)
# -----------------
# Gather assumes that each scalar is an index along the first dimension.
# gather_nd target other values

x = [[1, 2, 3, 4, 3, 2, 1],
     [2, 3, 4, 3, 2, 1, 0]]

# An empty index returns the entire tensor.
i = tf.cast([], tf.int32)
tf.gather_nd(x, i)  # [[ 1,2,3,4,3,2,1],
                    #  [ 2,3,4,3,2,1,0]]

# The row 0 of x is [1,2,3,4,3,2,1], so gathering [0] returns it.
tf.gather_nd(x, [0])  # [1,2,3,4,3,2,1]

# Row 0, column 0 of x is 1, so gathering [0,0] returns 1.
tf.gather_nd(x, [0, 0])  # 1

# The last dimension(or the most deeply-nested list) of the index tensor is
# an  index vector using the previous rules.  So if we stack two copies of
# the previous index tensors, we'll get two copies of the result:
# Two empty indices return two copies of the entire tensor
i = tf.cast([[], []], tf.int32)
tf.gather_nd(x, i)  # [[[ 1,2,3,4,3,2,1],
                    #   [ 2,3,4,3,2,1,0]],
                    #  [[ 1,2,3,4,3,2,1],
                    #   [ 2,3,4,3,2,1,0]]]

# Gathering [0] twice returns the first row twice.
tf.gather_nd(x, [[0], [0]])     # [ [1,2,3,4,3,2,1],
                                #   [1,2,3,4,3,2,1] ]

# Gathering [0,0] twice returns row 0, col 0 twice:
tf.gather_nd(x, [[0, 0], [0, 0]])  # [1,1]

# `indices` defines slices into the first `N` dimensions of `params`, where `N =
# indices.shape[-1]`

params_nd = [[1, 2, 3],
             [4, 5, 6]]
index = [[[0, 1], [0, 0]],
         [[1, 2], [1, 0]]]

tf.gather_nd(params_nd, index)  # [[2 1]
                                #    [6 4]], shape=(2, 2), dtype=int32
