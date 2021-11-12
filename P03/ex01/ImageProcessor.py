from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np

class ImageProcessor:
    
    @staticmethod
    def load(path):
        '''opens the .png file specified by the path argument
        Returns an array with the RGB values of the image pixels 
        It must display a message specifying the dimensions of the image (e.g. 340 x 500),'''
        try:
            img = mpimg.imread(path)
            print("Loading image of dimensions {0} x {1}".format(*img.shape))
            return img
        except FileNotFoundError:
            print('Exception: FileNotFoundError -- strerror:', 'No such file or directory')
            return None
        except SyntaxError:
            print('Exception: OSError -- strerror: None')
            return None

    @staticmethod
    def display(array):
        '''takes a numpy array as an argument and displays the corre- sponding RGB image.'''
        try:
            if not isinstance(array, np.ndarray):
               raise TypeError("Error : not a numpy array") 
            plt.imshow(array)
            plt.show()
        except TypeError:
            return 