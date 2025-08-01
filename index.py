def operation(x, y):
    for i in range(x[0], x[2]):
       for j in range(y[0], y[2]):
           return i+j
    return i

array_one = [1, 3, 5]
array_two = [2, 4, 7]

result = operation(array_one, array_two)

print(result)