from ImageProcessor import ImageProcessor
imp = ImageProcessor()

print("******** TEST 1 ***********")
arr = imp.load("non_existing_file.png")

print("******** TEST 2 ***********")
print(arr) 

print("******** TEST 3 ***********")
arr = imp.load("empty_file.png")

print("******** TEST 4 ***********")
print(arr) 

print("******** TEST 5 ***********")
arr = imp.load("./42AI.png") 

print("******** TEST 6 ***********")
print(arr)

print("******** TEST 7 ***********")
imp.display(arr)