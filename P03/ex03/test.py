from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter

print("******** BASE IMAGE ***********")

imp = ImageProcessor()
arr = imp.load("./elon_canaGAN.png")
imp.display(arr)

from ColorFilter import ColorFilter
cf = ColorFilter()

print("******** TEST 0 - CELLULOID ***********")
cel = cf.to_celluloid(arr)
imp.display(cel)

print("******** TEST 1 - INVERT ***********")
invert_arr = cf.invert(arr)
imp.display(invert_arr)

print("******** TEST 2 - GREEN ***********")
green = cf.to_green(arr)
imp.display(green)

print("******** TEST 3 - RED ***********")
red = cf.to_red(arr)
imp.display(red)

print("******** TEST 4 - BLUE ***********")
blue = cf.to_blue(arr)
imp.display(blue)


print("******** TEST 5 - GRAYSCALE ***********")
print("----> Test 1 with m")
gray1 = cf.to_grayscale(arr, 'm')
imp.display(gray1)
print("----> Test 2 with weighted list")
gray2 = cf.to_grayscale(arr, 'weight', [0.2, 0.3, 0.5])
imp.display(gray2)
