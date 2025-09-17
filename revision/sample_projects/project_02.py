import numpy as np

user_input_for_first_matrix = []
user_input_for_second_matrix = []

for i in range(1, 5):
    user_data = int(input(f"Enter elements {i} to be stored inside the first array: "))
    user_input_for_first_matrix.append(user_data)

for i in range(1, 5):
    user_data = int(input(f"Enter elements {i} to be stored inside the second array: "))
    user_input_for_second_matrix.append(user_data)

arr = np.array([user_input_for_first_matrix, user_input_for_second_matrix])

print(arr)
print(f"Total elements inside the matrix: {arr.size}")
print(f"Shape of the matrix: {arr.shape}")