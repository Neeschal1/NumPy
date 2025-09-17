import numpy as np

arr_1 = np.array([1, 2, 3], dtype=np.int8)   
arr_2 = np.array([4, 5, 6], dtype=np.int8)   

sum = arr_1 + arr_2

print(sum)


'''
  NOTES:

  datatype     no. of bits      range

| np.int8     | 8-bit        | -128 to 127                                             |
| np.uint8    | 8-bit        | 0 to 255                                                |
| np.int16    | 16-bit       | -32,768 to 32,767                                       |
| np.uint16   | 16-bit       | 0 to 65,535                                             |
| np.int32    | 32-bit       | -2,147,483,648 to 2,147,483,647                         |
| np.uint32   | 32-bit       | 0 to 4,294,967,295                                      |
| np.int64    | 64-bit       | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| np.uint64   | 64-bit       | 0 to 18,446,744,073,709,551,615                         |


default value is: dtype=np.int64

'''