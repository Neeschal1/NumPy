import numpy as np

arr_one = np.array([1, 2, 3], dtype=np.int8)
arr_two = np.array([4, 5, 6], dtype=np.int8)

cross_product = np.cross(arr_one, arr_two)
dot_product = np.dot(arr_one, arr_two)
sum = arr_one + arr_two
difference = arr_one - arr_two
multiplication = arr_one * arr_two
division = arr_one / arr_two

print(f'''
      Cross Product: {cross_product} \n
      Dot Product: {dot_product}, \n
      Sum: {sum}, \n
      Difference: {difference}, \n
      Multiplication: {multiplication}, \n
      Division: {division}
''')