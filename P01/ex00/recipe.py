
def check_attributes(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
    if not isinstance(name, str) or str == "":
        print("Format pbm: name")
        return 1
    if not isinstance(cooking_lvl, int) or cooking_lvl < 1 or cooking_lvl > 5:
        print("Format pbm: cooking_lvl")
        return 1
    if not isinstance(cooking_time, int) or cooking_time < 0:
        print("Format pbm: cooking_time")
        return 1
    if isinstance(ingredients, list):
        for elmt in ingredients:
            if not isinstance(elmt, str) or elmt == "":
                print("Format pbm : Ingredients (elmt)!")
                return 1
    else:
        print("Format pbm : Ingredients (list)!")
        return 1
    if not isinstance(description, str):
        print("Format pbm: description")
        return 1
    return 0


class Recipe(object):
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if check_attributes(name, cooking_lvl, cooking_time, ingredients, description, recipe_type) == 1:
            quit()
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    
    def __str__(self):
        return("Name : " + self.name + " | Cooking_time : " + str(self.cooking_time) + " | Cooking_lvl : " + str(self.cooking_lvl) + " | Ingredients : " + str(self.ingredients) + " | Description : "  + self.description + " | Recipe_type : " + self.recipe_type)




