import time 
from random import randint
import os 

#... definition of log decorator...
def logger(function):
    def new_function(elem, water_lvl=None):

        file_log = open('machine.log', "a")
        start = time.time()
        if water_lvl is None:
            ret = function(elem)
        else:
            ret = function(elem, water_lvl)
        end = time.time()
        USER = os.getenv("USER")
        ft_name = "{0:<19}".format(function.__name__.replace("_", " ").title())
        exec = end - start
        if exec > 1:
            file_log.write(f"({USER})Running: {ft_name}[ exec-time = {exec:.3f} s ]\n") 
        else:
            file_log.write(f"({USER})Running: {ft_name}[ exec-time = {(exec * 1000):.3f} ms]\n") 
        file_log.close()
        return ret
    return new_function

