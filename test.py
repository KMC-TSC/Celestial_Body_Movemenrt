import numpy as np
import math
print("-----------")
x = 4.0
y = 3.0
a = 90.0*(math.pi/180)

for i in range(5):
    array = np.array([x*math.cos(a)-y*math.sin(a), x*math.sin(a)+y*math.cos(a)])
    x=array[0]
    y=array[1]
    print(np.round(array,10))
print("-----------")
array1 = np.array([[2,3,5],
                  [7,9,12]])
array2 = np.array([[5,1,6],
                   [2,3,4]])
print(array1[1]*array2)
print("-----------")
