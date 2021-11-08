import string
from string import Template 

it = ( 0, 4, 132.42222, 10000, 12345.67)
print("module_0%d, ex_0%d : " %(it[0], it[1]), end='');
print("{:.2f}".format(it[2]), "{:.2e}".format(it[3]), "{:.2e}".format(it[4]), sep=', ')
 


