from random import randint

def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    if not isinstance(text, str):
       print("ERROR")
       quit()

    mylist = text.split(sep)
   
    if option is None:
        for word in mylist:
            yield word
    else:
        if option == 'shuffle':
            shuffle_list = []
            while len(mylist) > 0:
                i = randint(0, len(mylist) - 1)
                shuffle_list.append(mylist[i])
                mylist.remove(mylist[i])
            for word in shuffle_list:
                yield word
        elif option == 'unique':
            unique_list = []
            for word in mylist:
                if word not in unique_list:
                    unique_list.append(word) 
            for word in unique_list:
                yield word
        elif option == 'ordered':
            mylist.sort()
            for word in mylist:
                yield word
        else:
            print("ERROR")

