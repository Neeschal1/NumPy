import numpy as np

matrix = np.array([1, 2, 3, np.nan, 5, 6, np.nan, 8, 9], dtype=np.float32)

print(np.isnan(matrix)) # prints True where the elements are NaN

