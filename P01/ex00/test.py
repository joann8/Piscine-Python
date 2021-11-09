from recipe import Recipe
from book import Book

book = Book("My recipe book")
to_print = str(book)

sushi = Recipe('sushi', 3, 20, ['saumon', 'riz'], 'good sushi maki', 'lunch')
pho = Recipe('pho', 5, 33, ['boeuf', 'soja', 'coriandre'], 'best dish ever', 'lunch')
pana = Recipe('pannacota', 1, 10, ['creme', 'fruits rouges'], 'italian delice', 'dessert')
ile = Recipe('ile flottante', 2, 55, ['creme', 'oeufs'], 'personne n\'en mage', 'dessert')
soupe = Recipe('soupe', 3, 15, ['legumes', 'fromage'], 'for winter', 'starter')
gaspa = Recipe('gaspacho', 2, 25, ['legumes', 'croutons'], 'for summer', 'starter')

book.add_recipe(sushi)
book.add_recipe(pho)
book.add_recipe(pana)
book.add_recipe(ile)
book.add_recipe(soupe)
book.add_recipe(gaspa)

book.get_recipe_by_name('pho')
book.get_recipe_by_name('xiao long bao')
book.get_recipes_by_types('dessert')
book.get_recipes_by_types('dinner')
to_print = str(book)
print(to_print)
