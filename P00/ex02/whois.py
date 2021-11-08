import sys

if len(sys.argv) > 2:
    print("ERROR")
elif len(sys.argv) == 2:
    if sys.argv[1].isdigit():
        x = int(sys.argv[1])
        if x == 0:
            print("I'm Zero.")
        elif (x % 2) == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print("ERROR")
