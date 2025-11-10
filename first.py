import numpy as np

print("Hello, World!")

data = [1, 2, 3, 4, 5]
array = np.array(data)
print("Numpy array:", array)
print("Array mean:", np.mean(array))

multiplied_array = array * 10
print("Multiplied array:", multiplied_array)

add_array = array + 100
print("Array after addition:", add_array)