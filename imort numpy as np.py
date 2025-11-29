import numpy as np
arr=np.array([1,2,3,4])
print(arr)
matrix=np.array([[1,2,3],
                 [4,5,6],
                 [8,9,10]])
print("/n===arrayproperties===")
print("shape of the matrix",arr.shape)
print("data type of the matrix",arr.dtype)
print("size of the matrix",arr.size)
print("data type of the matrix",arr.dtype)

print("/n===mathematical properties===")
print("sum of the matrix",np.sum(arr))
print("mean of the matrix",np.mean(arr))
print("standard deviation of the matrix",np.std(arr))
print("variance of the matrix",np.var(arr))
