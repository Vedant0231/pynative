import numpy as np

arr = np.array([1,2,3,4,5])

print(arr)
print(np.__version__)
print(type(arr))

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

b = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
print(b[1,0,0])

c = np.array([1, 2, 3, 4, 5, 6, 7])

print(c[1:6:2])

#from the second element, slice elements from index 1 to index 4
d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(d[1, 1:4])

e = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(e.shape)

f = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in f:
    for y in x:
        for z in y:
            print(z)


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

g = np.concatenate((arr1,arr2), axis=1 )

print(g)            

arr = np.array([1, 2, 3, 4, 5, 6])

new = np.array_split(arr,3)

print(new)