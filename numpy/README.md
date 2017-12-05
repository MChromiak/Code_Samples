### [Numpy](http://www.numpy.org/) 

The folder contains code samples explaining and experimenting with Numpy particularities and applications.
NumPy is the fundamental package for scientific computing with Python. In NumPy dimensions are called **axes**. The 
number of axes is **rank**. [CheetSheet](Numpy_Python_Cheat_Sheet.pdf)

#### Run `.ipynb`
Use your local `jupyter notebook` or click the following links to view:
1. [Numpy Arrays](np-array.ipynb)
2. 

#### Numpy Array Vs Python Lists
Use numpy arrays. NumPy’s **array** class is called `ndarray`. It is also known by the alias `array`. `numpy.array` 
is not the same as the Standard Python Library class `array.array`, which only handles one-dimensional arrays  \and 
offers less functionality. [NymPy array doc](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)

The difference is mostly due to "indirectness" -- a **Python list** is an array of pointers to Python objects. This 
means it can hold completely heterogeneous, arbitrary data, at least 4 bytes per pointer plus 16 bytes for even the 
smallest Python object (4 for type pointer, 4 for reference count, 4 for value -- and the memory allocators rounds 
up to 16). 

A **NumPy array** is an array of uniform values -- single-precision numbers takes 4 bytes each, double-precision 
ones, 8 bytes. Numpy provides optimized vectorized operations. Less flexible, but you pay substantially for the 
flexibility of standard Python lists!
 
Difference between a list and an array is also the functions that you can perform to them. For example, you can 
divide an array by 3, and each number in the array will be divided by 3 and the result will be printed if you request
it. If you try to divide a list by 3, Python will tell you that it can't be done, and an error will be thrown.

### More:
* [Tutorial on Numpy Arrays](https://www.datacamp.com/community/tutorials/python-numpy-tutorial)
* [Python 3 Quckstart](https://docs.python.org/3/tutorial/)
* [Python 3 Doc](https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.ndarray.html)

---
###### LICENSING
Code: AGPL-3.0 Content:
[![CC-by-SA-4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)
