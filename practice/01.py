import numpy as np

matrix_01 = np.array(
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 8, 9], [10, 11, 12], [13, 14, 15]]]
)


matrix_02 = np.array(
    [
        [
            [3, 2, 1],
            [6, 5, 4],
            [9, 8, 7],
        ],
        [
            [9, 8, 7],
            [12, 11, 10],
            [15, 14, 13],
        ],
    ]
)

dot_product = np.dot(matrix_01, matrix_02)
cross_product = np.cross(matrix_01, matrix_02)

print(f"Dot Product: {dot_product}")
print(f"Cross Product: {cross_product}")
