cookbook = { 'sandwich': { 'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'] , 'meal' : 'lunch', 'prep_time' : 10},
            'cake': { 'ingredients' : ['flour', 'sugar',' eggs'], 'meal' : 'dessert', 'prep_time' : 60},
            'salad': { 'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal' :'lunch', 'prep_time' : 15}}

def print_recipe(recipe):
    if recipe in cookbook:
        print("**********Recipe for %s **********" %(recipe))
        print("Ingredients list: ", end='')
        print(cookbook[recipe]['ingredients'])
        print("To be eaten for %s" %(cookbook[recipe]['meal']))
        print("Takes %d minutes of cooking:" %(cookbook[recipe]['prep_time']))
    else:
        print("This recipe does not exist")  

def print_cookbook():
    print("This Cookbook has %d recipe(s)" %(len(cookbook)))
    for tup in cookbook:
        print(tup, end=' ')

def delete_recipe(recipe):
    if recipe in cookbook:
        del cookbook[recipe]
        print("The recipe %s has been deleted" %(recipe))
    else:
        print("This recipe does not exist")  

def add_recipe(name):
    if name in cookbook:
        print("Recipe for %s already exists" %(name))
        return
    cookbook[name] ={}
    ingredient = input("Please enter all your ingredients separated by a space and then enter:\n").split()
    cookbook[name]['ingredients'] = ingredient
    meal_type =  input("Please enter the meal type: \n")
    cookbook[name]['meal'] = meal_type
    nb = -1
    while nb < 0:
        prep_time = input("Please enter the prep_time:\n")
        if prep_time.isdigit():
            nb = int(prep_time)
        if nb < 0:
            print("You need to enter a positive number")
    cookbook[name]['prep_time'] =nb
    #cookbook[name] ={'ingredients' : ingredient, 'meal' : meal_type, 'prep_time' : prep_time }

while(1):
    text = input("\nPlease select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n");
    if not text.isdigit():
        print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
    else:
        x = int(text)
        if (x == 1):
            name = input("Please enter the recipe's name:\n")
            add_recipe(name)
        elif (x == 2):
            text2 = input("Please enter the recipe's name you want to delete\n")
            delete_recipe(text2)
        elif (x == 3):
            text2 = input("Please enter the recipe's name to get its details\n")
            print_recipe(text2)
        elif (x == 4):
            print_cookbook()
        elif (x == 5):
            print("See you soon!")
            break
        else:
            print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
    
