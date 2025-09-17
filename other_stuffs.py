import numpy as np

e = np.e
exponential = np.exp

# For finding square root
array_one = np.array([4, 9, 16, 25, 36], dtype=np.int8)
square_root = np.sqrt(array_one).astype(int)
print(square_root)

# For finding power of a single integer
power = np.array([2**2])
print(power)

# For finding logarithmic values
logarithm = np.array([1, e, e**2])
log = np.log(logarithm)
print(log)

# For finding exponential values
exp = np.array([1, 2, 3, 4])
exponential_result = exponential(exp)
print(exponential_result)
