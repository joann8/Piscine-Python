from ImageProcessor import ImageProcessor
imp = ImageProcessor()
arr = imp.load("assets/42AI.png")

from ColorFilter import ColorFilter

cf = ColorFilter()
cf.invert(arr)
cf.to_green(arr)
cf.to_red(arr)
cf.to_blue(arr)
cf.to_celluloid(arr)
cf.to_grayscale(arr, 'm')
cf.to_grayscale(arr, 'weighted', [0.2, 0.3, 0.5])