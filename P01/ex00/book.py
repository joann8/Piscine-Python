
import datetime
from recipe import Recipe

def check_attributes(name):
    if not isinstance(name, str) or str == "":
        print("Format pbm: name")
        return 1
    return 0


class Book(object):
    def __init__(self, name):
        if check_attributes(name) == 1:
            quit()
        self.name = name
        self.recipes_list = {"starter":[], 'lunch':[], "dessert":[]}
        self.creation_date = datetime.datetime.now()
        self.last_update = 0
            
    def __str__(self):
        return("*********************\nName : " + self.name + " | creation_date : " + str(self.creation_date) + " | last_update : " + str(self.last_update) + "\n*********************")

    def get_recipe_by_name(self, name): 
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for key, type in self.recipes_list.items():
            for elm in type:
                if name == elm.name:
                    print(elm)
                    return elm
        print("%s is not in the recipe book" %(name))
        return None
    
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if not recipe_type == 'lunch' and not recipe_type == 'dessert' and not recipe_type == 'starter':
            print("No such recipe type")
            return
        print("Recipes of type %s are the followimg: " %(recipe_type))
        for elm in self.recipes_list[recipe_type]:
            print("   - ", end='')
            print(elm.name) 
               
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.last_update = datetime.datetime.now()
        if isinstance(recipe, Recipe):
            self.recipes_list[recipe.recipe_type].append(recipe)
            return
        else:
            print("This is not a Recipe")




