import numpy as np

one_matrix = np.ones((2, 5))
print(one_matrix)

zeros_matrix = np.zeros((3, 3))
print(zeros_matrix)

full_matrix = np.full((4, 2), 9)
print(full_matrix)

eye_matrix = np.eye(4, 4, dtype=np.int8)
print(eye_matrix)

identity = np.identity(3, dtype=np.int8)
print(identity)

sequence = np.arange(1, 5, 1, dtype=np.int8)
print(sequence)
