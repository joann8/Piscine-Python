import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()
print("******** TEST 1 ***********")
arr1 = np.arange(0,25).reshape(5,5) 
to_print = spb.crop(arr1, (3,1) , (1,0) )
print(to_print)

print("******** TEST 2 ***********")
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)

print("--> Inital array")
print(arr2)

print("--> remove columms with n=3 et axis =0")
to_print = spb.thin(arr2,3,0)
print(to_print)

print("--> remove columms with n=2 et axis =1")
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
to_print = spb.thin(arr2,2,1)
print(to_print)

print("******** TEST 4 ***********")
arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print("--> Inital array")
print(arr3)

print("--> Juxtapose n = 3 on axis 1")
to_print = spb.juxtapose(arr3, 3, 1)
print(to_print)

print("--> Juxtapose n = 3 on axis 0")
arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
to_print = spb.juxtapose(arr3, 3, 0)
print(to_print)

print("******** TEST 5 ***********")
arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(arr3)
print("--> Mosaic dim 2, 4")
to_print = spb.mosaic(arr3, (2,4))
print(to_print)