import sys

def mysum(x, y):
    print('{0: <12}'.format("Sum:"), x + y)
    return (x + y)

def mydifference(x, y):
    print('{0: <12}'.format("Difference:"), x - y)
    return (x - y)

def myproduct(x, y):
    print('{0: <12}'.format("Product:"), x * y)
    return (x * y)

def myquotient(x, y):
    if y == 0:
        print('{0: <12}'.format("Quotient:"), end='')
        print("ERROR (div by zero)")
        return("ERROR (div by zero)")
    else:
        print('{0: <12}'.format("Quotient:"), x / y)
        return (x / y)

def myremainder(x, y):
    if y == 0:
        print('{0: <12}'.format("Remainder:"), end='')
        print("ERROR (modulo by zero)")
        return("ERROR (modulo by zero)")
    else:
        print('{0: <12}'.format("Remainder:"), x % y)
        return (x % y)

def myres(x, y):
    return ((mysum(x, y), mydifference(x, y), myproduct(x, y), myquotient(x, y), myremainder(x, y)))

if len(sys.argv) < 3:
     print("Usage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3 ")

elif  len(sys.argv) > 3:
    print("InputError: too many arguments")

else:
    if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
        print("InputError: only numbers")
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        myres(x, y)
        
