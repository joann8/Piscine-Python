t = (19,42,21)
print("The 3 numbers are: ", end='')
for tup in t:
    if (tup == t[-1]):
        print(tup)
    else:
        print(tup, end=', ')
        
