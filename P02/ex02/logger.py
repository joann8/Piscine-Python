import time
from random import randint
import os 

#... definition of log decorator...
def log(function):
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
    
    @log
    def start_machine(self):       
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)