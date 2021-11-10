class Vector(object):
    def __init__(self, args):
        #constructeur INT
        if isinstance(args, int):
            if args < 0:
                raise ValueError("INT init : int value >= 0 needed")
            self.values = []           
            for i in range(args):
                self.values.append([float(i)])
            line = len(self.values)
            column = 1
        
        #constructeur RANGE
        elif isinstance(args, tuple):
            if not len(args) == 2:
                raise ValueError("RANGE init : need 2 numbers only")
            if not isinstance(args[0], int) or not isinstance(args[1], int):
                raise ValueError("RANGE init : inut needs to be INT")
            self.values = []
            my_range = range(args[0], args[1])
            for i in my_range:
                self.values.append([float(i)])
            line = len(self.values)
            column = 1
        
        elif isinstance(args, list):
            if len(args) == 0:
                raise ValueError("LIST init : list size > 0 needed")
            nb_list = sum((isinstance(elm, list) for elm in args))
            
            #constructeur LIST OF FLOAT
            if nb_list == 0: #list of floats
                nb = sum((isinstance(elm, float) for elm in args))
                if not nb == len(args):
                    raise ValueError("LIST OF FLOATS init : only floats needed")
                self.values = args
                line = 1
                column = len(args)
           
            #constucteur list of list of floats
            else: 
                for elm in args:
                    if not len(elm) == 1:
                        raise ValueError("LIST OF LIST OF FLOATS init : only list of size 1")
                for elm in args:
                    if not isinstance(elm[0], float): 
                        raise ValueError("LIST OF LIST OF FLOATS init : only floats needed")
                self.values = args
                line = len(self.values)
                column = 1
        else:
            raise ValueError("CONSTRUCTEUR fail : wrong type of inputs")
        self.shape = (line, column)

    def __add__(self, vec):
        print("-- enter ADD --")
        if not isinstance(vec, Vector):
            raise ValueError("ADD: not a type Vector")
        if self.shape != vec.shape:
            raise ValueError("ADD: vectors not of same shape")
        new_list =[]
        if self.shape[0] == 1: # row vector
            for i in range(self.shape[1]):
                new_list.append(self.values[i] + vec.values[i])
        else: #column vector
            for i in range(self.shape[0]):
                new_list.append([self.values[i][0] +vec.values[i][0]])
        return Vector(new_list)

    def __radd__(self, vec):
        print("-- enter RADD -- ")
        if vec == 0:
            return self
        else:
            return self.__add__(vec)
    
    def __sub__(self, vec):
        print("-- enter SUB --")
        if not isinstance(vec, Vector):
            raise ValueError("SUB: not a type Vector")
        if self.shape != vec.shape:
            raise ValueError("SUB: vectors not of same shape")
        new_list =[]
        if self.shape[0] == 1: # row vector
            for i in range(self.shape[1]):
                new_list.append(self.values[i] - vec.values[i])
        else: #column vector
            for i in range(self.shape[0]):
                new_list.append([self.values[i][0] - vec.values[i][0]])
        return Vector(new_list)
    
    def __rsub__(self, vec):
        print("-- enter RSUB --")
        if vec == 0:
            return self
        else:
            return self.__sub__(vec)
    
    def __truediv__(self, m):
        print("-- enter TRUEDIV --")
        if not isinstance(m, (int, float)):
            raise ValueError("TRUEDIV: scalar is not an int or a float")
        if m == 0:
            raise ValueError("TRUEDIV: division by 0 does not exist")
        new_list =[]
        if self.shape[0] == 1: # row vector
            for i in range(self.shape[1]):
                new_list.append(self.values[i] / m)
        else: #column vector
            for i in range(self.shape[0]):
                new_list.append([self.values[i][0] / m])
        return Vector(new_list)
    
    def __rtruediv__(self, vec):
        print("-- enter RTRUEDIV --")
        if vec == 0:
            return self
        else:
            return self.__truediv__(vec)

    def __mul__(self, m):
        print("-- enter MUL --")
        if not isinstance(m, (int, float)):
            raise ValueError("MUL: scalar is not an int or a float")
        new_list =[]
        if self.shape[0] == 1: # row vector
            for i in range(self.shape[1]):
                new_list.append(self.values[i] * m)
        else: #column vector
            for i in range(self.shape[0]):
                new_list.append([self.values[i][0] * m])
        return Vector(new_list)
        
    def __rmul__(self, vec):
        print("-- enter RMUL --")
        if vec == 0:
            return self
        else:
            return self.__mul__(vec)
    
    def __str__(self):
	    return f"Here is the content of class:\nShape = {self.shape}\nValue = {self.values}"
   
    def __repr__(self):
	    return f"Vector(shape={self.shape} value={self.values})"

    def dot(self):
        pass

    def T(self):
        new_list = []
        if self.shape[0] == 1: #row vector
            for i in range(self.shape[1]):
                new_list.append([self.values[i]])
        else: #column
            for i in range(self.shape[0]):
                new_list.append(self.values[i][0])
        return Vector(new_list)


