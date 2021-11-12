import numpy as np
import numpy as np
from numpy.core.numeric import array_equal

class ScrapBooker:
    # within the class
    def crop(self, array, dim, position=(0,0)): 
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width oof the image) from the coordinates given by position arguments.
        Args:
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        Returns:
            new_arr: the cropped numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
    """
        
        #check types
        if not isinstance(array, np.ndarray):
            print("This array is not an numpy array")
            return None
        if not isinstance(dim, tuple) or not isinstance(dim[0], int) or not isinstance(dim[1], int) or dim[0] <= 0 or dim[1] <= 0:
            print("Dim paramaters need to be positive integers")
            return None
        if position is not None:
            if not isinstance(position, tuple) or not isinstance(position[0], int) or not isinstance(position[1], int) or position[0] < 0 or position[1] < 0:
                print("Positions  paramaters need to be positive integers")
                return None

        #check datas
        if position[0] not in range(0, array.shape[0]) or position[1] not in range(0, array.shape[1]):
            print("Position out of array")
            return None
        if (position[0] + dim[0] - 1) not in range(0, array.shape[0]) or (position[1] + dim[1] - 1) not in range(0, array.shape[1]):
            print("Position + Dim out of array")
            return None
        return np.array(array[position[0]:(position[0] + dim[0]), position[1]:(position[1] + dim[1])])
    
    def thin(self, array, n, axis): 
        """
            Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
            Args:
                array: numpy.ndarray.
                n: non null positive integer lower than the number of row/column of the array (depending of axis value).
                axis: positive non null integer.
            Returns:
                new_arr: thined numpy.ndarray.
                None otherwise (combinaison of parameters not incompatible).
            Raises:
                This function should not raise any Exception.
        """
        #check types
        if not isinstance(array, np.ndarray):
            print("This array is not an numpy array")
            return None
        if not isinstance(n, int) or n <= 0:
            print("n need to be a non null positive integer")
            return None
        if not isinstance(axis, int) or axis < 0 or axis > 1:
            print("axis need to be a 0 or 1")
            return None
        
        new_array = np.array(array)
        #Enonce pas logique, les axis 0et 1 sont inverses
        if (axis == 1): #we remove lines
            for index in range(new_array.shape[0] - 1, -1, -1):
                if (index + 1) % n == 0:
                    new_array = np.delete(new_array, index, axis=0)

        else: #we remove columns
            for index in range(new_array.shape[1] - 1, -1, -1):
                if (index + 1) % n == 0:
                    new_array = np.delete(new_array, index, axis=1)                  
        return new_array

    def juxtapose(self, array, n, axis): 
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Returns:
            new_arr: juxtaposed numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        #check types
        if not isinstance(array, np.ndarray):
            print("This array is not an numpy array")
            return None
        if not isinstance(n, int) or n <= 0:
            print("n need to be a non null positive integer")
            return None
        if not isinstance(axis, int) or axis < 0 or axis > 1:
            print("axis need to be a 0 or 1")
            return None

        new_array = np.array(array)
        if axis == 0: 
            for i in range(n - 1):
                new_array = np.append(new_array, array, axis)
            return new_array
        else:
            for i in range(n - 1):
                new_array = np.append(new_array, array, axis)
            return new_array      

    def mosaic(self, array, dim): 
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
            array: numpy.ndarray.
            dim: tuple of 2 integers.
        Returns:
            new_arr: mosaic numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        
        #check types
        if not isinstance(array, np.ndarray):
            print("This array is not an numpy array")
            return None
        if not isinstance(dim, tuple) or not isinstance(dim[0], int) or not isinstance(dim[1], int) or dim[0] <= 0 or dim[1] <= 0:
            print("Dim paramaters need to be positive integers")
            return None
        new_array = self.juxtapose(array, dim[0], 0)
        new_array = self.juxtapose(new_array, dim[1], 1)
        return new_array
        
      