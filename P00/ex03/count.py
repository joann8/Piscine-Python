import string
import fileinput

def text_analyser(*args):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text"""
    if len(args) > 1:
        print("ERROR")
        return
    
    elif len(args) < 1:
        text = input("What is the file to input?\n")
    
    else:
        text = args[0];

    c_space = 0;
    c_lower = 0;
    c_upper = 0;
    c_punctuation = 0;

    for c in text:
        if c == ' ':
            c_space += 1
        if c.isupper():
            c_upper += 1
        if c.islower():
            c_lower += 1
        if c in string.punctuation:
            c_punctuation += 1
    print("The text contains %d characters\n- %d upper letters\n- %d lower letters\n- %d punctuation marks\n- %d spaces" %(len(text), c_upper, c_lower, c_punctuation, c_space))  



    

