import numpy as np

matrix = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900])

"""
    Slicing begins by using : symbol.
    
    Suppose, I need to access elements from 0th index to 4th index of matrix array.
    Then, I can do it by using:
        matrix[0:5]
        
    I can make a step using second : symbol. For eg:
    matrix[0:-1:2]
    this makes my element appear skipping 1 symbols.
"""

print(matrix[0:-1:2])
print(matrix[::4])
print(matrix[2::3])