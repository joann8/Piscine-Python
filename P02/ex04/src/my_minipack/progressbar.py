import time
from random import randint
import os 
from time import time
from time import sleep

def progressbar(listing, sizebar=30):
    elapsed_time = 0
    loopend = 0.01
    count = len(listing)
    for i, item in enumerate(listing):
        loopstart = time()
        x = int(sizebar * (i + 1) / count)
        print("\rETA: %.2fs [%3d%%][%s>%s] %d/%d | elapsed time %.2fs"
              % (loopend * (len(listing) - i) + elapsed_time,
                 (i + 1) / count * 100,
                 "=" * x,
                 " " * (sizebar - x), (i + 1), count, elapsed_time),
              end='', flush=True)
        yield item
        loopend = time() - loopstart
        elapsed_time = elapsed_time + loopend


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

class CoffeeMachine():
    water_level = 100
    
    @logger
    def start_machine(self):       
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @logger
    def boil_water(self):
        return "boiling..."
    
    @logger
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @logger
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
