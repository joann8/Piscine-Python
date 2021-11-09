import sys
import string

#comment emlever la ponctuation?

if len(sys.argv) != 3 or not sys.argv[2].isdigit():
    print("ERROR")
else:
    list_words = sys.argv[1].split()
    n = int(sys.argv[2])  
    list_new=[]
    for tup in list_words:
        if len(tup) > n:
            list_new.append(tup)
    
    print(list_new)
