
def check_attributes(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
    print("********** Format check start *****************")
    if isinstance(name, str) and not str == "":
        print("Name : Format ok!")
    else:
        print("Format pbm: name")
        return 1
    if isinstance(cooking_lvl, int) and cooking_lvl > 0 and cooking_lvl < 6:
        print("Cooking_lvl: Format ok!")
    else:
        print("Format pbm: cooking_lvl")
        return 1
    if isinstance(cooking_time, int) and cooking_time >= 0:
        print("Cooking_time: Format ok!")
    else:
        print("Format pbm: cooking_time")
        return 1
    if isinstance(ingredients, list):
        for elmt in ingredients:
            if not isinstance(elmt, str) or elmt == "":
                print("Format pbm : Ingredients (elmt)!")
                return 1
        print("Ingredients: Format ok!")
    else:
        print("Format pbm : Ingredients (list)!")
        return 1
    if isinstance(description, str):
        print("Description : Format ok!")
    else:
        print("Format pbm: description")
        print("********** Format check end *****************")
        return 1
    print("********** Format check end *****************")
    return 0


class Recipe(object):
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if check_attributes(name, cooking_lvl, cooking_time, ingredients, description, recipe_type) == 1:
            print("Error")
            pass
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    
    def __str__(self):
        return("Name : " + self.name + " | Cooking_time : " + str(self.cooking_time) + " | Cooking_lvl : " + str(self.cooking_lvl) + " | Ingredients : " + str(self.ingredients) + " | Description : "  + self.description + " | Recipe_type : " + self.recipe_type)

recipe = Recipe("sushi", 2,20, ["saumon", "avocats"], "un petit suhshi", "lunch")
print(recipe)
recipe2 = Recipe("sushi", 10,20, ["saumon", "avocats"], "un petit suhshi", "lunch")
print(recipe2)
recipe3 = Recipe("sushi", 3, 20, ["saumon", "avocats"], "un petit suhshi", "lunch")
print(recipe3)
