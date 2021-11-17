import numpy as np
import copy

class ColorFilter():

	@staticmethod
	def invert(array):
		"""
		Inverts the color of the array received as a numpy array.
		Args:
			array: numpy.ndarray corresponding to the array.
		Return:
			array: numpy.ndarray corresponding to the transformed array.
			None: otherwise.
		Raises:
			This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray):
			print("This array is not an numpy array")
			return None
		return 1 - array[:,:,:3]

	@staticmethod
	def to_blue(array):
		"""
		Applies a blue filter to the array received as a numpy array.
		Args:
			array: numpy.ndarray corresponding to the array.
		Return:
			array: numpy.ndarray corresponding to the transformed array.
			None: otherwise.
		Raises:
			This function should not raise any Exception.
		◦ Authorized functions:.zeros,.shape,.dstack
		◦ Authorized operator:None
		"""
		if not isinstance(array, np.ndarray):
			print("This array is not an numpy array")
			return None
		blue_arr = np.zeros(np.shape(array[:,:,:3]))
		blue_arr[:,:,2] = array[:,:,2]
		return blue_arr

	@staticmethod
	def to_green(array):
		"""
		Applies a green filter to the array received as a numpy array.
		Args:
			array: numpy.ndarray corresponding to the array.
		Return:
			array: numpy.ndarray corresponding to the transformed array.
			None: otherwise.
		Raises:
			This function should not raise any Exception.
		◦ Authorized functions: copy. deepcopy 
		◦ Authorized operator: *
		"""
		if not isinstance(array, np.ndarray):
			print("This array is not an numpy array")
			return None
		return copy.deepcopy(array[:,:,:3] * [0, 1, 0])
	
	@staticmethod
	def to_red(array): 
		"""
		Applies a red filter to the array received as a numpy array.
		Args:
			array: numpy.ndarray corresponding to the array.
		Return:
			array: numpy.ndarray corresponding to the transformed array.
			None: otherwise.
		Raises:
			This function should not raise any Exception.
			Authorized functions:.to_green,.to_blue
		"""
		if not isinstance(array, np.ndarray):
			print("This array is not an numpy array")
			return None
		obj = ColorFilter()
		return (array[:,:,:3]  - obj.to_blue(array) - obj.to_green(array))

	@staticmethod
	def to_celluloid(array): 
		"""
		Applies a celluloid filter to the array received as a numpy array.
		Celluloid filter must display at least four thresholds of shades.
		Be careful! You are not asked to apply black contour on the object,
		you only have to work on the shades of your arrays.
		Remarks:
			celluloid filter is also known as cel-shading or toon-shading.
		Args:
			array: numpy.ndarray corresponding to the array.
		Return:
			array: numpy.ndarray corresponding to the transformed array.
			None: otherwise.
		Raises:
			This function should not raise any Exception.
			Authorized functions:.arange,.linspace
	 """
		if not isinstance(array, np.ndarray):
			print("This array is not an numpy array")
			return None
		interval = np.linspace(0, 1, 5)
		for i in np.arange(1, 5):
			array[(array>=interval[i - 1]) & (array<interval[i])] = interval[i - 1]
		return array

	@staticmethod
	def to_grayscale(array, filter, weight = None): #proto change pour l'exemple
		"""
		Applies a grayscale filter to the array received as a numpy array.
		For filter = ’mean’/’m’: performs the mean of RBG channels.
		For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
		Args:
			array: numpy.ndarray corresponding to the array.
			filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
			weights: [kwargs] list of 3 floats where the sum equals to 1,
					corresponding to the weights of each RBG channels.
		Return:
			array: numpy.ndarray corresponding to the transformed array.
			None: otherwise.
		Raises:
			This function should not raise any Exception.
			◦ Authorizedfunctions:.sum,.shape,.tile,.reshape,.dstack,.broadcast_to,.as_type 
			◦ Authorized operator:*,/

		 """
		#check types
		if not isinstance(filter, str) or not isinstance(array, np.ndarray):
			print("Wrong types inputs")
			return None
		if filter not in['m', 'mean', 'w', 'weight']:
			print("This filter inputs is not correct ")
			return None
		if weight is not None:
			if not isinstance(weight,list) or len(weight) != 3 and not isinstance(weight[0], float) or not isinstance(weight[1], float) or not isinstance(weight[2], float) or weight[0] + weight[1] + weight[2] != 1:
				print("Need 3 floats with sum = 1")
				return None
			else:
				r = weight[0]
				g = weight[1]
				b = weight[2]
		else:
			r = 0.299
			g = 0.587
			b = 0.114
		
		means =  array[:,:,0] * r + array[:,:,1] * g + array[:,:,2] * b  
		return np.dstack((means, means, means,  array[:,:,3]))
