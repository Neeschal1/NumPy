import numpy as np

mat_one = np.array([1, 2, 3])
mat_two = np.array([[1, 2, 3], [4, 5, 6]])
mat_three = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
mat_four = np.array(
    [
        [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]],
        [[[13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24]]],
    ]
)

print(f"{mat_one.ndim}D ARRAY")
print(f"{mat_two.ndim}D ARRAY")
print(f"{mat_three.ndim}D ARRAY")
print(f"{mat_four.ndim}D ARRAY")

print(mat_four[1, 1, 0, 2])
