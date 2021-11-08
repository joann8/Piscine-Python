
    
#def delete_recipe(recipe):
#def add_recipe(recipe):
#def print_cookbookrecipe(recipe):



cookbook = { 'sandwich': { 'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'] , 'meal' : 'lunch', 'prep_time' : 10},
            'cake': { 'ingredients' : ['flour', 'sugar',' eggs'], 'meal' : 'dessert', 'prep_time' : 60},
            'salad': { 'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal' :'lunch', 'prep_time' : 15}}

def print_recipe(recipe):
    if recipe in cookbook:
        print("Ingredients list: ", end='')
        print(cookbook[recipe]['ingredients'])
        print("To be eaten for %s" %(cookbook[recipe]['meal']))
        print("Takes %d minutes of cooking:" %(cookbook[recipe]['prep_time']))
    else:
        print("This recipe does not exist")  

while(1):
    text = input("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n");
    if not text.isdigit():
        print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
    else:
        x = int(text)
        if (x == 1):
            print("Add recipe!")
            
        elif (x == 2):
            print("Delete recipe!")
        elif (x == 3):
            text2 = input("Please enter the recipe's name to get its details\n")
            print_recipe(text2)
        elif (x == 4):
            print("Print cookbook!")
        elif (x == 5):
            print("Quit!")
            break
        else:
            print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
    
