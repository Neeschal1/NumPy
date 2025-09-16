import numpy as np

mat_one = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
mat_two = np.array([[[13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24]]])

user_decision = None
while True:
    decide = int(input(
        """
          Choose among following operations:
          1. Matrix Addition
          2. Matrix Subtraction
          3. Matrix Multiplication
          4. Matrix Division
          5. Finish 
          
          Enter your Choice: 
        """
    ))
    match (decide):
        case 1:
            mat_add = np.add(mat_one, mat_two)
            print(mat_add)
        case 2:
            mat_diff = np.subtract(mat_one, mat_two)
            print(mat_diff)
        case 3:
            mat_mul = np.multiply(mat_one, mat_two)
            print(mat_mul)
        case 4:
            mat_div = np.divide(mat_one, mat_two)
            print(mat_div)
        case 5:
            print("Exitting program...!")
            break
        case _:
            print("Invalid Choice!")